

# X man Green stuf go here !



# Luke stuff

# FUNCTION 3:
# start the function
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

# running the func twice to choose two teams 
# important, the second time should elim sHomeTeam from lstTeams
sHomeTeam = chooseTeam()
sAwayTeam = chooseTeam(sHomeTeam)

# prints
print(f"\nHome team has selected: {sHomeTeam}")
print(f"Away team has selected: {sAwayTeam}\n")



# Reece stuff
import random

# FUNCTION 4: 
# Play the game receiving both team names. 
# Generate random scores without ties. Return W or L.

def play_game(sHomeTeam, sAwayTeam):
    #generates random scores for both teams
    iHomeScore = random.randrange(0, 4)
    iAwayScore = random.randrange(0, 4)

    # Re-roll if there is a tie
    while iHomeScore == iAwayScore:
        iHomeScore = random.randrange(0, 4)
        iAwayScore = random.randrange(0, 4)

    # Display the scores
    print(f"{sHomeTeam}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}")

    #Return W or L based on if they won or lost
    if iHomeScore > iAwayScore:
        return "W"
    else:
        return "L"


# FUNCTION 5:
# Display the final record for a team. 
# Receive the home team data and display information.

#final season score
def display_record(sHomeTeam, dctTeamWL, iTotalWinsHome, iTotalLossHome, iNumGames):
    # Display teams won against
    if iTotalWinsHome > 0:
        print("\nTeams won against:")
        for team in dctTeamWL["Won Against"]:
            print(f"  {team}")
    else:
        print("\nHome team had no wins. :(")

    # Display teams lost against
    if iTotalLossHome > 0:
        print("\nTeams lost against:")
        for team in dctTeamWL["Lost Against"]:
            print(f"  {team}")
    else:
        print("\nHome team had no losses!")

    # Final season record
    print(f"\nFinal season record: {iTotalWinsHome} - {iTotalLossHome}")

    # Win percentage and performance message
    fWinPercent = iTotalWinsHome / iNumGames

    # Display win percentage and message
    if fWinPercent >= 0.75:
        print("Qualified for the NCAA Soccer Tournament!")
    elif fWinPercent >= 0.5:
        print("You had a good season.")
    else:
        print("Your team needs to practice!")