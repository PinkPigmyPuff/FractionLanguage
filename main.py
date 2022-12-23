def translate_to_numbers(s):
    # Create a dictionary that maps each letter to a corresponding two-digit code
    letter_to_number = {
        'a': '01', 'b': '02', 'c': '03',
        'd': '04', 'e': '05', 'f': '06',
        'g': '07', 'h': '08', 'i': '09',
        'j': '10', 'k': '11', 'l': '12',
        'm': '13', 'n': '14', 'o': '15',
        'p': '16', 'q': '17', 'r': '18', 's': '19',
        't': '20', 'u': '21', 'v': '22',
        'w': '23', 'x': '24', 'y': '25', 'z': '26'
    }

    # Initialize an empty string to store the translated numbers
    numbers = ""

    # Iterate through each character in the input string
    for c in s:
        # If the character is a letter, translate it to a number using the dictionary
        if c.isalpha():
            numbers += letter_to_number[c.lower()]
        # If the character is a digit, add it to the output string as is
        elif c.isdigit():
            numbers += c
        # If the character is a space, add '00' to the output string
        elif c == " ":
            numbers += "00"
        # If the character is not a letter, digit, or space, ignore it

    return numbers


def translate_to_letters(s):
    # Create a dictionary that maps each two-digit code to a corresponding letter
    number_to_letter = {
        '01': 'a', '02': 'b', '03': 'c',
        '04': 'd', '05': 'e', '06': 'f',
        '07': 'g', '08': 'h', '09': 'i',
        '10': 'j', '11': 'k', '12': 'l',
        '13': 'm', '14': 'n', '15': 'o',
        '16': 'p', '17': 'q', '18': 'r', '19': 's',
        '20': 't', '21': 'u', '22': 'v',
        '23': 'w', '24': 'x', '25': 'y', '26': 'z'
    }
    # Initialize an empty string to store the translated letters
    letters = ""

    # Split the input string into a list of two-digit codes
    codes = [s[i:i + 2] for i in range(0, len(s), 2)]

    # Iterate through each two-digit code
    for code in codes:
        # If the code is a space ('00'), add a space to the output string
        if code == "00":
            letters += " "
        # If the code is a valid two-digit code, translate it to a letter using the dictionary
        elif code in number_to_letter:
            letters += number_to_letter[code]
        # If the code is not a valid two-digit code, ignore it

    return letters


def test(testString):
    print('Initial string: ' + testString)
    numberTranslation = translate_to_numbers(testString)
    print('Number translation: ' + numberTranslation)
    backToLetters = translate_to_letters(numberTranslation)
    print('Back to letters: ' + backToLetters)


test("My name is 123, otherwise known as Theo the 4th.")
test("does git work??")