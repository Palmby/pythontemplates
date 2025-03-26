
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient 

key_vault_url = "" #input Key URL 
secret_name = "" #input Secret Name
def retrieve_secret(key_vault_url, secretname):
    client = SecretClient(vault_url=key_vault_url, credential=DefaultAzureCredential())
    retrieved_secret = client.get_secret(secret_name)
    return retrieved_secret.value



