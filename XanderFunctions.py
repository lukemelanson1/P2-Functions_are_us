#Xander Green
#List of functions to orchestrate a soccer game

def getName() :
    name = input("What is your name? ")
    print(f"Welcome {name} to the season. Your team will play a certain number of games and based on your wins/losses you will be qualified to be in the tournament. ")
    return name

def menuDisplay():
    while True:
        print("---Menu---")
        print("1. Display and pick teams")
        print("2. Play a game")
        print("Display final results")

        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice >= 1 and choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number 1-3.")

user_choice = menuDisplay()

if user_choice == 1 :
    chooseTeam()
elif user_choice == 2 :
    play_game(sHomeTeam, sAwayTeam)
elif user_choice == 3 :
    display_record(sHomeTeam, dctTeamWL, iTotalWinsHome, iTotalLossHome, iNumGames)