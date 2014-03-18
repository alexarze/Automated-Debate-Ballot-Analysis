import os
import sys

#Begin Variable Definitions
BALLOT = dict(
    ballot1 = {
        'win':0,
        'side':"",
        'first':"",
        'second':"",
        'third':"",
        'fourth':"",
        '1a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '1n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
            },

    ballot2 = {
        'win':0,
        'side':"",
        'first':"",
        'second':"",
        'third':"",
        'fourth':"",
        '1a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '1n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
            },
    
    ballot3 = {
        'win':0,
        'side':"",
        'first':"",
        'second':"",
        'third':"",
        'fourth':"",
        '1a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '1n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
            },
    
    ballot4 = {
        'win':0,
        'side':"",
        'first':"",
        'second':"",
        'third':"",
        'fourth':"",
        '1a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '1n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
            },
    
    ballot5 = {
        'win':0,
        'side':"",
        'first':"",
        'second':"",
        'third':"",
        'fourth':"",
        '1a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '1n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
            },
    
    ballot6 = {
        'win':0,
        'side':"",
        'first':"",
        'second':"",
        'third':"",
        'fourth':"",
        '1a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2a':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '1n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
        '2n':{'name':"", 'persuasiveness':0, 'organization':0, 'delivery':0, 'evidence':0, 'crossex':0, 'refutation':0, 'total':0},
            },
)

currentBallotList = list("ballot1")
currentBallot = "ballot1"
currentBallotInt = 1
prelimRounds = 0
prelimRoundsCountdown = 0
ynAnswer = 0
complete = 0
winCount = 0
winCountAff = 0
winCountNeg = 0
lossCount = 0
tempWinLoss = ""
#End Variable Definitions

#Begin Function Definitions
def checkNumber(arg):
    if arg.isdigit() == True:
        return int(arg)
    else:
        print("That's not a number!")
        return arg

def isComplete(arg):
    if arg.isdigit() == True:
        if int(arg) < 7 and int(arg) > 0:
            return 1
        else:
            print("\nInvalid speaker point number!\n")
            return 0
    else:
        print("\nThat's not a valid number!\n")
        return 0

def checkVote(arg):
    if arg.lower() == "affirmative" or arg.lower() == "aff" or arg.lower() == "a":
        return 1
    elif arg.lower() == "negative" or arg.lower() == "neg" or arg.lower() == "n":
        return 0
    else:
        print("That's not a valid answer!")

def checkYNAnswer(arg):
    if arg.lower() == "y":
        return 1
    elif arg.lower() == "q":
        os.system("clear")
        sys.exit("Force quit enacted!")
    else:
        return 0
    
def checkInt(arg):
    try: 
        int(arg)
        return True
    except ValueError:
        return False

#End Function Definitions
    
#Introductory Message
os.system("clear")
print("\n\nThis program is designed to automate ballot analysis. This will require initial input of ballot information, but will hopefully end with saved time and effort and minimal keystrokes and math.\nPLEASE REMEMBER THAT THIS IS MEANT PURELY FOR PRELIMINARY ROUNDS. ANY BUGS OCCURRING WITH OUTROUNDS WILL BE DISREGARDED.\n")
#Press any key to continue...
os.system('read -s -n 1 -p "Press any key to continue..."')

#Determine Number of Prelim Rounds
while ynAnswer == 0:
    os.system("clear")
    print("\n\nIn order to best calculate ballot analysis, we need to determine the number of preliminary rounds. Please enter that number below...\n")
    prelimRounds = checkNumber(raw_input("Number of Preliminary Rounds? "))
    if checkInt(prelimRounds) == True:
        if prelimRounds > 6 or prelimRounds < 1:
            print("No tournament offers that number of preliminary rounds!!\n\n")
            ynAnswer = 0
            os.system('read -s -n 1 -p "Press any key to continue..."')
        else:
            ynAnswer = checkYNAnswer(raw_input("Are you sure: Y or N? "))
    else:
        os.system('read -s -n 1 -p "\nPress any key to continue..."')

ynAnswer = 0
prelimRoundsCountdown = prelimRounds

