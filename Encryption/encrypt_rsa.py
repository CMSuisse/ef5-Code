def encrypt_with_rsa():
    encrypted_msg = []

    for character in MSG:
        int_representation = ord(character)
        interim = int_representation ** OTHER_E
        encrypted_msg.append(interim % OTHER_PRODUCT)
    
    return encrypted_msg

print("-----------------INPUT-----------------")
OTHER_PRODUCT = int(input("Enter the n-number of the key with which you want to encrypt: "))
OTHER_E = int(input("Enter the e-number of the key with which you want to encrypt: "))
MSG = input("ASCII-Message to encrypt: ")

print("-----------------OUTPUT-----------------")
print(encrypt_with_rsa())