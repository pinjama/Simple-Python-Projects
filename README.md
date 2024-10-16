# Dice and Probabilities

**When throwing two fair dice the probabilites of possible sum values are:
2 or 12 = 2.8%
3 or 11 = 5.6%
4 or 10 = 8.3%
5 or 9 = 11.1%
6 or 8 = 13.9%
7 = 16.7%**

Program simulates throwing of two dice n times and computes the sum of the dice after every throw and adds the sum to list.
When the dice have been rolled n times, program draws a histogram of the frequencies of the sum.
You can observe that the results follow the calculated probability as the number n increases.

You need Matplotlib and Numpy for this code.

# Dictionary

**Simple dictionary application, which can save the dictionary in JSON format:**
The user can search words from the dictionary. If the word is found, it displays the translation.
if the word is not found, the program displays "Word not found. Please input a definition".
If user submits a definition, it adds a new word to this dictionary.

When the application is started it checks if the file containing the dictionary exists and will try to load the dictionary.
If loading fails, it starts with an inbuilt default dictionary, which contains just few words. The application saves the dictionary,
including newly added words, when the user exits the application. 
The program contains error handling.

# URL Fetcher and Parser

**Program asks the user for a valid URL to download. Then the program tries to load the contents of the URL into memory.
If contents look like a HTML file with utf-8 encoding, it tries to HTML parse it and check if the content has some dangerous words:**

The dangerous words are: "bomb", "kill", "murder", "terror", "terrorist", "terrorists" and "terrorism".
The program displays the amount of dangerous words found from the web page.
Finally the program asks the user for a path where to save the contents. This allows the user to save both binary files and text files to the local file system.
The program contains error handling.
