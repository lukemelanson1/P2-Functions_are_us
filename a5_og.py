# Author: Luke Melanson
# Program Description: Enter soccer team and generate random scores for games played


# O. Import and def rand function
import random
def fRandomScore() : 
    iHomeScore = random.randrange(0,4)
    iAwayScore = random.randrange(0,4)
    return iHomeScore, iAwayScore

# 1. User Prompts
sHomeTeam = input("Enter the name of your home team: ").upper()
iGamesPlayed = int(input(f"Enter the number of games that {sHomeTeam} will play: "))

# 2. Lists and Dicts
lstWonAgainst = []
lstLostAgainst = []
dctGames = {
    "Won Against" : lstWonAgainst,
    "Lost Against" : lstLostAgainst
    }

# 3. Total Counters
iTotalWinsHome = 0
iTotalLossesHome = 0

# 4. Game Loop
for iCount in range(0,iGamesPlayed) : 
    sAwayTeam = input(f"\n Enter the name of the away team for game {iCount + 1}: ")
    iScore1,iScore2 = fRandomScore()
    while iScore1 == iScore2 :
        iScore1,iScore2 = fRandomScore()
    if iScore1 > iScore2 :
        iTotalWinsHome = iTotalWinsHome + 1
        lstWonAgainst.append(sAwayTeam)
    else :
        iTotalLossesHome = iTotalLossesHome + 1
        lstLostAgainst.append(sAwayTeam)
    print(f"{sHomeTeam}'s score: {iScore1} - {sAwayTeam}'s score: {iScore2}")

# 5. Prints
if iTotalWinsHome > 0 :
    print(f"\n Teams won against: ")
    for team in dctGames["Won Against"] :
        print(f"    {team}")
else :
    print("Home team had no wins. Womp Womp.")
if iTotalLossesHome > 0 :
    print(f"\n Teams lost against: ")
    for team in dctGames["Lost Against"] :
        print(f"    {team}")
else :
    print("Home team had no losses. Wooooo-hooo.")
print(f"\n Final season record: {iTotalWinsHome} - {iTotalLossesHome}")

# 6. Qualifications
fRecord = float( iTotalWinsHome / (iTotalWinsHome + iTotalLossesHome) )
if fRecord >= .75 :
    print(f"Qualified for the NCAA Soccer Tournament!")
elif fRecord >= .5 :
    print(f"You had a good season.")
else :
    print(f"Your teams needs to practice")