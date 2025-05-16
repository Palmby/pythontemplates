import requests
import base64

client_id = #putclientIDhere
client_secret = #putclientSecrethere

jwt_token = #PutJWTToken here

url = #AuthenticationURL
'''
you can break this out as
jwt_token =
(
    
)

if you want to break the string out
'''


def jwt_token_gen(client_id, client_secret, jwt_token, url):
    client_credentials = f"{client_id}:{client_secret}"
    
    basic_auth = base64.b64encode(client_credentials.encode("utf-8")).decode("utf-8")

    headers = {
        "Authorization": f"Basic {basic_auth}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    
    

    data = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt_token
    }

    response = requests.post(url, headers=headers, data=data)
    access_token = response.json()["access_token"]
    return access_token



    