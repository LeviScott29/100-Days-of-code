print("Welcome to high low")

import random
def high_low():
    while True:
        already_guessed=[]
        guesses = 1
        while True:
            difficulty = input(" do you want to play easy or hard? \n")
            
            if difficulty == "easy":
                guesses = 10
                print ("you have 10 guesses")
                break
            elif difficulty =="hard":
                guesses = 5
                print(" you have 5 guesses")
                break
            else: print(" only 'easy' or 'hard' may be entered")
        number = random.randint(1, 100)
        while guesses !=0:

            while True:
                while True:
                    user_guess = input("Choose a number between 1 and 100: \n")
                    try:
                        int_guess = int(user_guess)
                        break
                    except ValueError:
                        print("You can only enter a number")

                for check in already_guessed:
                    if int_guess == check:
                        print("You already guessed that number")
                        break
                else:
                    already_guessed.append(int_guess)
                    break

   
            if int_guess < number:
                print(" too low")
                guesses -= 1
                print ("you have", guesses, "guesses left")
            elif int_guess > number:
                print("too high")
                guesses -=1
                print("you have", guesses, "guesses left")
            elif int_guess == number:
                print("you guessed correctly")
                print("you win")
                break
            if guesses== 0:
                break
        while True:
            play_again= input("do you want to play again? (yes or no): \n")
            if play_again != "no" and play_again != "yes":
                print(" you can only choose 'yes' or 'no'")
            elif play_again == "yes":
                break
            elif play_again == "no":
                break
        if play_again == "no":
            break
high_low()
            
        
