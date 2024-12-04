Authentification avec le client_id_secondary : Tu utilises le client_id_secondary pour accéder à ton Key Vault et récupérer le secret pour le SP principal.
Utilisation d'un SAS Token : Le token est généré avec user_delegation_key en utilisant l'authentification du SP principal.
Téléchargement et upload du fichier CSV : Le fichier CSV est téléchargé depuis l'URL puis téléchargé dans le Data Lake via le SAS Token

#######################################################################"
#Journalisation
{
    "id": "/subscriptions/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/resourceGroups/RG_xxxxxxx/providers/Microsoft.KeyVault/vaults/keyvault-xxxxxxxxx/providers/microsoft.insights/diagnosticSettings/journal",
    "name": "journal",
    "properties": {
        "logs": [
            {
                "category": null,
                "categoryGroup": "audit",
                "enabled": true,
                "retentionPolicy": {
                    "days": 0,
                    "enabled": false
                }
            },
            {
                "category": null,
                "categoryGroup": "allLogs",
                "enabled": true,
                "retentionPolicy": {
                    "days": 0,
                    "enabled": false
                }
            }
        ],
        "metrics": [
            {
                "timeGrain": null,
                "enabled": false,
                "retentionPolicy": {
                    "days": 0,
                    "enabled": false
                },
                "category": "AllMetrics"
            }
        ],
        "storageAccountId": "/subscriptions/xxxxxxxxxxxxxxxxxxxxxxxxxxxx/resourceGroups/RG_xxxxxxxxxxxx/providers/Microsoft.Storage/storageAccounts/adlxxxxxxxi"
    }
}
git 