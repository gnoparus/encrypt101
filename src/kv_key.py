import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm


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
    plaintext = b"Empower data scientists and developers to build, deploy, and manage high-quality models faster and with confidence."

    print(f"Encrypting plaintext = {plaintext}")
    result = crypto_client.encrypt(EncryptionAlgorithm.rsa_oaep, plaintext)
    print(f"result.ciphertext = {result.ciphertext}")

    print(f"Decrypting")
    decrypted = crypto_client.decrypt(result.algorithm, result.ciphertext)
    print(f"decrypted.plaintext = {decrypted.plaintext}")


if __name__ == "__main__":
    main()
