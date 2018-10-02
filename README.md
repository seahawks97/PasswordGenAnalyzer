# PasswordGenAnalyzer
### How to Use
The primary program to be used is *gather_stats.py*. Because of this, the *main* functions have been commented out in the remaining files. If you choose to use *generator.py* or *multiple_generator.py* on their own, open the file in a text editor and remove the *#* in front of *main()* in the last line.
To generate one password, the only file you have to download is *generator.py*. To generate multiple passwords, download *generator.py* and *multiple_generator.py*. To generate statistics about the passwords, download *generator.py*, *multiple_generator.py*, and *gather_stats.py*. Run the last file mentioned in each sentence.
### How it Works
1. *Generator.py* gets the length of the password to generate, parses which characters to use, randomly selects the desired number of characters to use, and prints the password.
2. *Multiple_generator.py* does everything that *generator.py* does, but repeats the printing process to print out multiple passwords in succession.
3. *Gather_stats.py* is a more comprehensive program that has more menus and options. You can see instructions on how to use the program at the beginning by typing "i". Type "p" to generate passwords. This basically calls *multiple_generator.py*, and then puts each used character into a dictionary as the key with a counter as the value. It asks if you want to see statistics about the characters or need more information about what each option does. It prints the value of the stat that you wish to see, and then quits.
### The Stats
1. Number: Gives the number of times a chosen character has appeared across all generated passwords.
2. Characters: See all characters with a chosen number of appearances.
3. Percent: See the percentage of times a character has appeared.
4. List All: Neatly print all characters & their values ("x" has been used n times).
5. General Stats: Finds the total number of characters generated, number of unique characters generated, expected and actual averages, variance, standard deviation, highest and lowest frequency of characters generated, and which characters have been generated the maximum and minimum number of times.
6. Graph: MUST have [matplotlib](https://matplotlib.org/) library installed to use the Graph function. Creates a bar graph of number of characters that have been generated. How to read the graph: The bars at a decimal number are read as the lower number. For example, if a bar from 2-3 has a height of 4, that means 4 characters have been generated 2 times.
