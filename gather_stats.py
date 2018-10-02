import generator
import multiple_generator


def main():
    """This is the Main Menu. Come here to get started and get help on how to use the program."""
    print('Welcome to the Password Stats Collector! Developed by Steven Tucker - https://github.com/seahawks97')
    while True:
        selection = input("What would you like to do: Generate (N)ew passwords, get (H)elp, or (Q)uit? ").lower()
        print('')

        if selection == 'q':
            input("Press Enter to quit. ")
            exit(1)

        elif selection == 'h':
            print_help()

        elif selection == "n":
            list_of_pws = gen_pws()
            times_chars_used = populate_dict(list_of_pws)
            stats_menu(times_chars_used)

        else:
            print("Please type a valid command.")


def print_help():
    print('Instructions:\n'
          '1. Type "p" into the menu to generate your passwords or "q" to quit.\n'
          '2. Follow the instructions to generate your passwords.\n'
          '3. The generated passwords will be displayed on the screen.\n'
          '4. Type a number to view a statistic. Type "i" after the number to view information on what the statistic '
          'shows.\n')


def stats_menu(dict_of_chars):
    """
    This is the Stats Menu. Each number performs a specific function. Each number with an "i" typed after it will
    display useful information about the function (given the function exists).
    """
    stat_info = {'1': '1. Number: Gives the number of times a chosen character has appeared across all generated '
                      'passwords.',
                 '2': '2. Characters: See all characters with a chosen number of appearances.',
                 '3': '3. Percent: See the percentage of times a character has appeared.',
                 '4': '4. List All: Neatly print all characters & their values ("x" has been used n times).',
                 '5': '5. General Stats: Finds various statistics about frequency of character generation.',
                 '6': '6. Graph: Create a bar graph of frequency distribution.\n'
                      'How to read the graph: The bars at a decimal number are read as the lower number. '
                      'For example, if a bar from 2-3 has a height of 4, that means 4 characters have been '
                      'generated 2 times.'}

    while True:
        print('Type the number of a stat you want to display. Type "i" after '
              'the number to see information about the stat. (-1 to quit, -2 to return to Main Menu):')
        selection = input('1. Number\n'
                          '2. Characters\n'
                          '3. Percent\n'
                          '4. List All\n'
                          '5. General Stats\n'
                          '6. Graph\n').lower()

        if selection == '-1':
            input('Press Enter to quit. ')
            exit(1)

        elif selection == '-2':
            print('')
            break

        elif selection == '1':
            number1(dict_of_chars)

        elif selection == '2':
            number2(dict_of_chars)

        elif selection == '3':
            number3(dict_of_chars)

        elif selection == '4':
            number4(dict_of_chars)

        elif selection == '5':
            number5(dict_of_chars)

        elif selection == '6':
            number6(dict_of_chars)

        elif len(selection) == 2:
            sel_list = list(selection)
            #print(sel_list)                                    # Comment for testing
            sel_num = sel_list[0]

            if sel_list[1] == 'i' and sel_num in stat_info.keys():
                print(stat_info[sel_num])
            else:
                print('Please type a valid number.')

        else:
            print("Please type a valid number.")

        print('')


def gen_pws():
    # Get variables
    my_list = []
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
    #print(my_list)                                         # Comment for testing

    return my_list                                          # Returns list of passwords


def populate_dict(my_list):
    my_dict = {}
    for pw in my_list:
        for char in pw:
            if char in my_dict.keys():
                my_dict[char] += 1
            else:
                my_dict[char] = 1

    #print(my_dict)                                         # Comment for testing
    return my_dict


def number1(dict):
    """ Returns the number of times a single character has appeared in the generated passwords. """
    while True:
        char_in = input("Please type a character (-1 to quit, -2 to return to Stats Menu): ")
        if char_in == '-1':
            input('Press Enter to quit. ')
            exit(1)

        elif char_in == '-2':
            break

        elif len(char_in) != 1:
            print("Please type a single character.\n")

        else:
            if char_in not in dict.keys():
                char_freq = 0
            else:
                char_freq = char_freq_finder(dict, char_in)

            print('The character "{}" has been generated {} times.\n'.format(char_in, char_freq))


