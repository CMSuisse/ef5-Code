import qrcode

#It is much easier for the user to only type L instead of qrcode.constants.ERROR_CORRECT_L
ERROR_CORRECTION_LOT = {"L": qrcode.constants.ERROR_CORRECT_L,
                        "M": qrcode.constants.ERROR_CORRECT_M,
                        "Q": qrcode.constants.ERROR_CORRECT_Q,
                        "H": qrcode.constants.ERROR_CORRECT_H}

#Only used by the advanced generator
def generate_code(error_correction_level: str, data: str, box_size: int) -> qrcode.QRCode:
        qr_code = qrcode.QRCode(None, ERROR_CORRECTION_LOT[error_correction_level], box_size)
        qr_code.add_data(data)
        return qr_code

#Don't let the user type in something that isn't even a string
try: 
    data = input("Enter the content of the QR Code: ")
    assert(type(data) == str)

except AssertionError:
    print("Your input wasn't a string. Please try again with a valid input.")

else:
    generator_select = input("Press ENTER to use the  qrcode library generator. Input 'advanced' to use the advanced generator: ")
    #Empty string
    if len(generator_select) == 0:
        img = qrcode.make(data)
        img.save("qrcode-v1.png")
    
    if generator_select == "advanced":
        error_correction_level = input("What error correction level should the generator use (L/M/Q/H): ")
        try:
            box_size = int(input("What size should one box of the code have: "))
        except ValueError:
            print("Your box size isn't an integer. Used the default of 4.")
            box_size = 4

        #User inputed an invalid error correction level
        if not error_correction_level in ERROR_CORRECTION_LOT.keys():
            print("Yo, wtf, I said only use L, M, Q or H! Idiot!")
        else:
            #Make the code with all the advanced parameters
            code = generate_code(error_correction_level, data, box_size)
            code.make(fit=True)
            img = code.make_image()
            img.save("qrcode-v1advanced.png")