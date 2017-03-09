from getjson import getJSON


theURL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
theJSON = getJSON(theURL)

print(theJSON)