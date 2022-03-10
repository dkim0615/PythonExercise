#!/opt/bb/bin/python3.6

#palindrome check use variable[0:] start from finish 
#variable[::-1] from the end to start in reverse order
#are these the same? 

while True:
    user_input = input("Enter a random word: ")

    if len(user_input) == 0:
        print("Please enter a valid word")

    else:
        if user_input[0:].lower() == user_input[::-1].lower():
            print("\033[0;32m\033[01m\033[04m{} is a palindrome\033[0;0m".format(user_input))

        else:
            print("\033[91m\033[04m{} is NOT a palindrome\033[0;0m".format(user_input))

        try_again = input("Press enter if you want to continue or N to exit ")
        if try_again.upper() == "N":
            break
    
input("Press Enter now to quit")