def char_freq_finder(diction, charac):
    """ Return the (value) number of times a character (key) has been chosen.
     Seperate function so it can be reused. """
    return diction[charac]


def number2(dict):
    """ Returns all chars with selected number of occurrences. """
    while True:
        num_in = input('Please type a number (-1 to quit, -2 to return to Stats Menu): ')
        try:
            num_in = int(num_in)
            if num_in == -1:
                input('Press Enter to quit. ')
                exit(1)

            elif num_in == -2:
                break

            elif num_in <= 0:
                print('Please type a positive number.\n')

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

    if num_chars == 1:
        hay = 'is'
        words = ''
        word2 = 'has'
    else:
        hay = 'are'
        words = 's'
        word2 = 'have'

    if num_occr == 1:
        word_end = 'time'
    else:
        word_end = 'times'

    if num_chars == 0:
        print('There are no characters that have been generated {} {}.'.format(num_occr, word_end))
    else:
        print('There {} {} character{} that {} been generated {} {}:'.format(hay, num_chars, words, word2, num_occr,
                                                                               word_end))

    for i in range(num_chars):
        if i == num_chars - 1:
            print(list_of_chars[i])
        else:
            print(list_of_chars[i], end = ', ')

    print('')


def find_num_chars(dict):
    """ Gets total number of characters generated. Returns an integer. """
    counter = 0
    for i in dict.values():
        counter += i
    return counter


def number3(dict):
    """ Returns the percentage of times a chosen character has been generated. """
    # Gets total number of characters generated
    denom = find_num_chars(dict)

    while True:
        char_in = input("Please type a character (-1 to quit, -2 to return to Stats Menu): ")
        if char_in == '-1':
            input('Press Enter to quit. ')
            exit(1)

        elif char_in == '-2':
            break

        elif len(char_in) != 1:
            print("Please type a single character.\n")

        else:
            if char_in not in dict.keys():
                numer = 0
            else:
                numer = char_freq_finder(dict, char_in)

            quotient = 100 * numer/denom
            quotient = '%.4f' % quotient

            print('The character "{}" has been generated {} of {} times, or {}% of the time.\n'.format(
                char_in, numer, denom, quotient))


def number4(dict):
    """ Print all the characters with the number of times they've been generated. """
    keys = list(dict.keys())
    vals = list(dict.values())

    for i in range(len(keys)):
        print('The character "{}" has been generated {} times.'.format(keys[i], vals[i]))

    num_chars = find_num_chars(dict)
    print('\nThere have been a total of {} characters generated.'.format(num_chars))


def number5(dict):
    """ Provide general statistics about the spread of numbers"""
    vals_list = list(dict.values())                     # list of values
    possible_chars = generator.parse_chars()            # string of all possible chars (from generator.py)
    tot_num_chars = len(possible_chars)                 # int of length of possible_chars
    num_gen_chars = find_num_chars(dict)                # int of length * num pws actually generated

    # Total
    print('Total of number of characters generated: {}'.format(num_gen_chars))
    print('Total unique characters generated (of {}): {}\n'.format(tot_num_chars, len(vals_list)))

    # Mean
    exp_mean = num_gen_chars / tot_num_chars
    print('Expected average frequency of generation for each possible character: %.4f times' % exp_mean)

    mean_out = mean(dict)
    print('Actual average frequency of generation for each character generated: %.4f times' % mean_out)

    # Variance & Standard Deviation
    variance_out = variance(dict, mean_out)
    print('Variance: %.4f' % variance_out)

    std_dev = variance_out ** 0.5
    print('Standard Deviation: %.4f\n' % std_dev)

    # Minimum
    min_gen = find_small_num(vals_list)
    print('Lowest Frequency: {}'.format(min_gen))

    min_chars = find_chars_w_num(dict, min_gen)
    length1 = len(min_chars)
    if length1 > 1:
        specials1 = 's'
    else:
        specials1 = ''

    print('{} Character{} with lowest frequency of {}:'.format(length1, specials1, min_gen), end=' ')
    length = len(min_chars)
    for i in range(length):
        if i == length - 1:
            print('"' + min_chars[i] + '"')
        else:
            print('"' + min_chars[i], end='", ')

    # Maximum
    max_gen = find_large_num(vals_list)
    print('Highest Frequency: {}'.format(max_gen))

    max_chars = find_chars_w_num(dict, max_gen)
    length2 = len(max_chars)
    if length2 > 1:
        specials2 = 's'
    else:
        specials2 = ''

    print('{} Character{} with highest frequency of {}:'.format(length2, specials2, max_gen), end=' ')
    length = len(max_chars)
    for i in range(length):
        if i == length - 1:
            print('"' + max_chars[i] + '"')
        else:
            print('"' + max_chars[i], end='", ')


