# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
import pandas as pd
import geojson
from geojson import Feature, Point, FeatureCollection
import json
import math
import numpy as np
import covid_constant as constants
import covid_util as util
import covid_download as downloader


def createFeatureCollectionsFromDailyFile(df):
  features = []
  for index, row in df.iterrows():
    if math.isnan(row[1]) or math.isnan(row[0]):
      continue

    pt = Point([float(row[1]), float(row[0])])
    props = {
      'color': util.getColor(int(row[2])),
      'radius': util.getRadius(int(row[2])),
      'note': row[-1] + '\n' 
        +'# confirmed:' 
        + str(row[2]) + '\n'
        + '# death:'
        + str(row[3])  + '\n'
        + '# recovered:'
        + str(row[4])
    }
    feature = Feature(geometry=pt, id=index, properties=props)
    features.append(feature)
  return FeatureCollection(features)


def getUSCovid19(fileName):
  df = pd.read_csv(fileName)
  df2 = df[df[df.columns[3]] == 'US']
  return df2.iloc[:, 5:]

def getWorldCovid19(fileName):
  df = pd.read_csv(fileName)
  return df.iloc[:, 5:]

def generateUS():
  df = getUSCovid19(constants.OUTPUT_DIR + constants.DAILY_FILE_NAME)
  feature_collections = createFeatureCollectionsFromDailyFile(df)
  with open('/backup/apps/covid19admin/src/views/Charts/covid-us.json', 'w') as writer:
    writer.write(geojson.dumps(feature_collections))

def generateWorld():
  df = getWorldCovid19(constants.OUTPUT_DIR + constants.DAILY_FILE_NAME)
  feature_collections = createFeatureCollectionsFromDailyFile(df)
  with open('/backup/apps/covid19admin/src/views/Charts/covid-world.json', 'w') as writer:
    # writer.write('var infected=\n')
    writer.write(geojson.dumps(feature_collections))
 
def generateCovidDailyData():
  # downloader.downloadDailyFile(constants.DAILY_FILE_NAME)
  print('Start generate US COVID-19')
  generateUS()
  print('Start generate world COVID-19')
  generateWorld()

generateCovidDailyData()

