#This program is to generate swiss pools for a TFT tournament, where 8 players play eachother at a time

import math
import openpyxl

class Player:
    def __init__(self, name, rank, points):
        """Creates an instance of the Player class. The name is taken from a .xlsx file, the rank is generated
           by the order of the name in the spreadsheet, and the points are initially set to 0."""
        self.name = name #(String) The name (or tag) of the player
        self.rank = rank #(Int) The pre-determined seeding of each player. The higher 
                         #the number, the higher ranked they are
        self.points = points #(Int) The amount of points that the player has total from all completed rounds
    def __str__(self):
        return self.name

def generatePlayers():
    """Takes the names from the .xlsx file, converts them into players (the rank of each player is determined by
       the order they are in on the spreadsheet) where the first name is the highest rank and the last name
       is the bottom rank."""
    players = [] #Stores all of the players
    #Credits to https://jdgwf.com/posts/2020-03-30-accessing-data-in-xlsx-spreadsheets-in-python/ for
    #teaching me how to use openpyxl, some lines are either copied verbatum or slightly altered
    WorkbookRead = openpyxl.load_workbook(filename = "INSERT FILE NAME AND LOCATION HERE")
    worksheet1 = WorkbookRead[WorkbookRead.sheetnames[0]]
    counter = 1
    while(worksheet1["A" + str(counter)].value is not None):
        players.append(Player(str(worksheet1["A" + str(counter)].value), counter, 0))
        counter += 1
    WorkbookRead.close()
    return players

def generateLobbies():
    """Creates the different lobbies that players are divided into. It does so using a snake draft system
       (i.e. if there are three lobbies, the third lobby has both the third and fourth highest rated players)"""
    playerCounter = 0
    lobbyCounter = 0
    end = False
    while playerCounter < len(players) - numberOfPlayers % 8:
        if len(games[lobbyCounter]) == 8:
            end = True
        games[lobbyCounter].append(players[playerCounter])
        if lobbyCounter == len(games) - 1:
            if len(games[lobbyCounter]) < 8:
                playerCounter += 1
                games[lobbyCounter].append(players[playerCounter])
            lobbyCounter -= 1
        elif lobbyCounter == 0:
            if len(games[lobbyCounter]) < 8 and playerCounter != 0:
                playerCounter += 1
                games[lobbyCounter].append(players[playerCounter])
            lobbyCounter += 1
        elif len(games[lobbyCounter]) <= len(games[lobbyCounter + 1]):
            lobbyCounter -= 1
        else:
            lobbyCounter += 1
        playerCounter += 1

def distributePoints():
    """Distributes points based on the placing of each player in their lobby."""
    pointSpread = [8, 7, 6, 5, 4, 3, 2, 1] #Change these values in order to adjust how many points a player
                                           #receives for their placing. The first value is how many points
                                           #are received for first place, and the lasst value is how many 
                                           #points are received for eighth place.
    placesPossible = [1, 2, 3, 4, 5, 6, 7, 8]
    valid = False
    toRemove = -1
    for i in range(len(games)):
        print("\nRound " + str(currentRound))
        print("\nLobby " + str(games.index(games[i]) + 1))
        placesPossible = [1, 2, 3, 4, 5, 6, 7, 8]
        for j in range(len(games[i])):
            valid = False
            while valid == False:
                playerTotal = int(input("\nWhat place did " + games[i][j].name + " get? "))
                valid = False
                for k in placesPossible:
                    if playerTotal == k:
                        valid = True
                        toRemove = k
                if valid:
                    placesPossible.remove(toRemove)
                    games[i][j].points += pointSpread[playerTotal - 1]
                else:
                    print("You have either distributed that place or it is impossible, try again")
    for i in games:
        i.clear()
    players.sort(key = lambda sort: sort.points, reverse = True)

def printLobbies():
    """Prints the different lobbies and who is in them for the current round."""
    print("\nRound " + str(currentRound))
    for i in games:
        i.sort(key = lambda sort: sort.points, reverse = True)
        print("\nLobby " + str(games.index(i) + 1) + "\n")
        for j in i:
            print(j)

def printStandings():
    """Prints the current standings of all players based on their point total"""
    print()
    players.sort(key = lambda sort: sort.points, reverse = True)
    for i in players:
        print(str(i) + ": " + str(i.points) + " points")

def menu():
    """Allows the user to choose what they would like to do. This is the core of the program, and just about
       everything else goes through this function."""
    print("\nIt is currently Round " + str(currentRound))
    print("\nWhat would you like to do? (type the number of the corresponding option)")
    print("\n1. Look at the lobbies for this round")
    print("2. Look at the current standings")
    print("3. Distribute the points for this round")
    decision = input("Decision: ")
    if(decision == "1"):
        printLobbies()
        menu()
    elif(decision == "2"):
        printStandings()
        menu()
    elif(decision == "3"):
        distributePoints()
    else:
        print("That is not a valid decision")
        menu()

players = generatePlayers() #(1D Array) Stores all of the players
numberOfPlayers = len(players) #The amount of players in the .xlsx file
numberOfLobbies = (int)(numberOfPlayers / 8) #The amount of lobbies playing concurrently
rounds = round(math.log(len(players), 2)) #The amount of rounds played
currentRound = 1
games = [] #(Multiple Dimension Array) Stores all of the players after they've been sorted into lobbies

for i in range(numberOfLobbies):
    games.append(list())
generateLobbies()
while currentRound < rounds + 1:
    menu()
    generateLobbies()
    currentRound += 1
printStandings()