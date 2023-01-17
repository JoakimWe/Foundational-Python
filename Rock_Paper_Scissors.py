# Rock Paper Scissors

#1
print("_____________________________________________________________________________________________________")
import random
plays = ["rock", "paper", "scissors"]
usr_play = input("Enter your play: ").lower()

if usr_play != "rock" or usr_play != "paper" or usr_play != "scissors":
    print("Wrong input, check spelling. Choose one of: " + str(plays))
usr_play = input("Enter your play: ").lower()
computer_play = random.choice(plays)

if usr_play == "rock" and computer_play == "scissors":
    print("You win, " + "computer played: " + str(computer_play))
elif usr_play == "rock" and computer_play == "paper":
    print("You loose, " + "computer played: " + str(computer_play))
elif usr_play == "rock" and computer_play == "rock":
    print("Draw , pick again")


if usr_play == "paper" and computer_play == "scissors":
    print("You loose, " + "computer played: " + str(computer_play))
elif usr_play == "paper" and computer_play == "paper":
    print("Draw , pick again")
elif usr_play == "paper" and computer_play == "rock":
    print("You win, " + "computer played: " + str(computer_play))

if usr_play == "scissors" and computer_play == "scissors":
    print("Draw , pick again")
elif usr_play == "scissors" and computer_play == "paper":
    print("You win, " + "computer played: " + str(computer_play))
elif usr_play == "scissors" and computer_play == "rock":
    print("You loose, " + "computer played: " + str(computer_play))

print("______________________________________________________________________________________________________")
print("Here comes the same game done in a different way.")
##################
# 2 # using dictionaries

import random

rock_table = {"paper":"lose","scissors":"win","rock":"again"}
paper_table = {"paper":"again","scissors":"lose","rock":"win"}
scissors_table = {"paper":"win","scissors":"again","rock":"lose"}
game_logic = {"rock":rock_table,"paper":paper_table,"scissors":scissors_table}
choices = ["rock","paper","scissors"]

user_score = 0
computer_score = 0
round_number = 1
while True:
    usr_play = input("Enter your play: ").lower()
    print(f"Round {round_number}:")
    print(f"You played {usr_play}!")
    computer_play = random.choice(choices)
    if game_logic[usr_play][computer_play] == "lose":
        print(f"You loose computer played: {computer_play}" )
        computer_score += 1
    elif game_logic[usr_play][computer_play] == "win":
        print(f"You win computer played: {computer_play}")
        user_score += 1
    elif game_logic[usr_play][computer_play] == "again":
        print(f"Draw computer played: {computer_play}")
    print("----------------------------------------------------------------------------------")
    print(f"Score round {round_number}. \n Player: {user_score} \n Computer: {computer_score}")
    print("----------------------------------------------------------------------------------")
    play_again = input("Play again? Yes/No ").lower()
    print("----------------------------------------------------------------------------------")
    if play_again == "no":
        print(f"Final Score: \n Player: {user_score} \n Computer: {computer_score}")
        break


