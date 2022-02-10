from code_list import morse_code_list

code = []
reversed_morse_code = {value: key for key, value in morse_code_list.items()}
on = True


def encode_morse_code(phrase):
    for letter in phrase:
        try:
            code.append(morse_code_list[letter])
        except KeyError:
            pass
    return ','.join(code)


def decode_morse_code(phrase):
    decode = phrase.split(',')
    for letter in decode:
        try:
            code.append(reversed_morse_code[letter])
        except KeyError:
            pass
    return ''.join(code)


print('Welcome to morse coder')
while on:
    choice = input("Choose either to encode or decode by typing 'c' or 'd': ")
    if choice == 'c':
        text = input("Enter phrase to be turned into morse code:\n")
        print(encode_morse_code(text))
        code.clear()
    elif choice == 'd':
        text = input("Enter morse code to be turned into a phrase:\n")
        print(decode_morse_code(text))
        code.clear()
    elif choice == 'e':
        on = False
    elif choice != 'c' or choice != 'd':
        print("Invalid choice, try again")



