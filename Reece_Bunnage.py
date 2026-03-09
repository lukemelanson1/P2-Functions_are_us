#Reece Bunnage
#Function 4 and 5 for Soccer Season Simulator

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