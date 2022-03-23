import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm


def main():
    keyVaultName = os.environ["KEY_VAULT_NAME"]
    keyName = os.environ["KEY_NAME"]

    credential = DefaultAzureCredential()
    key_client = KeyClient(
        vault_url=f"https://{keyVaultName}.azure.net/", credential=credential
    )

    print(f"Getting key {keyName} in key vault: {keyVaultName}")
    key = key_client.get_key(keyName)
    crypto_client = CryptographyClient(key, credential=credential)
    plaintext = b"plaintext"

    print(f"Encrypting")
    result = crypto_client.encrypt(EncryptionAlgorithm.rsa_oaep, plaintext)
    print(f"result = {result}")

    print(f"Decrypting")
    decrypted = crypto_client.decrypt(result.algorithm, result.ciphertext)
    print(f"decrypted = {decrypted}")


if __name__ == "__main__":
    main()
