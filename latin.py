#!/opt/bb/bin/python3.6

'''
This program takes in a random word as an input and check the first letter of the word. 

If the word begins with a consonant, it moves that consonant to the end, 
and then add "ay" to the end of the word. 

If the word begins with a vowel, it simply adds "way" to the end of the word. 
'''

# Create a list of vowels [a, o, i, u, e]
# Take in a word as an input
# Check if the index[0] of the input belongs in vowels list    
# If yes, add "way" to the end of the word and print out this word
# If no, move the index[0] of the input to index[-1] and assign this to a new variable
# And then, add "ay" to this new variable
# Print out the new variable

vowels_list = ["a", "e", "i", "o", "u"]

while True:
    random_word = input("Please enter a random word: ")
    random_word = random_word.lower()

    if random_word[0] in vowels_list:
        random_word_altered = random_word + "ay"
        random_word_altered.upper()
        print("\033[0;32m\033[01m\033[04m" + random_word_altered + "\033[0;0m")

    else:
        random_word_consonant = random_word[0]
        new_word = random_word[1:] + random_word_consonant + "ay"
        print("\033[0;32m\033[01m\033[04m" + new_word + "\033[0;0m")

    try_again = input("Press Enter to play again or n to quit ")
    if try_again.lower() == "n":
        break

input("Press Enter now to quit.")

