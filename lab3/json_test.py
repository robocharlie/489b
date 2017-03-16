from getjson import getJSON


# theURL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
theURL = "http://data.ny.gov/api/views/d6yy-54nr/rows.json"
theJSON = getJSON(theURL)

print(theJSON['meta']['view']['name'])
for i in theJSON['data']:
    print('data: ' + i[8])  # print the 9th entry ( the data)
    print('winning #: ' + i[9])  # print
    print('')
