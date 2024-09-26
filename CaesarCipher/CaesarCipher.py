#　入力はすべて小文字のアルファベットのみとする

def encrypt(key, plain_text):
    cipher_text = ""

    for char in plain_text:
        ascii = ord(char)
        num = ascii - 97
        num = (num + key) % 26
        ascii = num + 97
        cipher_text += chr(ascii)

    return cipher_text

def decrypt(key, cipher_text):
    plain_text = ""

    for char in cipher_text:
        ascii = ord(char)
        num = ascii - 97
        num = (num - key) % 26
        ascii = num + 97
        plain_text += chr(ascii)

    return plain_text

def main():
    plain_text = input()
    key = int(input())
    cipher_text = encrypt(key, plain_text)
    print(cipher_text)
    print(decrypt(key, cipher_text))

if __name__ == "__main__":
    main()