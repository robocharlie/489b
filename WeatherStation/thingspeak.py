# Thingspeak module
#
# Send a data list to a selected Thingspeak channel.
# Dynamically determine the number of fields based on data list length
# Data must be sent in the same order as Thingspeak field numbering scheme
#
# Example: 
# from thingspeak import sendData
# sendData([temp. pressure, humidity], key="FG123123AWEJHC12")

import httplib, urllib
import time

def sendData(dataList, key="RV3H5FDV17IZNFY7"):
  dataDictionary = {}   # start with a null dictionary
  for i in range(len(dataList)):
    dataDictionary['field'+str(i+1)] = dataList[i] # add data 
  dataDictionary['api_key'] = key                  # append the API key
  params = urllib.urlencode(dataDictionary)        # encode the dictionary 
  headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
  conn = httplib.HTTPConnection("api.thingspeak.com:80")
  conn.request("POST", "/update", params, headers)
  response = conn.getresponse()
  print(response.status, response.reason)
