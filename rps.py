#!/opt/bb/bin/python3.6

valid_choices = ["Rock","Paper","Scissors"]
print("Welcome to the Rock, Paper, Scissors game")

global player1_score, player2_score, winning_score 
player1 = "Athena"
player2 = "Doyoun"
player1_score = 0
player2_score = 0
winning_score = 3

def make_choice(player)
   choice = input(player + "Please Enter your choice: ")
   while choice not in valid_choices:
       print("incorrect entry")
       choice = input(player + "Enter your choice again: ")
   return choice

def check_winner(player1_score, player2_score):
    while player1_score < 3 and player2_score < 3:
        player1_choice = make_choice(player1)
        player2_choice = make_choice(player2)

        if player1_choice == player2_choice:
            print("DRAW!")

        elif ((player1_choice == "Paper" and player2_choice == "Rock")
        or
        (player1_choice == "Rock" and player2_choice == "Scissors")
        or
        (player1_choice == "Scissors" and player2_choice == "Paper")):
            print(player1, "Wins!")
            player1_score += 1
            print(player1, "is now", winning_score - player1_score, "point away from winning!") 

        else:
            print(player2, "Wins!")
            player2_score += 1
            print(player2, "is now", winning_score - player2_score, "point away from winning!")
            
        if player1_score == winning_score:
            print(player1, "wins with total score:", player1_score)

        elif player2_score == winning_score:
            print(player2, "wins with total score:", player2_score)

check_winner(player1_score, player2_score)
