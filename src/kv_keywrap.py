import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm
from azure.keyvault.keys.crypto import KeyWrapAlgorithm


def main():
    keyVaultName = os.environ["KEY_VAULT_NAME"]
    keyName = os.environ["KEY_NAME"]

    credential = DefaultAzureCredential()
    key_client = KeyClient(
        vault_url=f"https://{keyVaultName}.vault.azure.net/", credential=credential
    )

    print(f"Getting key {keyName} in key vault: {keyVaultName}")
    key = key_client.get_key(keyName)
    crypto_client = CryptographyClient(key, credential=credential)
    key_bytes = b"a40fc1ce666d8588809b1d22217c666169a11107a8d6777d903faaad23444855"

    # the result holds the encrypted key and identifies the encryption key and algorithm used
    result = crypto_client.wrap_key(KeyWrapAlgorithm.rsa_oaep, key_bytes)
    encrypted_key = result.encrypted_key
    print(result.key_id)
    print(result.algorithm)
    print(encrypted_key)


if __name__ == "__main__":
    main()
