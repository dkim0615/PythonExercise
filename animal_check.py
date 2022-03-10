#!/opt/bb/bin/python3.6
ANIMAL_LIST = ['cats', 'dogs', 'horses']

def list_o_matic(new_animal):
    if new_animal == "":
        print(ANIMAL_LIST.pop(), "popped from the list")
        print(ANIMAL_LIST)
        return

    elif new_animal not in ANIMAL_LIST:
        ANIMAL_LIST.append(new_animal)
        print("1 instance of ", new_animal, "appended to the list")
        print(ANIMAL_LIST)
        return
    
    else:
        ANIMAL_LIST.remove(new_animal)
        print("1 instance of ", new_animal,"removed from the list")
        print(ANIMAL_LIST)
        return

if len(ANIMAL_LIST) == 0:
    exit()

print("Look at all the animals: ", ANIMAL_LIST)

while True:
    animal_input = input("Please enter the name of an animal: ")
    if animal_input.isalpha() == True and animal_input != "quit":
        list_o_matic(animal_input)

    elif animal_input == "":
        list_o_matic(animal_input)
        
    else:
        print("goodbye")
        break
