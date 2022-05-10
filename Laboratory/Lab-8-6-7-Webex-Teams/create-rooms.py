import requests

# Персональный токен, валидный 12 часов 
access_token = "ZGFhZDQxOWEtYTEwMC00OTY2LTk0N2ItNjgzNjVkMjdmMjFmOGQ0ODUxZTctMDFj_PE93_205195e3-62e4-48fc-840b-cdb6117315b4"
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'Подготовка к собесу ASMR!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
