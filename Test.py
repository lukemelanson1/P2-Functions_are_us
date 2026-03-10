#Xander Green, Luke Melanson, Reece Bunnage
# Soccer Season Simulator Group Project

import random

# Xander Green

# FUNCTION 1: Get player name and display welcome message
def getName():
    # ask for the player's name
    name = input("What is your name? ")
    # welcome message explaining the season rules
    print(f"Welcome {name} to the season. Your team will play a certain number of games and based on your wins/losses you will be qualified to be in the tournament. ")
    # return name so it can be used throughout the program
    return name

# FUNCTION 2: Display menu and return the user's choice
def menuDisplay():
    while True:
        # display the menu options
        print("---Menu---")
        print("1. Display and pick teams")
        print("2. Play a game")
        print("3. Display final results")
        try:
            # get the user's choice
            choice = int(input("Enter your choice (1-3): "))
            # check if choice is valid
            if choice >= 1 and choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number 1-3.")

# Luke Melanson

# FUNCTION 3: Display list of teams and return the chosen team
# excludeTeam parameter removes the home team from the list when picking an opponent
def chooseTeam(excludeTeam = None) :

    # list of teams available
    lstTeams = ["BYU","Utah","Stanford",
    "UVU","Tech","Arizona","Oklahoma"]

    # this part excludes the team entered in the
    # parameters above for the function
    if excludeTeam is not None : 
        lstTeams.remove(excludeTeam)

    # display the list of teams
    print("\nChoose a team: ")
    for iCount in range(len(lstTeams)) :
        print(f"{iCount+1}. {lstTeams[iCount]}")

    # selection and return
    iChoice = int(input("\nEnter the number of your choice: "))
    return lstTeams[iChoice - 1]

# Reece Bunnage

# FUNCTION 4: Play a game between two teams and return W or L
def play_game(sHomeTeam, sAwayTeam):
    # generate random scores for both teams
    iHomeScore = random.randrange(0, 4)
    iAwayScore = random.randrange(0, 4)

    # re-roll if there is a tie so there is always a winner
    while iHomeScore == iAwayScore:
        iHomeScore = random.randrange(0, 4)
        iAwayScore = random.randrange(0, 4)

    # display the final scores
    print(f"{sHomeTeam}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}")

    # return W if home team won, L if they lost
    if iHomeScore > iAwayScore:
        return "W"
    else:
        return "L"

# FUNCTION 5: Display the final season record for the home team
def display_record(sPlayerName, sHomeTeam, dctTeamWL, iTotalWinsHome, iTotalLossHome, iNumGames):
    # display header with player name and home team
    print(f"\n{sPlayerName}'s Final Season Record for {sHomeTeam}")

    # display teams the home team won against
    if iTotalWinsHome > 0:
        print("\nTeams won against:")
        for team in dctTeamWL["Won Against"]:
            print(f"  {team}")
    else:
        print("\nHome team had no wins. :(")

    # display teams the home team lost against
    if iTotalLossHome > 0:
        print("\nTeams lost against:")
        for team in dctTeamWL["Lost Against"]:
            print(f"  {team}")
    else:
        print("\nHome team had no losses!")

    # display the final win/loss record
    print(f"\nFinal season record: {iTotalWinsHome} - {iTotalLossHome}")

    # calculate win percentage and display performance message
    try:
        if iNumGames > 0:
            fWinPercent = iTotalWinsHome / iNumGames
            if fWinPercent >= 0.75:
                print("Qualified for the NCAA Soccer Tournament!")
            elif fWinPercent >= 0.5:
                print("You had a good season.")
            else:
                print("Your team needs to practice!")
    except ZeroDivisionError:
        print("No games played, so no performance to evaluate.")

    # closing message using player name
    print(f"\nThanks for playing, {sPlayerName}!")


# Main function to run the program and call our functions

# get the player's name and store it for use throughout the program
sPlayerName = getName()

# initialize opponent, win/loss tracking variables, and game counter
sHomeTeam = None
sAwayTeam = None
iTotalWinsHome = 0
iTotalLossHome = 0
dctTeamWL = {"Won Against": [], "Lost Against": []}
iNumGames = 0

# main loop - keeps running until the player chooses to see final results
while True:
    user_choice = menuDisplay()

    # option 1 - pick home team and opponent
    if user_choice == 1:
        # running the func twice to choose two teams
        # important, the second time should elim sHomeTeam from lstTeams
        sHomeTeam = chooseTeam()
        sAwayTeam = chooseTeam(sHomeTeam)
        # prints
        print(f"\nHome team has selected: {sHomeTeam}")
        print(f"Away team has selected: {sAwayTeam}\n")

    # option 2 - play a game and track the result
    elif user_choice == 2:
        # make sure an opponent has been chosen first
        if sAwayTeam is None:
            print("\nPlease choose an opponent first (option 1).")
            continue
        print(f"\n{sPlayerName}'s {sHomeTeam} vs {sAwayTeam}")
        result = play_game(sHomeTeam, sAwayTeam)
        iNumGames += 1
        # update wins or losses based on result
        if result == "W":
            iTotalWinsHome += 1
            dctTeamWL["Won Against"].append(sAwayTeam)
        else:
            iTotalLossHome += 1
            dctTeamWL["Lost Against"].append(sAwayTeam)

    # option 3 - display final results and end the program
    elif user_choice == 3:
        display_record(sPlayerName, sHomeTeam, dctTeamWL, iTotalWinsHome, iTotalLossHome, iNumGames)
        break