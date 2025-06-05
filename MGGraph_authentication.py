from azure.identity import ClientSecretCredential
import requests
from msgraph import GraphServiceClient
secret_creds = {
"tenant_id": '',
"client_id": '',
"client_secret":''
}
credential = ClientSecretCredential(**secret_creds)

client = GraphServiceClient(credentials=credential)






'''
info on the Graph SDK: https://pypi.org/project/msgraph-sdk/


use Microsoft Graph Explorer to explore API call types
https://developer.microsoft.com/en-us/graph/graph-explorer

'''


