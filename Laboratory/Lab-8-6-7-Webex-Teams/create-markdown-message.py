import requests

# Персональный токен, валидный 12 часов 
access_token = "ZGFhZDQxOWEtYTEwMC00OTY2LTk0N2ItNjgzNjVkMjdmMjFmOGQ0ODUxZTctMDFj_PE93_205195e3-62e4-48fc-840b-cdb6117315b4"
# ID-шник комнаты :'Подготовка к собесу ASMR!'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vOGU2Njc5MTAtZDBhZS0xMWVjLWEwNmUtNDFhN2JmMTliZjEy'
message = 'Here in my garage, just bought this new Lamborghini here.'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
