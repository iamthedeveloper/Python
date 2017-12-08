import requests

weatherUrl = "http://api.wunderground.com/api/8d55b1fea347ef26/hourly/q/CA/San_Francisco.json"
response = requests.get(weatherUrl)
if response.status_code == 200:
	decodedResponse = response.json()
	print(decodedResponse['hourly_forecast'][0]['temp']['english'])
else:
    print "Sorry! Not found any information!"