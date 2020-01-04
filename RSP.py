import random

def game():
    play_again=True
    game_choice = ["paper", "scissors", "rock"]
    print("Wlecome Jacks Rock Paper SCissor")
    print("")
    winning_choices = {("paper", "rock"): "Paper covers rock.",
                        ("scissors", "paper"): "Scissors cut paper.",
                        ("rock", "scissors"): "Rock breaks scissors"}
    while play_again:
        player1 = input("Choose Rock, Paper, or Scissors:  ").lower()
        try:
            game_choice.index(player1)

        except ValueError:
            print("{} That is an invalid entry. Try again.".format(player1.capitalize()))
            continue
            print("")
        ai = random.choice(game_choice)
        matchup = (player1, ai)

        print("You chose {}, and the computer chose {}.".format(player1, ai))  
       
        if player1 == ai:
            print("It's a tie!")
        elif matchup in winning_choices:
            print(winning_choices[matchup])
            print("You win!")
        else:
            print(winning_choices[(ai, player1)])
            print("You lose.")

        if input("Would you like to play again (y/n)? ").lower() == "n":
            play_again = False
            print("See you next time!")
           
game()
