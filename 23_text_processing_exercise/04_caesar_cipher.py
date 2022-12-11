def encrypt(text):
    encrypted_str = ""
    for character in text:
        encrypted_char = chr(ord(character) + 3)
        encrypted_str += encrypted_char
    return encrypted_str


unencrypted_text = input()
print(encrypt(unencrypted_text))
