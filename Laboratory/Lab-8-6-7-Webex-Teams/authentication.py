import requests
import json

# Персональный токен, валидный 12 часов 
access_token = "ZGFhZDQxOWEtYTEwMC00OTY2LTk0N2ItNjgzNjVkMjdmMjFmOGQ0ODUxZTctMDFj_PE93_205195e3-62e4-48fc-840b-cdb6117315b4"
url = "https://webexapis.com/v1/people/me"
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
