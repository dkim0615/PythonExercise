#!/opt/bb/bin/python3.6
""" test out counter for anagram """
from collections import Counter

def load(file_name="dictionary_file.txt"):
    try:
        with open(file_name, "r") as in_file:
            loaded_text = []
            for x in in_file.read().strip().split('\n'):
                loaded_text.append(x.lower())
            return loaded_text

    except:
        pass

word_list = load("dictionary_file.txt")

user_name = input("Enter your name: ")
set_limit = len(user_name)

anagram_collection = []
        
while len(anagram_collection) < set_limit:
    for word in word_list: 
        word = word.lower()
        if word != user_name: 
            if len(word) == len(user_name):
                if sorted(word) == sorted(user_name):
                    anagram_collection.append(word)
    print(anagram_collection, ": Here is the list of anagram words that match your name")


