import game_data
import random

def higher_or_lower():
    while True:
        person_A = random.choice(game_data.data)
        person_B = random.choice(game_data.data)
        score = 0
        while True:
            print("A. ",[person_A['name'], person_A['description'], person_A['country'],  person_A['follower_count']])
            print("vs")
            print("B. ",[person_B['name'], person_B['description'], person_B['country'], person_B['follower_count']])

            pick = input ("who do you think has more followers? (A or B): \n").lower()
            if pick == "a" and person_A["follower_count"]> person_B["follower_count"]:
                print("correct")
                print(person_A['name'], "has", person_A['follower_count'], "followers")
                print( person_B['name'], "has", person_B['follower_count'], "followers")
                score += 1
                print("score:", score)
                person_B = random.choice(game_data.data)
            elif pick == "b" and person_A["follower_count"]< person_B["follower_count"]:
                print("correct")
                print ( person_A['name'], "has", person_A['follower_count'], "followers")
                print ( person_B['name'], "has", person_B['follower_count'], "followers")
                score+=1
                print("score:", score)
                person_A= person_B
                person_B = random.choice(game_data.data)
            elif pick== "a" and person_A["follower_count"]< person_B["follower_count"]:
                print("incorrect \n game over")
                print("your score was:", score)
                break
            elif pick == "b" and person_A["follower_count"]> person_B["follower_count"]:
                print("incorrect \n game over")
                print("your score was:", score) 
                break
        play_again = input(" do you want to play again? (yes or no) \n")
        if play_again == "no":
            break
higher_or_lower()
    

