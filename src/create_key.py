import encryptor


def main():
    print("Creating a symmetric key")
    enc = encryptor.Encryptor()

    mykey = enc.key_create()

    enc.key_write(mykey, "mykey.key")


if __name__ == "__main__":
    main()
