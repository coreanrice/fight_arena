import socket # for socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print ("the socket has successfully connected to google")
#Intro
print ("For each fighter, give them a name, attack , dodge, and luck")
print ("Attack + dodge + luck must == 100")
print ("Each attribute must be greater than 10 and less than 80.")
print ("The program can also read in a file iwth the following style format:")
print ("Jimmy 50 10 40")
print ("John 33 33 34")
print ("Billy 10 10 80")

class Fighter:
    def __init__(self, fighter_id, name, health, attack, dodge, luck):
        self.fighter_id = fighter_id
        self.name = name
        self.health = health
        self.attack = attack
        self.dodge = dodge
        self.luck = luck

        try:
            self.fighter_id is not None
        except TypeError:
            print("fighter_id must be assigned")

    def __str__(self):
        return (f"{self.name} with attack {self.attack} dodge {self.dodge} luck {self.luck}")

def checkValidAttribute(attackPoints, dodgePoints, luckPoints): #checking the fighter's allocated points
    if (dodgePoints == 0 and luckPoints == 0):
        if (attackPoints < 10 or attackPoints > 80):
            print("That was not a proper allocation of fighter's points")
            exit()
    elif (luckPoints == 0):
        if (dodgePoints < 10 or (attackPoints + dodgePoints) > 90):
            print("That was not a proper allocation of fighter's points")
            exit()
    else:
        if (luckPoints < 10 or (luckPoints + dodgePoints + attackPoints) != 100):
            print("That was not a proper allocation of fighter's points")
            exit()

typeSelection = int(input("Type 1 to upload a file or type 2 to enter fighters manually:\n"))
fightersDict = {}

if (typeSelection == 1): #taking a file
    #fighterFileName = input("What file: ")
    with open('fighters.txt') as f:
        lines = f.readlines()
        count = 1
        for line in lines:
            eachLine = line.strip().split( ) #fighter info per line
            for element in eachLine:
                fightersDict[count] = [eachLine[0], 200, eachLine[1], eachLine[2], eachLine[3]]
            count += 1


    for i in range()
    print("type 1 complete")

elif (typeSelection == 2): #manually enter
    fighterNum = int(input("How many fighters? "))
    for i in range(1,fighterNum+1):
        fighterName = input("Fighter " + str(i) + " What is your fighter's name?\n")
        print("Mighty " + fighterName + " now you must allocate 100 total points into three categories")
        attackNum = int(input("Attack:\n"))
        checkValidAttribute(attackNum, 0, 0)
        #if (attackNum < 10 or attackNum > 80): #checking the fighter's allocated points
            #print("That was not a proper allocation of fighter's points")
            #exit()
        dodgeNum = int(input("Dodge:\n"))
        checkValidAttribute(attackNum, dodgeNum, 0)
        #if (dodgeNum < 10 or (dodgeNum + attackNum) > 90): #checking the fighter's allocated points
        #    print("That was not a proper allocation of fighter's points")
        #    exit()
        luckNum = int(input("Luck:\n"))
        checkValidAttribute(attackNum, dodgeNum, luckNum)
        #if (luckNum < 10 or (luckNum + dodgeNum + attackNum) != 100): #checking the fighter's allocated points
        #    print("That was not a proper allocation of fighter's points")
        #    exit()
        fightersDict[i] = [fighterName, 200, attackNum, dodgeNum, luckNum] #aggregate fighters

#    print(fightersDict.items())
    print("type 2 complete")

else: #checking for a valid type selection
    print ("That is not a valid type for this program.")
