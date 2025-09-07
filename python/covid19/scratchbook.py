
# https://gist.github.com/meiqimichelle/7727723
import pandas as pd 

# df = pd.read_csv('/backup/test_data/daily.csv')
# # get only count and name
# df = df[['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
# # rename the column
# df = df.rename(columns={'Country_Region':'Location'})
# #set index
# df = df.groupby(['Location']).sum()

# #get worldwide count
# pf = df['total_confirmed'] = df['Confirmed'].sum()
# pf = df['total_death'] = df['Deaths'].sum()
# pf = df['total_recovered'] = df['Recovered'].sum()
# largest_confirm = df.nlargest(10, 'Confirmed')
# print(largest_confirm.to_json())


# df2 = df[df[df.columns[3]] == 'US']
# print(len(df2))

# df[df.columns[1]].replace('', np.nan, inplace=True)
# df[df.columns[2]].replace('', np.nan, inplace=True)
# print(len(df), len(df.columns))
# df.dropna(subset=[df.columns[1]], inplace=True)
# df.dropna(subset=[df.columns[2]], inplace=True)
# print(len(df), len(df.columns))
# print(df.head())
# df2 = df[df[df.columns[1]].isnull() | df[df.columns[1]].isnull()]
# print(len(df2))
# df3 = df2.iloc[:, 3:]
# print(df3)
# print(df[df.columns[1]].str.strip().astype(bool))
# df2 = df[df[df.columns[1]].str.strip().astype(bool)]


# df = pd.read_csv('/backup/test_data/time_series_covid19_confirmed_global.csv')
# df1 = df.iloc[:, 1:2]
# df1 = df1.rename(columns={'Country/Region': 'Country'})
# # print(df1.columns)
# df2 = df.iloc[:, 4:]
# # print(df2.columns)
# df = pd.concat([df1, df2], axis=1)
# df.reset_index(drop=True, inplace=True)
# # print(df)
# us = df[df['Country'] == 'US'].reset_index()
# us = us.T
# # us = us.rename(columns={'Country':'ds', 'US':'y'})
# # print(us.columns)
# data = us.to_csv()
# lines = data.split('\n')
# count = 0
# dates = []
# total = []
# for line in lines:
#   if line.strip() == '': 
#     continue
#   if count > 2:
#     tokens = line.split(',')
#     print(line)
#     dates.append(tokens[0])
#     total.append(tokens[1])
#   count += 1

# dict1 = {
#   'ds': dates,
#   'y': total
# }

# print(dict1)

# df = pd.DataFrame.from_dict(dict1)
# df = df.iloc[55:]
# print(df.head())
# from fbprophet import Prophet
# import matplotlib.pyplot as plt
# from pandas.plotting import register_matplotlib_converters
# m = Prophet()
# m.fit(df)
# future = m.make_future_dataframe(periods=7)
# forcast = m.predict(future)
# print (forcast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
# fig1 = m.plot(forcast)
# plt.savefig('predicted_confirmed_growth_rate.png')
# plt.show()

import json
states_dict = {}
with open('us_state_geo.json') as json_file:
    data = json.load(json_file)
    for item in data:
      df = pd.DataFrame.from_dict(item).reset_index()
      print(df)
      break

