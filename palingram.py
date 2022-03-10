#!/opt/bb/bin/python3.6

import sys, time

start_time = time.time()
# palin_list = []
# for word in dictionary_loaded:
#         for secondary_word in dictionary_loaded:
#                 if word == secondary_word:
#                         continue
#                 else: 
#                         new_var = word + secondary_word

#                         if new_var == new_var[::-1]:
#                                 palin_list.append(word + " " + secondary_word)

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

def find_palingrams():
        pali_list = []
        for word in word_list:
                end = len(word)
                rev_word = word[::-1]

                if end > 1: 
                        for i in range(end):
                                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                                        pali_list.append((word, rev_word[end-i:]))
                                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                                        pali_list.append((rev_word[:end-i], word))
        return pali_list

palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)

print(palingrams_sorted)
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
        print("{} {}".format(first, second))

end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))
