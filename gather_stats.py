import generator
import multiple_generator

pw_list = []

def main():
    """
    I want to be able to:
    1. NUMBER: Be given the number of times an input char appears in all passwords (n)
    2. CHARACTERS: See all chars with input num
    3. PERCENT: See the percentage of given char (##.## %)
    4. PRINT: Neatly print all characters & their values ("x" has been used n times)
    5. Return a list of the values ->
    GENERAL STATS: AVERAGE, MEDIAN, STANDARD DEVIATION of values
    6. Find avg, median, st dev of values
    """
    print('Welcome to the Password Stats Collector!\n')
    while True:
        selection = input("What would you like to do: Generate (P)asswords, get (H)elp, or (Q)uit? ").lower()
        if selection == 'q':
            input("Press enter to quit. ")
            exit(1)
        elif selection == 'h':
            print('')
            print_help()
        elif selection == "p":
            list_of_pws = gen_pws(pw_list)
            times_chars_used = populate_dict(list_of_pws)
            stats_prompt(times_chars_used)
            print('finale')
        else:
            print("Please type a valid command.")


def print_help():
    print('Instructions:\n'
          '1. Type "p" into the menu to generate your passwords.\n'
          '2. Follow the instructions to generate your passwords.\n'
          '3. After generating your passwords, type "y" to see the stats, "n" to quit, or "i" for information.\n'
          '4. Read the information or type a number to view the statistic.\n')


def stats_prompt(dict_chars):
    while True:
        yesno = input('Would you like to see statistics about your passwords? (Y)es, (N)o, or (I)nformation: ').lower()
        if yesno == 'n':
            input('Press enter to quit. ')
            exit(1)
        elif yesno == 'y':
            stats_menu(dict_chars)
            break
        elif yesno == 'i':
            get_info()
        else:
            print('Please type a valid command.')


def get_info():
    print("\nHere is the info for each stat:")
    print('1. Number: Gives the number of times a chosen character has appeared across all generated passwords.\n'
          '2. Characters: See all characters with a chosen number of appearances.\n'
          '3. Percent: See the percentage of times a character has appeared.\n'
          '4. List All: Neatly print all characters & their values ("x" has been used n times).\n'
          '5. General Stats: Finds the median, mean/average, and standard deviation of character frequency.\n')


def stats_menu(dict_of_chars):
    print("Select a stat to display:")
    while True:
        selection = input('1. Number\n'
                          '2. Characters\n'
                          '3. Percent\n'
                          '4. List All\n'
                          '5. General Stats\n')
        if selection == '1':
            number1(dict_of_chars)
        elif selection == '2':
            number2(dict_of_chars)
        elif selection == '3':
            print('Not yet implemented')
        elif selection == '4':
            print('Not yet implemented')
        elif selection == '5':
            print('Not yet implemented')
        else:
            print("Please type a valid number. ")


def gen_pws(my_list):
    # Get variables
    length = generator.get_length()
    runs = multiple_generator.get_run_num()
    usable_chars = generator.parse_chars()
    if runs == 1:
        print("Your password is:\n")
    else:
        print("Your passwords are:\n")

    # Run a loop n times to print nxm-length passwords
    for i in range(runs):
        password = generator.construct_pass(length, usable_chars)
        print(password)
        my_list.append(password)

    # Printing statements
    print('')
    print(my_list)

    return my_list                                          # Returns list of passwords


def populate_dict(my_list):
    my_dict = {}
    for pw in my_list:
        for char in pw:
            if char in my_dict.keys():
                my_dict[char] += 1
            else:
                my_dict[char] = 1

    print(my_dict)
    return my_dict


def number1(dict):
    """ Returns the number of times a single character has appeared in the generated passwords. """
    while True:
        char_in = input("Please type a character (-1 to quit): ")
        if char_in == '-1':
            input('Press Enter to quit. ')
            exit(1)

        elif len(char_in) != 1:
            print("Please type a single character.\n")

        else:
            if char_in not in dict.keys():
                char_freq = 0
            else:
                char_freq = char_freq_finder(dict, char_in)

            print('The character "{}" has been generated {} times.\n'.format(char_in, char_freq))
            # if char_in not in dict.keys():
            #     print('The character "{}" has been generated 0 times.'.format(char_in))
            # else:
            #     print('The character "{}" has been generated {} times.'.format(char_in, dict[char_in]) )


def char_freq_finder(diction, charac):
    """ Return the (value) number of times a character (key) has been chosen. """
    return diction[charac]


def number2(dict):
    """ Returns all chars with selected number of occurrences. """
    while True:
        num_in = input('Please type a number (-1 to quit): ')
        try:
            num_in = int(num_in)
            if num_in == -1:
                input('Press Enter to quit. ')
                exit(1)
            elif num_in <= 0:
                print('Please type a positive number.')
            else:
                num2_finder(dict, num_in)
        except ValueError:
            print('Please type a number.')


def num2_finder(dict, num_occr):
    """ Finds the data for number2 function, and prints chosen numbers. """
    list_of_chars = []
    for item in dict:
        if dict[item] == num_occr:
            list_of_chars.append(item)

    num_chars = len(list_of_chars)

    if num_occr == 1:
        # print('Characters that have been generated 1 time:')
        word_end = 'time'
    else:
        word_end = 'times'

    if num_chars == 0:
        print('There are no characters that have been generated {} {}.'.format(num_occr, word_end))
    else:
        print('Characters that have been generated {} {}:'.format(num_occr, word_end))

    for i in range(num_chars):
        if i == num_chars - 1:
            print(list_of_chars[i])
        else:
            print(list_of_chars[i], end = ', ')

    print('')



main()