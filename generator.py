import random

def main():
    length = get_length()
    chars = parse_chars()
    password = construct_pass(length, chars)
    print("Your password is: " + password)
    input("Press enter to exit.")


def get_length():
    print("Weak: 0-7; Moderate: 8-11; Strong: 12+")
    while True:
        num = input("How many characters long is your password? (-1 to quit) ")
        try:
            num = int(num)
            if num == -1:
                exit(1)
            elif num <= 0:
                print("Please type a positive number.\n")
            else:
                return num
        except ValueError:
            print("Please type a number.\n")


def parse_chars():
    lowercase = "abcdefghijkmnopqrstuvwxyz"                 # 'l' as in lambda removed
    uppercase = "ABCDEFGHJKLMNPQRSTUVWXYZ"                  # 'I' as in IGLOO, 'O' as in OPRAH removed
    numbers = "123456789"                                   # 'zero' removed
    special_characters = "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~"
    return lowercase + uppercase + numbers + special_characters


def construct_pass(length, chars):
    pw = ""
    for i in range(length):
        pw += random.choice(chars)
    return pw

