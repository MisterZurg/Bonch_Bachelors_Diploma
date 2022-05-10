import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Санкт-Петербург, Россия"
dest = "Baltimore, Ru"

key = "DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()
print(json_data)
