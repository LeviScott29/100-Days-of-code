print("welcome to the silent auction")
more_players= "yes"
players = {}
highest=0
winner= ""
    
while more_players=="yes":
    name = input("what is your name?: ")
    bid = float(input("what is your bid? "))
    more_players = input("are there more players? yes or no: ")
    players[name]= bid

for bidder in players:
    bid = players[bidder]
    if bid > highest:
        highest= bid
        winner= bidder
print(players)
print( "the highest bid is: ", winner, "with", highest )

