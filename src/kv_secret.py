import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from datetime import datetime


def main():
    keyVaultName = os.environ["KEY_VAULT_NAME"]
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    # secretName = input("Input a name for your secret > ")
    # secretValue = input("Input a value for your secret > ")

    d = datetime.now()
    secretName = f"secretName{d}"
    secretValue = f"secretValue{d}-{d}"

    print(
        f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ..."
    )

    client.set_secret(secretName, secretValue)

    print(" done.")

    print(f"Retrieving your secret from {keyVaultName}.")

    retrieved_secret = client.get_secret(secretName)

    print(f"Your secret is '{retrieved_secret.value}'.")
    print(f"Deleting your secret from {keyVaultName} ...")

    poller = client.begin_delete_secret(secretName)
    deleted_secret = poller.result()

    print(" done.")


if __name__ == "__main__":
    main()
