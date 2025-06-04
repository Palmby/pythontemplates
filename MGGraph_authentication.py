from azure.identity import ClientSecretCredential

secret_creds = {
"tenant_id": '',
"client_id": '',
"client_secret":''
}
credential = ClientSecretCredential(**secret_creds)

'''
Documentation on how to Make Calls:
Overview:
https://learn.microsoft.com/en-us/graph/sdks/sdks-overview

Python SDK Docs:
https://learn.microsoft.com/en-us/graph/sdks/sdk-installation?tabs=python
'''