def mean(dictionary):
    """ Returns the mean number from a list of dictionary values"""
    counter = 0
    total = 0

    for i in dictionary.values():
        total += i
        counter += 1

    return total / counter


def variance(dictionary, xbar):
    """ Returns variance of list of dictionary values. Standard Deviation is the square root of the variance."""
    total = 0
    counter = 0

    for i in dictionary.values():
        total += ((i - xbar) ** 2)
        counter += 1

    return total / counter


def find_small_num(my_list):
    """ Finds & returns the lowest number of generations."""
    lowest = my_list[0]                       # number: 1st element is automatically the lowest
    for i in range(1, len(my_list)):
        if my_list[i] < lowest:
            lowest = my_list[i]

    return lowest


def find_large_num(my_list):
    """ Finds & returns the largest number of generations."""
    highest = my_list[0]                       # number: 1st element is automatically the highest
    for i in range(1, len(my_list)):
        if my_list[i] > highest:
            highest = my_list[i]

    return highest


def find_chars_w_num(dictionary, sn):
    """ Returns a list of characters whose frequency matches the specified number."""
    char_list = []
    for i in dictionary:
        if dictionary[i] == sn:
            char_list.append(i)

    return char_list


def module_exists():
    """ Checks to see if matplotlib, the module used for the graph, is installed on the current machine."""
    try:
        import matplotlib.pyplot
        return True
    except ModuleNotFoundError:
        print('Module for graph not found. Please exit and install the matplotlib module (https://matplotlib.org/) '
              'to view the graph.')



def construct_graph(my_dict):
    """ Construct a histogram of the list of character generation frequencies. """
    import matplotlib.pyplot as plt                             # imports matplotlib

    my_list = list(my_dict.values())                            # creates list of values

    # Smallest Freq
    small = find_small_num(my_list)                             # smallest value
    min_chars_li = find_chars_w_num(my_dict, small)
    scl_length = len(min_chars_li)
    if scl_length > 1:
        specials_s = 's'
    else:
        specials_s = ''
    print('Smallest Frequency: {} character{} had a frequency of {}'.format(scl_length, specials_s, small))

    # Largest Freq
    large = find_large_num(my_list)                             # largest value
    large_chars_li = find_chars_w_num(my_dict, large)
    lcl_length = len(large_chars_li)
    if lcl_length > 1:
        specials_t = 's'
    else:
        specials_t = ''
    print('Largest Frequency: {} character{} had a frequency of {}'.format(lcl_length, specials_t, large))

    # Find number of bins
    range_n = large - small + 1                                 # range of values (difference b/n smallest and largest)
    print('Number of bins:', range_n)

    # Finds width of bins
    bin_width = 1

    # Construct bin intervals, must be a list
    bin_units = [small]
    x = 1
    while x <= range_n:
        bin_units.append(bin_units[x - 1] + bin_width)
        x += 1

    # print(bin_units)                                          # Comment out for testing

    his = plt.xlabel('Times a Character was Generated')
    his = plt.ylabel('Number of Characters')
    his = plt.title('Frequency of Number of Characters Generated')

    his = plt.hist(x=my_list, bins=[x for x in bin_units])

    plt.show()


def number6(my_dict):
    """ Shows a histogram of character generation frequencies. """
    it_exists = module_exists()
    if it_exists is True:
        construct_graph(my_dict)


main()

