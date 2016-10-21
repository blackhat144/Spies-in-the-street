from random import randint as random
while True:
    numberOfPlayers=int(input("How many players?"))
    if numberOfPlayers<2: 
        print("Sorry, not enough players. Got any friends?")
        continue
    elif numberOfPlayers>6: #there's only 6 nationalities
        print("Sorry, too many players. Decide who's not cool enough to play and try again.")
        continue
    else:
        break
print()
print("Number of players: "+str(numberOfPlayers)+".")
listOfIDs=["French","German","Italian","American","Russian","Spanish"] #nationality possibilities
playerIDs=[]
bankAccounts=[] #list declaration
positions=[]
moveCards=[]
gameBoard=[] #fill this in with the indexes of the gameboard
for i in range(numberOfPlayers): #sets start-conditions for each player
    num=random(0,len(listOfIDs)-1) #random number that's a real index from the ID array/list
    playerIDs.append(listOfIDs[num]) #adds the random ID from ID list to the player (picked)  ID list
    listOfIDs.remove(listOfIDs[num]) #removes the picked ID from the list of IDs yet to be picked
    bankAccounts.append(30) #gives $30 to each player
    positions.append(0) #sets everyone's position at Start
    moveCards.append([])
for i in range(numberOfPlayers):
    e=i+1 #indexes player numbers at one for display purposes
    while True:
        print("Player "+str(e)+"\'s turn")
        ready=input("Type yes when ready, player "+str(e))
        if ready.lower()=="yes": #starts when player is ready
            print("it's working (so far)")
            if len(moveCards[i])>0: #if the player's movecard deck has movecards
                print("You have movecards")
                acceptableMoves=["roll","accuse","movecard"] #they can use a movecard
            else:
                print("You have no movecards") #if they don't have movecards, they can't use them
                acceptableMoves=["roll","accuse"]
            while True:
                decision=input("Type movecard to use a movecard if you have any, roll to roll the dice, and accuse to accuse another player").lower()
                if decision not in acceptableMoves:
                    print("Sorry, you can't do that")
                    continue
                else:
                    if decision=="movecard":
                        if len(moveCards[i])>1: #if they have multiple movecards:
                            while True:
                                cardPicked=input("You have the following movecards: "+moveCards[i]+". Which one do you want to use?")           
                                if cardPicked not in moveCards[i]:
                                    print("You don't have that movecard")
                                    continue
                                else:
                                    positions[i]+=cardPicked
                                    moveCards[i].remove(cardPicked)
                                    break
                        else: #if they only have one movecard
                            cardPicked=moveCards[i]
                            positions[i]+=cardPicked
                            print("You moved forward "+str(cardPicked)+" spaces")
                            moveCards[i].remove(cardPicked) """add the move numer to their position,
                            delete their moveCard array,
                            and add a new empty moveCard array at their index"""
                            moveCards[i].insert(i,[])
                    if decision=="roll":
                        playerRoll=input("What do you want to roll?") #TODO: Debugging feature replace with random from 1-6 for final release
                        print("You rolled a "+str(playerRoll))
                        positions[i]+=playerRoll 
        else:
            print("crap")
            continue #starts over if the player doesn't type yes

 
 
