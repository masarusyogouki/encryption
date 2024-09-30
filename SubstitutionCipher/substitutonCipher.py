import random

def cryptographicRules():
    plain = "abcdefghijklmnopqrstuvwxyz"
    key = "".join(random.sample(plain, len(plain)))
    return plain, key

def encrypt( text, plain, key):
    result = ""

    for char in text:
        index = plain.find(char)
        result += key[index]
    
    return result

if __name__ == '__main__':
    plain, key = cryptographicRules()

    text = input( "暗号化したい文字列を入力してください: " )

    cipher_text = encrypt( text, plain, key)
    decode_text = encrypt( cipher_text, key, plain)

    print(text)
    print(cipher_text)
    print(decode_text)