# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
import pandas as pd
import geojson
from geojson import Feature, Point, FeatureCollection
import json
import math
import covid_constant as constants
import covid_util as util
import covid_download as downloader

name_change = {
  'United States': 'US',
  'South Korea':'Korea, South'
}

def createDictFromDataFrame(df):
  dictionary = {}
  for index, row in df.iterrows():
    if (row['name'] in name_change):
      dictionary[name_change[row['name']]] = row['latlng']
    else:
      dictionary[row['name']] = row['latlng']
  return dictionary    

def getCovid19DataByCountry(fileName):
  df = pd.read_csv(fileName)
  #get only country and the latest date
  subset = df[[df.columns[1], df.columns[-1]]]
  summary = subset.groupby(subset.columns[0]).sum().reset_index()
  return summary

def mergeDataFrames(df1, df2):
  tmp = df2[df2.columns[-1]]
  df = pd.concat([df1, tmp], axis=1)
  return df

def createFeatureCollectionsByCountry(df, countries):
  features = []
  for index, row in df.iterrows():
    if row[0] in countries:
      latlng = countries[row[0]]
      pt = Point([float(latlng[1]), float(latlng[0])])
      props = {
        'color': util.getColor(int(row[1])),
        'radius': util.getRadius(int(row[1])),
        'note': row[0] + '\n' 
          +'# of confirmed:' 
          + str(row[1]) + '\n'
          + '# of death:'
          + str(row[2])
      }
      feature = Feature(geometry=pt, id=index, properties=props)
      features.append(feature)
    else:
      print('Country not found ' + row[0])

  feature_collections = FeatureCollection(features)
  return feature_collections

def getCovid19ByCountry():
  countriesDf = pd.read_json('countries.json')
  countries = createDictFromDataFrame(countriesDf)
  confirmed = getCovid19DataByCountry(constants.OUTPUT_DIR + constants.CONFIRM_FILE_NAME)
  death = getCovid19DataByCountry(constants.OUTPUT_DIR + constants.DEATH_FILE_NAME)
  df = pd.concat([confirmed, death], axis=1)
  feature_collections = createFeatureCollectionsByCountry(df, countries)
  with open('covid-by-country.js', 'w') as writer:
    writer.write('var infected=\n')
    writer.write(geojson.dumps(feature_collections))

getCovid19ByCountry()

# https://developer.here.com/blog/run-circles-around-geojson-beginner-to-advanced-with-here-xyz
# center = Point(0,0)          # Null Island
# circle = center.buffer(0.3)  # Degrees Radius
# print(geojson.dumps(shapely.geometry.mapping(circle)))

