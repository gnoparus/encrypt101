import os
import time
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
    print(f"Wraping key_bytes = {key_bytes}")
    result = crypto_client.wrap_key(KeyWrapAlgorithm.rsa_oaep, key_bytes)
    encrypted_key = result.encrypted_key
    print(f"result.key_id = {result.key_id}")
    print(f"result.algorithm = {result.algorithm}")
    print(f"encrypted_key = {encrypted_key}")

    print(f"Unwraping encrypted_key")
    unwrap_result = crypto_client.unwrap_key(KeyWrapAlgorithm.rsa_oaep, encrypted_key)

    print(f"unwrap_result = {unwrap_result}")
    print(f"unwrap_result.key = {unwrap_result.key}")
    print(f"unwrap_result.algorithm = {unwrap_result.algorithm}")

    assert key_bytes == unwrap_result.key


if __name__ == "__main__":
    main()
