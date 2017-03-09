from getjson import getJSON


#theURL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
theURL = "http://data.my.gov/api/views/d6yy-54nr/rows.json"
theJSON = getJSON(theURL)

print(theJSON)