while prelimRoundsCountdown > 0:
    
    #Ballot Message
    while ynAnswer == 0:
        os.system("clear")
        print("\n\nThe first step is to enter the ballots' information. Please enter the specified information below:\n\n")
        
        print("BALLOT " + currentBallot[6] + "\n")
        
        #1A Speaker Info
        print("1A SPEAKER\n")
        BALLOT[currentBallot]['1a']['name'] = raw_input("Name: ")
        ynAnswer = checkYNAnswer(raw_input("Are you sure: Y or N? "))
    ynAnswer = 0
    while complete == 0:
        BALLOT[currentBallot]['1a']['persuasiveness'] = raw_input("Persuasiveness: ")
        complete = isComplete(BALLOT[currentBallot]['1a']['persuasiveness'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1a']['organization'] = raw_input("Organization: ")
        complete = isComplete(BALLOT[currentBallot]['1a']['organization'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1a']['delivery'] = raw_input("Delivery: ")
        complete = isComplete(BALLOT[currentBallot]['1a']['delivery'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1a']['evidence'] = raw_input("Evidence: ")
        complete = isComplete(BALLOT[currentBallot]['1a']['evidence'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1a']['crossex'] = raw_input("Cross-Examination: ")
        complete = isComplete(BALLOT[currentBallot]['1a']['crossex'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1a']['refutation'] = raw_input("Refutation: ")
        complete = isComplete(BALLOT[currentBallot]['1a']['refutation'])
    complete = 0
    BALLOT[currentBallot]['1a']['total'] = int(BALLOT[currentBallot]['1a']['persuasiveness'])+int(BALLOT[currentBallot]['1a']['organization'])+int(BALLOT[currentBallot]['1a']['delivery'])+int(BALLOT[currentBallot]['1a']['evidence'])+int(BALLOT[currentBallot]['1a']['crossex'])+int(BALLOT[currentBallot]['1a']['refutation'])
    
    ynAnswer = 0
    
    #Ballot Message
    while ynAnswer == 0:
        os.system("clear")
        print("\n\nThe first step is to enter the ballots' information. Please enter the specified information below:\n\n")
        
        print("BALLOT " + currentBallot[6] + "\n")
        
        #2A Speaker Info
        print("2A SPEAKER\n")
        BALLOT[currentBallot]['2a']['name'] = raw_input("Name: ")
        ynAnswer = checkYNAnswer(raw_input("Are you sure: Y or N? "))
    while complete == 0:
        BALLOT[currentBallot]['2a']['persuasiveness'] = raw_input("Persuasiveness: ")
        complete = isComplete(BALLOT[currentBallot]['2a']['persuasiveness'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2a']['organization'] = raw_input("Organization: ")
        complete = isComplete(BALLOT[currentBallot]['2a']['organization'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2a']['delivery'] = raw_input("Delivery: ")
        complete = isComplete(BALLOT[currentBallot]['2a']['delivery'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2a']['evidence'] = raw_input("Evidence: ")
        complete = isComplete(BALLOT[currentBallot]['2a']['evidence'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2a']['crossex'] = raw_input("Cross-Examination: ")
        complete = isComplete(BALLOT[currentBallot]['2a']['crossex'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2a']['refutation'] = raw_input("Refutation: ")
        complete = isComplete(BALLOT[currentBallot]['2a']['refutation'])
    complete = 0
    BALLOT[currentBallot]['2a']['total'] = int(BALLOT[currentBallot]['2a']['persuasiveness'])+int(BALLOT[currentBallot]['2a']['organization'])+int(BALLOT[currentBallot]['2a']['delivery'])+int(BALLOT[currentBallot]['2a']['evidence'])+int(BALLOT[currentBallot]['2a']['crossex'])+int(BALLOT[currentBallot]['2a']['refutation'])
    
    ynAnswer = 0
    
    #Ballot Message
    while ynAnswer == 0:
        os.system("clear")
        print("\n\nThe first step is to enter the ballots' information. Please enter the specified information below:\n\n")
        
        print("BALLOT " + currentBallot[6] + "\n")
        
        #1N Speaker Info
        print("1N SPEAKER\n")
        BALLOT[currentBallot]['1n']['name'] = raw_input("Name: ")
        ynAnswer = checkYNAnswer(raw_input("Are you sure: Y or N? "))
    while complete == 0:
        BALLOT[currentBallot]['1n']['persuasiveness'] = raw_input("Persuasiveness: ")
        complete = isComplete(BALLOT[currentBallot]['1n']['persuasiveness'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1n']['organization'] = raw_input("Organization: ")
        complete = isComplete(BALLOT[currentBallot]['1n']['organization'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1n']['delivery'] = raw_input("Delivery: ")
        complete = isComplete(BALLOT[currentBallot]['1n']['delivery'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1n']['evidence'] = raw_input("Evidence: ")
        complete = isComplete(BALLOT[currentBallot]['1n']['evidence'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1n']['crossex'] = raw_input("Cross-Examination: ")
        complete = isComplete(BALLOT[currentBallot]['1n']['crossex'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['1n']['refutation'] = raw_input("Refutation: ")
        complete = isComplete(BALLOT[currentBallot]['1n']['refutation'])
    complete = 0
    BALLOT[currentBallot]['1n']['total'] = int(BALLOT[currentBallot]['1n']['persuasiveness'])+int(BALLOT[currentBallot]['1n']['organization'])+int(BALLOT[currentBallot]['1n']['delivery'])+int(BALLOT[currentBallot]['1n']['evidence'])+int(BALLOT[currentBallot]['1n']['crossex'])+int(BALLOT[currentBallot]['1n']['refutation'])
    
    ynAnswer = 0
    
    #Ballot Message
    while ynAnswer == 0:
        os.system("clear")
        print("\n\nThe first step is to enter the ballots' information. Please enter the specified information below:\n\n")
        
        print("BALLOT " + currentBallot[6] + "\n")
        
        #2N Speaker Info
        print("2N SPEAKER\n")
        BALLOT[currentBallot]['2n']['name'] = raw_input("Name: ")
        ynAnswer = checkYNAnswer(raw_input("Are you sure: Y or N? "))
    while complete == 0:
        BALLOT[currentBallot]['2n']['persuasiveness'] = raw_input("Persuasiveness: ")
        complete = isComplete(BALLOT[currentBallot]['2n']['persuasiveness'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2n']['organization'] = raw_input("Organization: ")
        complete = isComplete(BALLOT[currentBallot]['2n']['organization'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2n']['delivery'] = raw_input("Delivery: ")
        complete = isComplete(BALLOT[currentBallot]['2n']['delivery'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2n']['evidence'] = raw_input("Evidence: ")
        complete = isComplete(BALLOT[currentBallot]['2n']['evidence'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2n']['crossex'] = raw_input("Cross-Examination: ")
        complete = isComplete(BALLOT[currentBallot]['2n']['crossex'])
    complete = 0
    while complete == 0:
        BALLOT[currentBallot]['2n']['refutation'] = raw_input("Refutation: ")
        complete = isComplete(BALLOT[currentBallot]['2n']['refutation'])
    
    complete = 0
    
    while complete == 0:
        ynAnswer = raw_input("Did you go Affirmative: Y or N? ")
        if ynAnswer.lower() == "y":
            BALLOT[currentBallot]['side'] = "aff"
            complete = 1
        elif ynAnswer.lower() == "n":
            BALLOT[currentBallot]['side'] = "neg"
            complete = 1
        elif ynAnswer.lower() == "q":
            sys.exit("Force quit enacted!")
        else:
            print("Invalid answer!")
            complete = 0
    
    complete = 0
    
    while complete == 0:
        ynAnswer = raw_input("Did your team win: Y or N? ")
        if ynAnswer.lower() == "y":
            complete = 1
            BALLOT[currentBallot]['win'] = 1
        elif ynAnswer.lower() == "n":
            complete = 1
            BALLOT[currentBallot]['win'] = 0
        elif ynAnswer.lower() == "q":
            sys.exit("Force quit enacted!")
        else:
            print("Invalid answer!")
            complete = 0
    
    BALLOT[currentBallot]['2n']['total'] = int(BALLOT[currentBallot]['2n']['persuasiveness'])+int(BALLOT[currentBallot]['2n']['organization'])+int(BALLOT[currentBallot]['2n']['delivery'])+int(BALLOT[currentBallot]['2n']['evidence'])+int(BALLOT[currentBallot]['2n']['crossex'])+int(BALLOT[currentBallot]['2n']['refutation'])
    
    ynAnswer = 0
    
    complete = 0
    
    prelimRoundsCountdown -= 1
    
    currentBallotInt += 1
    currentBallotList[6] = str(currentBallotInt)
    currentBallot = "".join(currentBallotList)

#Resetting prelimRoundsCountdown
prelimRoundsCountdown = prelimRounds

#Determining Goal
os.system("clear")
print("\n\nPlease determine what your goal for the tournament was.\n")
os.system('read -s -n 1 -p "Press any key to continue..."')

#Number of prelim rounds
os.system("clear")
print("\n\nThe number of preliminary rounds was:")
print("\n" + str(prelimRounds) + "\n")
os.system('read -s -n 1 -p "Press any key to continue..."')

#Win-Loss Record
os.system("clear")
print("\n\nYour win-loss record was:\n")

while prelimRoundsCountdown > 0:
    currentBallotInt -= 1
    currentBallotList[6] = str(currentBallotInt)
    currentBallot = "".join(currentBallotList)
    if BALLOT[currentBallot]['win'] == 1:
        if BALLOT[currentBallot]['side'] == "aff":
            winCountAff += 1
        else:
            winCountNeg += 1
        winCount += 1
    elif BALLOT[currentBallot]['win'] == 0:
        lossCount += 1
    else:
        print("Somehow you managed to neither win nor lose.")
    prelimRoundsCountdown -= 1

print(str(winCount) + "-" + str(lossCount) + "\n")
os.system('read -s -n 1 -p "Press any key to continue..."')

#Resetting prelimRoundsCountdown
prelimRoundsCountdown = prelimRounds

#Win-Loss By Round
os.system("clear")
print("\n\nYour win-loss record by round was:\n")

while prelimRoundsCountdown > 0:
    if BALLOT[currentBallot]['win'] == 0:
        tempWinLoss = "Loss"
    else:
        tempWinLoss = "Win"
    print("Round " + str(currentBallotInt) + ": " + tempWinLoss)
    currentBallotInt += 1
    currentBallotList[6] = str(currentBallotInt)
    currentBallot = "".join(currentBallotList)
    prelimRoundsCountdown -= 1

os.system('read -s -n 1 -p "\nPress any key to continue..."')

#Number of AFF Wins
os.system("clear")
print("\n\nNumber of AFF wins:\n")
print(winCountAff)
os.system('read -s -n 1 -p "\nPress any key to continue..."')

#Number of NEG Wins
os.system("clear")
print("\n\nNumber of NEG wins:\n")
print(winCountNeg)
os.system('read -s -n 1 -p "\nPress any key to continue..."')