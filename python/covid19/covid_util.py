import covid_constant as constants
import pandas as pd
import math
from geojson import Feature, Point, FeatureCollection
import numpy as np

def getRadius(val):
  if val == 0: return 0
  return max([3, math.log(val, 3)])

def getColor(val):
  if val < 100:
    return '#F7DC6F'
  elif val < 1000:
    return '#CA6F1E'
  elif val < 10000:
    return '#EC7063'
  else:
    return '#FF0000'

def getStateName(val1, val2):
  if str(val1) == 'nan': 
    return val2
  else: return val1
