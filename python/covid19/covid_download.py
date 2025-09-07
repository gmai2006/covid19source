import requests
from datetime import datetime, timedelta
import covid_constant as constants

github_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
def download(url, fileName):
  r = requests.get(url, allow_redirects=True)
  with open(constants.OUTPUT_DIR + fileName, 'wb') as writer:
    writer.write(r.content)

def downloadDailyFile(fileName):
  d = datetime.today() - timedelta(1)
  dateStr = d.strftime('%m-%d-%Y')
  print('Downloading file from ' + dateStr)
  url = constants.DAILY_URL + dateStr + '.csv'
  print(url)
  download(url, fileName)

def downloadReportFiles():
  download(github_url + constants.CONFIRM_FILE_NAME, constants.CONFIRM_FILE_NAME)
  download(github_url + constants.DEATH_FILE_NAME, constants.DEATH_FILE_NAME)
  download(github_url + constants.RECOVERED_FILE_NAME, constants.RECOVERED_FILE_NAME)
  download(github_url + constants.US_CONFIRM_FILE_NAME, constants.US_CONFIRM_FILE_NAME)
  download(github_url + constants.US_DEATH_FILE_NAME, constants.US_DEATH_FILE_NAME)
  # download(github_url + constants.US_RECOVERED_FILE_NAME, constants.US_RECOVERED_FILE_NAME)

downloadDailyFile(constants.DAILY_FILE_NAME)
downloadReportFiles()