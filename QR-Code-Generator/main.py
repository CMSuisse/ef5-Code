import qrcode

try: 
    data = input("Enter the content of the QR Code: ")
    assert(type(data) == str)

except AssertionError:
    print("Your input wasn't a string. Please try again with a valid input.")

else:
    img = qrcode.make(data)
    img.save("qrcode-v1.png")