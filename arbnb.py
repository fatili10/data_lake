from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables d'environnement depuis le fichier .env

# Informations Azure
client_id_secondary = os.getenv("CLIENT_ID_SECONDARY")
client_secret_secondary = os.getenv("CLIENT_SECRET_SECONDARY")
tenant_id = os.getenv("tenant_id")
keyvault_url = os.getenv("keyvault_url")
storage_account_name = os.getenv("storage_account_name")
container_name = os.getenv("container_name")
blob_name = os.getenv("blob_name")
csv_url = os.getenv("csv_url")

# 1. Authentification via SP secondaire pour accéder au Key Vault
credential_secondary = ClientSecretCredential(tenant_id, client_id_secondary, client_secret_secondary)
secret_client = SecretClient(vault_url=keyvault_url, credential=credential_secondary)

# 2. Récupération du secret du SP principal depuis Key Vault
sp_principal_secret = secret_client.get_secret("secret-sp-principal").value  # Nom du secret dans Key Vault

# 3. Authentification avec le SP principal pour accéder au Data Lake
client_id_principal = os.getenv("client_id_principal")
client_secret_principal = os.getenv("client_secret_principal")

# 4. Génération du SAS Token sécurisé
blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=credential_principal)

# Utilisation d'un timestamp UTC avec un fuseau horaire
expiry_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)

sas_token = generate_blob_sas(
    account_name=storage_account_name,
    container_name=container_name,
    blob_name=blob_name,
    account_key=None,  # Pas de clé directe utilisée
    user_delegation_key=blob_service_client.get_user_delegation_key(datetime.datetime.now(datetime.timezone.utc), expiry_time),
    permission=BlobSasPermissions(write=True, create=True),
    expiry=expiry_time
)

# 5. Télécharger le fichier CSV depuis l'URL
response = requests.get(csv_url)
response.raise_for_status()  # Vérifie si le téléchargement a réussi

# 6. Upload du contenu du CSV directement dans le Data Lake via SAS
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
blob_client.upload_blob(response.content, overwrite=True)  # Assure-toi d'overrider si nécessaire

print(f"Le fichier {blob_name} a été téléchargé depuis l'URL et stocké dans le conteneur {container_name} avec succès.")
