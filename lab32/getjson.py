
import urllib2
import json

def getJSON(urlData):
  webUrl = urllib2.urlopen(urlData) 	# Open the URL and read the data
  if (webUrl.getcode() == 200):		# verify that "ok" code received
    data = webUrl.read()
  else:
    data = "Server error: " + str(webUrl.getcode())
  return(json.loads(data))