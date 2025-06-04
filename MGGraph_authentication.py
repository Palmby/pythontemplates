from azure.identity import ClientSecretCredential

secret_creds = {
"tenant_id": '',
"client_id": '',
"client_secret":''
}
credential = ClientSecretCredential(**secret_creds)


