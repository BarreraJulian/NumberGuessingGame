import random

random_number = random.randint(1,10)
dealers_number = random_number
numer_of_guesses = 3
game_ended = False

while game_ended is False:
        players_number_input = input("Guess a number between 1-10: ")
        players_number = int(players_number_input)
        if players_number > 10 or players_number < 1:
            print("Please pick a number between 1-10!")
            continue
        if players_number != dealers_number:
            numer_of_guesses = numer_of_guesses - 1
            print("You got it wrong! You have", numer_of_guesses, "guesses left!")
            if numer_of_guesses == 0:
               play_again = input("You ran out of guesses! Do you want to play again?")
               if play_again == "Yes":
                    numer_of_guesses = 3
                    dealers_number = random.randint(1,10)
                    continue
               else:
                    print("Thanks for playing! Goodbye!")
                    break
            else:
                 continue
        elif players_number == dealers_number:
            print("You got it right!")
            play_again = input("Do you want to play again?")
            if play_again == "Yes":
                 numer_of_guesses = 3
                 dealers_number = random.randint(1,10)
                 continue
            else:
                 print("Thanks for playing! Goodbye!")
                 game_ended = True
                 break
