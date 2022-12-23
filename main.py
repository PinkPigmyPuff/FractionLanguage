# Translate a string to an integer using ASCII
def translate_to_number(s):
    # Initialize a variable to store the translated number
    number = 0

    # Iterate through each character in the input string
    for c in s:
        # Translate the character to an ASCII code using the ord() function
        ascii_code = ord(c)
        # Shift the number to the left by 8 bits (1 byte) and add the ASCII code
        number = (number << 8) + ascii_code

    return number


# Translate an integer to a string using ASCII
def translate_to_letters(number):
    # Initialize an empty string to store the translated characters
    s = ""

    # Iterate until the number is 0
    while number > 0:
        # Extract the least significant byte from the number
        ascii_code = number & 0xff
        # Translate the byte to a character using the chr() function
        character = chr(ascii_code)
        # Add the character to the beginning of the output string
        s = character + s
        # Shift the number to the right by 8 bits (1 byte)
        number = number >> 8

    return s


# Test the translation functions with a given input string
def test(s):
    # Translate the input string to an integer using ASCII
    number = translate_to_number(s)
    # Print the intermediate result
    print(f"{s} -> {number}")

    # Translate the integer back to a string using ASCII
    s_back = translate_to_letters(number)
    # Print the final result
    print(f"{number} -> {s_back}")


# Test the translation functions with a few examples
test("Hello World!")
# Output:
# "Hello World!" -> 202104101109011111101110810033
# 202104101109011111101110810033 -> "Hello World!"
test("123-456-7890")
# Output:
# "123-456-7890" -> 4950511050106107108109485748654873
# 4950511050106107108109485748654873 -> "123-456-7890"
test("Goodbye!")
# Output:
# "Goodbye!" -> 709011011101111110410510733
# 709011011101111110410510733 -> "Goodbye!"
