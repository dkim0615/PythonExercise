#!/opt/bb/bin/python3.6

from collections import counter, sys 
# import sys

def load(file_name="dictionary_file.txt"):
        try:
                with open(file_name,"r") as in_file:
                        loaded_text = []
                        for x in in_file.read().strip().split('\n'):
                                loaded_text.append(x.lower())
                        return loaded_text

        except:
                pass

word_list = load("dictionary_file.txt")

anagram_list = []

user_word = input("Enter any word/name you'd like to find anagrams of: ")
user_word = user_word.lower()
user_word_sorted = sorted(user_word)
# print(user_word_sorted)

for word in word_list:
    word = word.lower()
    if word != user_word:
        if sorted(word) == user_word_sorted:
            anagram_list.append(word)
            
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")

else: 
    print("Anagrams are: ", *anagram_list, sep='\n')
