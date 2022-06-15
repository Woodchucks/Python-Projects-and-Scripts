MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def if_exit():
    global exit
    if input("To EXIT press 1.\n") == "1":
        exit = True

def get_letter(val):
    for key, value in MORSE_CODE_DICT.items():
        if val == value:
            return key

exit = False
while exit == False:
    print("*** ====================================== ***")
    print("Welcome to the text to Morse Code Converter!")
    print("*** ====================================== ***\n")
    option = input("For Encrypting to Morse Code enter 1\n"
                   "For Decrypting to plain text enter 2\n")

    # Encrypting
    if option == "1":
        text = input("Please enter the text you want to convert to Morse Code:\n")
        text_upper = text.upper()
        translated_text = ""
        for letter in text_upper:
            if letter == " ":
                translated_text += " "
            else:
                translated_text += MORSE_CODE_DICT[letter] + " "

        print("*** ====================================== ***")
        print(f"Your Text: '{text}' in Morse Code:\n")
        print(translated_text)
        if_exit()

    # Decrypting
    elif option == "2":
        translated_text = ""
        text_in_morse = str(input("Please enter the text you want to convert to plain Text:\n"))
        morse_words = text_in_morse.strip().split("  ")
        for morse_word in morse_words:
            morse_letters = morse_word.split(" ")
            for morse_letter in morse_letters:
                if morse_letter == " ":
                    translated_text += " "
                else:
                    translated_text += str(get_letter(morse_letter))
            translated_text += " "

        print("*** ====================================== ***")
        print(f"Your Text: '{text_in_morse}' in Plain Text:\n")
        print(translated_text)
        if_exit()

    else:
        print("Wrong Entry. Try again\n")
