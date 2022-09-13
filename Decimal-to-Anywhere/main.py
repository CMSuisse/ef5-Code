HEX_REPLACEMENT = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

def convert_to_decimal(decimal_number):
    division_result = decimal_number
    output_array = []

    while division_result > 0:
        division_result, remaining = advanced_floordiv(division_result, 2)
        output_array.append(remaining)
    return output_array

def convert_to_hex(decimal_number):
    division_result = decimal_number
    output_array = []

    while division_result > 0:
        division_result, remaining = advanced_floordiv(division_result, 16)
        if remaining < 10:
            output_array.append(remaining)
        else:
            output_array.append(HEX_REPLACEMENT[str(remaining)])
    return output_array
    


def advanced_floordiv(input_number, denominator):
    output_number = input_number // denominator
    remaining = input_number % denominator
    return output_number, remaining

def display_output(output_array):
    output_array.reverse()
    for bit in output_array:
        print(bit, end=" ")
    print("\n") #Creature comfort


number_to_convert = int(input("What number should be converted? "))
binary_number = convert_to_decimal(number_to_convert)
hex_number = convert_to_hex(number_to_convert)
display_output(binary_number)
display_output(hex_number)