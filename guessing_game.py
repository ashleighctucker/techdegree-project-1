#Hi friends, I am aiming for an Exceeds Expectations grade, please reject the project if all requirements aren't met <3

import random

#print welcome/header
print("""
---------------------------------------
---------------------------------------
->WELCOME TO THE NUMBER GUESSING GAME<-
---------------------------------------
---------------------------------------
""")

#create empty list to store high scores
high_score = []


def start_game():

    #random num chosen between 1-10, updated each time game is played
    target_num = random.randint(1, 10)

    #create empty list to store the valid "attempts"
    guess_num = []

    while True:

        try:
            #prompt user continuously to choose a num until they get it right
            #raise ValueErrors for anything outside of the range
            guess = int(input("Pick a number between 1 and 10:  "))
            if guess > 10:
                raise ValueError()
            elif guess < 1:
                raise ValueError()
        #report error and prompt to try again, error should happen for anything != 1-10
        except ValueError:
            print("That is not a valid input. Try again.")
        #if attempt is valid (1-10), add it to the attempt list
        else:
            guess_num.append(guess)
            #print "got it" when they guess correctly, print the number of tries it took
            if guess_num[-1] == target_num:
                print("You got it! It took you {} tries.".format(len(guess_num)))
                #add the number of tries to the high score list
                high_score.append(len(guess_num))
                break
            #if guess > target number, print "its lower"
            elif guess_num[-1] > target_num:
                print("It's lower!")
                continue
            #if guess < target number, print "its higher"
            elif guess_num[-1] < target_num:
                print("It's higher!")
                continue


# Kick off the program by calling the start_game function.
start_game()

#allow the player to play again
while True:

    #prompt player to play again
    play_again = input("Would you like to play again? Y/N  ")

    #if player want to play again, print current high score and start game again
    if play_again.lower() == 'y':
        print("The current high score is {}!".format(min(high_score)))
        start_game()
        continue
    #if player says no (or anything other than y), thank them for playing and print high score
    else:
        print("Thanks for playing. Your high score was {}.".format(min(high_score)))
        break
