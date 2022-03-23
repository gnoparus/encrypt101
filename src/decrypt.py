import encryptor


def main():
    print("Decrypting data")
    enc = encryptor.Encryptor()

    loaded_key = enc.key_load("mykey.key")

    enc.file_decrypt(loaded_key, "enc_grades.csv", "dec_grades.csv")


if __name__ == "__main__":
    main()
