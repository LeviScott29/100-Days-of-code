import random

print("lets play rock paper scissors")
while True:
    user_input= int(input ("pick 0 for rock, 1 for paper, 2 for scissors or exit to quit: "))
    print ("you chose: ", user_input)


    computer_input= random.randint(0,2)
    computer_choice= computer_input

    print("computer chose: ", computer_choice)
    if computer_choice > user_input:
        if user_input == 0 and computer_choice == 2:
            print("you win")
        else: print("you lose")
                    
    elif user_input > computer_choice:
        if computer_choice== 0 and user_input == 2:
            print(" you lose")
        else: print("you win")
                    
    elif computer_choice == user_input:
                    print("you tied")
    else: print("invalid input")
                  
        

