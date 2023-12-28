print( " Welcome to Treasure Island \n your goal is the find the treasure")
while True:
    first_choice= input (" you are at a crossroads which way do you want to go? left or right?: ")
 
    if first_choice == "left":
        print("you go down the left path")
        break
    
    elif first_choice == "right":
        print("you go down the right path")
        break
    
    else: print("you can only go left or right")

if first_choice == "left":
    print("you come to a lake do you want to swim across or do you wait for the boat?")
    
    while True:
        choice_2a= input("choose wait or swim: ")
        if choice_2a== "wait":
            print("you wait for the boat and it takes you to the other side")
            print("you come to a chest sitting on a pedastal that was bars around it \n " " \n you see two levers in from of the pedastal \n " " \n  which one do you pull?")
            while True:
                final_choice = input("left or right?: ")
                if final_choice == "left":
                    print("you pull the left lever and a trap door opens up, you fall on to a pit of spikes and die")
                    break
                elif final_choice == "right":
                    print("you pull the right lever and the bars around the pedastal drop \nyou have found the treasure and won congratulations!")
                    break
                
                else: print("you can only choose left and right")
            break
        
        elif choice_2a== "swim":
            print("you try to swim across but get eaten by an alligator halfway across")
            break
        
        else: print("you can only choose wait or swim")
        
elif first_choice== "right":
    print("you come to an eerie forest do you walk through cautiously or careless?")

    while True:
        choice_2b = input(" cautious or careless?: ")
        if choice_2b== "careless":
            print("you carelessy walk through the forest and it scares a bear that kills you")
            break
        
        elif choice_2b == "cautious":
            print("you cautiously walk through the forest and make it to the other side safely")
            print("you come to a chest sitting on a pedastal that was bars around it \n " " \n you see two levers in from of the pedastal \n " " \n  which one do you pull?")
            while True:
                final_choice = input("left or right?: ")
                if final_choice == "left":
                    print("you pull the left lever and a trap door opens up, you fall on to a pit of spikes and die")
                    break
                elif final_choice == "right":
                    print("you pull the right lever and the bars around the pedastal drop \nyou have found the treasure and won congratulations!")
                    break
                else: print("you can only choose left and right")
            break
        
        else: print("you can only choose cautious or careless")
