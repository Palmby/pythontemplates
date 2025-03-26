token_url = ''
client_id = ''
client_secret = ''

def access_token(token_url, client_id, client_secret):
    data ={
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': "client_credentials" 
        
    }
    response = requests.post(token_url, data)
    token_data = response.json()
    access_token= token_data.get("access_token")
    return access_token