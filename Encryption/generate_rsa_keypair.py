import math

def is_prime(candidate: int):
    for i in range(2, candidate//2):
        if candidate % i == 0:
            return False
    return True

def extended_euclidian(a: int, b: int):
    if a == 0:
        return 0, 1
    
    x1, y1 = extended_euclidian(b%a, a)
    x = y1 - (b//a) * x1
    y = x1

    return x, y

try:
    print("-----------------INPUT-----------------")
    # Gather user input for the prime factors
    prim_inputs = input("Enter your two prime factors, leave a space or comma between the two numbers: ")
    prims = prim_inputs.replace(",", " ").split()

    # Assert user input is valid
    PRIVATE_P, PRIVATE_Q = int(prims[0]), int(prims[1])
    assert(is_prime(PRIVATE_P) and is_prime(PRIVATE_Q))
    del(prims)

    # Do some calculation
    PUBLIC_PRODUCT = PRIVATE_P * PRIVATE_Q
    PRIVATE_PHI = (PRIVATE_P - 1) * (PRIVATE_Q - 1)
    print("Product of your prime numbers is: {}".format(PUBLIC_PRODUCT))

    #Repeat with the e-number
    valid_e_number = False
    while not valid_e_number:
        PUBLIC_E = int(input("Enter your e-number of choice here: "))
        if math.gcd(PUBLIC_E, PRIVATE_PHI) == 1 and PUBLIC_E > 0 and PUBLIC_E < PUBLIC_PRODUCT:
            valid_e_number = True
        else:
            print("Invalid e-number. Try again.")

except:
    print("The values you inputted aren't valid inputs")
    
else:
    d_candidate = extended_euclidian(PUBLIC_E, PRIVATE_PHI)[0]
    PRIVATE_D = d_candidate if d_candidate > 0 else d_candidate + PRIVATE_PHI

    print("-----------------OUTPUT-----------------")
    print("Public key: E = {} / N = {}".format(PUBLIC_E, PUBLIC_PRODUCT))
    print("Private key: D = {} / N = {} \n".format(PRIVATE_D, PUBLIC_PRODUCT))