#Default Template to do an API Call utilizing Client Credentials#

import requests


client_id = ''
client_secret = ''

url = ''


body = {
    "grant_type": "client_credentials",
    "client_id": client_id, 
    "client_secret": client_secret,
    "scope": ""
}


tokenRequest = requests.post(url,data=body)

access_token = tokenRequest.json()["access_token"]

payload_url = ""
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
    }
    
response = requests.get(payload_url, headers=headers)
json_mess = response.json()

