def decrypt_with_rsa():
    decrypted_msg = ""

    for element in rcvd_msg_ints:
        interim = element ** OWN_D
        decrypted_msg = decrypted_msg + chr(interim % OWN_PRODUCT)

    return decrypted_msg

print("-----------------INPUT-----------------")
OWN_PRODUCT = int(input("Enter your own prime product: "))
OWN_D = int(input("Enter your own d-number: "))
RCVD_MSG = input("Enter the message you received here (separate with commas or white spaces): ")
RCVD_MSG = RCVD_MSG.replace(",", "").split(" ")

rcvd_msg_ints = []
for element in RCVD_MSG:
    rcvd_msg_ints.append(int(element))

print("-----------------OUTPUT-----------------")
print(rcvd_msg_ints, OWN_PRODUCT, OWN_D)
print(decrypt_with_rsa())