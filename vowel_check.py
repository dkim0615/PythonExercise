#!/opt/bb/bin/python3.6

def vowel_check(in_str):

    vowel = "aeiou"

    if len(in_str) < 2:
        print("please enter at least 2 letters")
        return False

    else:
        if in_str[:1] in vowel and in_str[-1:] in vowel:
            return True
        else:
            return False

while True:
    response = input("enter a word: ")
    if vowel_check(response) ==  True:
        print("success")

        break
