import hangman_words
import hangman_art
import random
print (hangman_art.logo)
print(" Welcome to Hangman")

word_list = hangman_words.word_list
lives= len(hangman_art.stages)
image = hangman_art.stages
play_again = "yes"
while play_again != "no":
    print("you have", lives, "lives")

    display= []
    chosen_word=random.choice(word_list)
    length = len(chosen_word)
    image_location= 6
    word_length = length

    for _ in range(length):
        display +="_"
    print(display)
    end_of_game = False
    while not end_of_game:
        guess= input("guess a letter or type quit to exit: \n").lower()
        if guess == "quit":
            break

        for position in range(length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(display)
        
        if guess not in display:
            print(image[image_location])
            image_location = image_location -1
            lives=lives-1
            print("you have ", lives, " lives left")
        if lives == 0:
            print("you lose")
            break

        if "_" not in display:
            end_of_game= True
            print("you win")
    play_again = input("do you want to play again? enter yes or no: ")
