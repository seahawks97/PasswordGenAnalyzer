import generator

def main():
    """ We want to run the generator multiple times, but without prompting for the length of the PW every time. """
    # Get variables
    length = generator.get_length()
    runs = get_run_num()
    usable_chars = generator.parse_chars()
    print("Your passwords are:\n")

    # Run a loop n times to print nxm-length passwords
    for i in range(runs):
        password = generator.construct_pass(length, usable_chars)
        print(password)

    # Exit
    print("\n")
    input("Press enter to exit.")


def get_run_num():
    while True:
        times_to_run = input("How many passwords to generate? (-1 to quit) ")
        try:
            times_to_run = int(times_to_run)
            if times_to_run == -1:
                exit(1)
            elif times_to_run <= 0:
                print("Please type a positive number.\n")
            else:
                return times_to_run
        except ValueError:
            print("Please type a number.\n")

