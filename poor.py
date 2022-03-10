#!/opt/bb/bin/python3.6

from collections import defaultdict

poor_dict = defaultdict(int)

user_input = input("Enter a string for test: ")
user_input_no_space = user_input.replace(" ", "")

for key in user_input_no_space.lower():
    if key.isalpha() == False:
        pass
    else:
        poor_dict[key] += 1

poor_dict = sorted(poor_dict.items())
# print(poor_dict, "poor dict")

another_dict = defaultdict(list)
for key, val in poor_dict:
    for i in range(val):
        another_dict[key].append(key)

another_dict = sorted(another_dict.items())
print("text received = ", user_input)
# print(another_dict)
# print(type(another_dict))

for item in another_dict:
    # print(item)
    item_left = item[0]
    # print(item_left)
    item_right = item[1]
    # print(item_right)
    join_line = " ".join(item_right)
    # print(join_line)
    sentence = item_left + ":" + " " + join_line
    print(sentence.upper())

