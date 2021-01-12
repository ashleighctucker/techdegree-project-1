import random

print("""
---------------------------------------
---------------------------------------
->WELCOME TO THE NUMBER GUESSING GAME<-
---------------------------------------
---------------------------------------
""")

high_score = []

def start_game():
    target_num = random.randint(1, 10)
    guess_num = []

    while True:

        try:
            guess = int(input("Pick a number between 1 and 10:  "))
            if guess > 10:
                raise ValueError()
            elif guess < 1:
                raise ValueError()
        except ValueError:
            print("That is not a valid input. Try again.")
        else:
            guess_num.append(guess)

            if guess_num[-1] == target_num:
                print("You got it! It took you {} tries.".format(len(guess_num)))
                high_score.append(len(guess_num))
                break
            elif guess_num[-1] > target_num:
                print("It's lower!")
                continue
            elif guess_num[-1] < target_num:
                print("It's higher!")
                continue


# Kick off the program by calling the start_game function.
start_game()

while True:
    play_again = input("Would you like to play again? Y/N  ")

    if play_again.lower() == 'y':
        print("The current high score is {}!".format(min(high_score)))
        start_game()
        continue
#todo add highscore
    else:
        print("Thanks for playing. Your high score was {}.".format(min(high_score)))
        break
