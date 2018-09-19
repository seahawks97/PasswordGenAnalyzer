# PasswordGenAnalyzer
### How to Use
The only file you have to download is *generator.py*. To generate multiple passwords, download *generator.py* and *multiple_generator.py*. To generate statistics about the passwords, downlaod *generator.py*, *multiple_generator.py*, and *gather_stats.py*.
### How it Works
1. *Generator.py* gets the length of the password to generate, parses which characters to use, randomly selects the desired number of characters to use, and prints the password.
2. *Multiple_generator.py* does everything that *generator.py* does, but repeats the printing process to print out multiple passwords in succession.
3. *Gather_stats.py* is a more comprehensive program that has more menus and options. You can see instructions on how to use the program at the beginning by typing "i". Type "p" to generate passwords. This basically calls *multiple_generator.py*, and then puts each used character into a dictionary as the key with a counter as the value. It asks if you want to see statistics about the characters or need more information about what each option does. It prints the value of the stat that you wish to see, and then quits.
### The Stats
1. Number: Gives the number of times a chosen character has appeared across all generated passwords.
2. Characters: See all characters with a chosen number of appearances.
3. Percent: See the percentage of times a character has appeared.
4. List All: Neatly print all characters & their values ("x" has been used n times).
5. General Stats: Finds the median, mean/average, and standard deviation of character frequency.
6: Minimum: Finds the character(s) generated the least amount of times.
7. Maximum: Finds the character(s) generated the most amount of times.
