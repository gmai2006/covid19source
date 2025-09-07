import pandas as pd 
from fbprophet import Prophet
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import json
import datetime
import math
import geojson
from geojson import Feature, Point, FeatureCollection
import plotly.express as px
import covid_util as util

def createStateGeo(fileName):
  states_dict = {}
  with open(fileName) as json_file:
      data = json.load(json_file)
      for item in data:
        states_dict[item['state']] = item
  return states_dict        

def generateDict(data):
  lines = data.split('\n')
  dates = []
  total = []
  for line in lines:
    if line.strip() == '': 
      continue
    tokens = line.split(',')
    dates.append(tokens[0])
    total.append(tokens[1])

  return {
    'ds': dates,
    'y': total
  }

def generate_header_data(cvs_data, state):
  lines = cvs_data.split('\n')
  header = ''
  data = ''
  for x in range(1, len(lines)-1):
    if lines[x].startswith('ds'):
      header = lines[x].replace('ds', 'State,X,Y')
    elif lines[x].startswith('yhat'):
      data = lines[x].replace('yhat', state['state'] + ',' + str(state['longitude']) + ',' + str(state['latitude']))
  return (header, data)

def runProphet(df):
  m = Prophet()
  m.fit(df)
  future = m.make_future_dataframe(periods=7)
  forcast = m.predict(future)
  # forcast = forecast.rename({'ds':'#', 'yhat':case_type})
  forcast = forcast[['ds', 'yhat']]
  return m, forcast

def build_model_for_states(case_type, df, state_dict):
  result_header = ''
  result_body = []
  
  for index, row in df.iterrows():
    if index in state_dict:
      print('Start running for state ' + index)
      data = row.to_csv()
      dictionary = generateDict(data)
      df = pd.DataFrame.from_dict(dictionary)
      df = df.iloc[55:]
      prophet, forcast = runProphet(df)
      
      forcast.rename(columns={'ds':'date', 'yhat':case_type + '_cases'}, inplace=True)
      fig = px.line(forcast, x='date', y=case_type + '_cases', title='Predicted Growth Rate for ' + index)
      fig.write_image('/backup/apps/covid19admin/src/views/' + index + '_' + case_type + '_predicted_growth_rate.png')
      
      #save result into a csv file.
      forcast = forcast.iloc[-5:].T
      (header, body) = generate_header_data(forcast.to_csv(), state_dict[index])
      result_header = header
      result_body.append(body)
  result_body.insert(0, result_header)
  return result_body

  
def create_predictive_models(fileName, outputFile):
  df = pd.read_csv(fileName)
  df = df.iloc[:, 6:]
  df = df.drop(['Country_Region', 'Lat', 'Long_', 'Combined_Key'], axis=1)
  df = df.rename(columns={'Province_State':'State'})
  df = df.groupby('State').sum()

  state_dict = createStateGeo('./us_state_geo.json')
  if 'confirm' in fileName:
    case_type = 'confirm'
  else:
    case_type = "deaths"
  lst = build_model_for_states(case_type, df, state_dict)

  with open(outputFile, 'w') as writer:
    for line in lst:
      writer.write(line + '\n')

def generate_all():
  fileList = [
    '/backup/test_data/time_series_covid19_confirmed_US.csv',
    '/backup/test_data/time_series_covid19_deaths_US.csv',
    # '/backup/test_data/time_series_covid19_recovered_US.csv'
  ]

  outputList = [
    './predictive_time_series_covid19_confirmed_US.csv',
    './predictive_time_series_covid19_deaths_US.csv',
    # './predictive_time_series_covid19_recovered_US.csv'
  ]

  for index in range(len(fileList)):
    print('Start building predictive model for ' + fileList[index])
    create_predictive_models(fileList[index], outputList[index])

def parse_date(date_time_str):
  date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
  return str(date_time_obj.date())

def getStates(df):
  return df.iloc[:, 0:3]

def createFeatureCollections(df):
  features = []
  for index, row in df.iterrows():
    if math.isnan(row[1]) or math.isnan(row[2]):
      continue

    pt = Point([float(row[1]), float(row[2])])
    props = {
      'color': util.getColor(int(row[3])),
      'radius': util.getRadius(int(row[3])),
      'note': row[0] + '\n' 
        +'# confirmed:' 
        + str(row[3]) + '\n'
        + '# death:'
        + str(row[4])  + '\n'
    }
    feature = Feature(geometry=pt, id=index, properties=props)
    features.append(feature)
  return FeatureCollection(features)

def create_data_files():
  pd.options.display.float_format = '{:,.0f}'.format
  confirmeddf = pd.read_csv('predictive_time_series_covid19_confirmed_US.csv')
  deathdf = pd.read_csv('predictive_time_series_covid19_deaths_US.csv')
  state = getStates(confirmeddf)
  headers = confirmeddf.columns[3:]
  # print(headers)
  for header in headers:
    fileName = '/backup/apps/covid19admin/src/views/Charts/predictive_' + parse_date(header) + '.json'
    confirm = confirmeddf[header]
    confirm = confirm.rename('Confirmed')
    deaths = deathdf[header]
    deaths = deaths.rename('Deaths')
    df = pd.concat([state, confirm, deaths], axis=1)
    df['Confirmed'] = df['Confirmed'].astype(int)
    df['Deaths'] = df['Deaths'].astype(int)
    feature_collections = createFeatureCollections(df)
    with open(fileName, 'w') as writer:
      writer.write(geojson.dumps(feature_collections))


generate_all()
# create_data_files()


      
   