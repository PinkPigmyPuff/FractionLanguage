import nltk
import timeit
import sys
from tqdm import tqdm
import fractions
import decimal

# set the maximum amount of digits that can be converted to a string to be WAY higher
sys.set_int_max_str_digits(10000000)

# import the book 'emma' from nltk
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
# join the list of words together into a string
emmaText = text = " ".join(emma)

all_words = nltk.corpus.words.words()
ten_letter_words = [word for word in all_words if len(word) == 10]
print(ten_letter_words)


# Translate a string to an integer using ASCII
def translate_to_number(s):
    # Initialize a variable to store the translated number
    number = 0

    # Iterate through each character in the input string
    for c in tqdm(s):
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
    # print(f"{s} -> {str(number)}")

    # Translate the integer back to a string using ASCII
    s_back = translate_to_letters(number)
    # Print the final result
    # print(f"{number} -> {s_back}\n")


# estimate the time it will take to run 'test', given a smaller sample of text
def estimateTime(sample, full):
    time = timeit.timeit(lambda: test(sample), number=1)
    print(f"\nRunning time of sample: {time} seconds")

    sampleLen = len(sample)
    fullLen = len(full)
    timesLarger = fullLen/sampleLen
    print(f"\nThe length of the sample is: {sampleLen},"
          f" the length of the full text is: {fullLen},"
          f" and the ratio is: {timesLarger}")
    print(f"Estimated running time of full: {time * timesLarger}")


def getSample(original, sampleSize):
    return original[:sampleSize]

def decimal_to_fraction(decimal):
    # Convert the decimal to a fraction using the fractions module
    fraction = fractions.Fraction(decimal).limit_denominator()
    return fraction


def decimal_from_fraction(frac):
    return frac.numerator / decimal.Decimal(frac.denominator)


emmaNum = translate_to_number(getSample(emmaText, 500))
print(f"emmaNumber: {emmaNum}")
power_of_10 = len(str(emmaNum))
print(f"power of 10: {power_of_10}")
decimal.getcontext().prec = 100
decimalEmma = decimal.Decimal(emmaNum) / (decimal.Decimal(10) ** power_of_10)
print(f"decimal Emma: {decimalEmma}")
fraction = fractions.Fraction(str(decimalEmma)).limit_denominator()
print(f"fraction: {fraction}")

backToFraction = decimal_from_fraction(fraction)
print(f"back to fraction: {backToFraction}")

# Open the file in write mode
with open('emma.txt', 'w') as f:
    # Write the emmaNum variable to the file
    f.write(str(emmaNum))

