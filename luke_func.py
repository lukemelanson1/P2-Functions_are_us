# Author: LM
# Program Description: run step #3

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