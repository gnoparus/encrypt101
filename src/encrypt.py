import encryptor


def main():
    print("Encrypting")
    enc = encryptor.Encryptor()

    loaded_key = enc.key_load("mykey.key")

    enc.file_encrypt(loaded_key, "grades.csv", "enc_grades.csv")


if __name__ == "__main__":
    main()
