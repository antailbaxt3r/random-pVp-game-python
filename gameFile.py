import subprocess as sp
from sys import exit
from time import sleep

list = [(1, "Akash"),(2, "Arpit"),(3, "Arjun"),(4, "Kinshuk"),(5, "Varun"),(6, "Sarvagnya"),(7, "Yatik")]

player1Character = ""
player2Character = ""
player1Health = 100
player2Health = 100
player1Magic = 0
player2Magic = 0
player1Potions = 1
player2Potions = 1
player1Red = 1
player2Red = 1
player1Blue = 1
player2Blue = 1
player1Attack = 1
player2Attack = 1
player1Defense = 0
player2Defense = 0
player1Green = 2
player2Green = 2


def init():

    global player1Character
    global player2Character
    global player1Health 
    global player2Health
    global player1Magic
    global player2Magic
    global player1Potions
    global player2Potions
    global player1Red
    global player2Red
    global player1Blue
    global player2Blue
    global player1Attack
    global player2Attack
    global player1Defense
    global player2Defense
    global player1Green
    global player2Green

    player1Character = ""
    player2Character = ""
    player1Health = 100
    player2Health = 100
    player1Magic = 0
    player2Magic = 0
    player1Potions = 1
    player2Potions = 1
    player1Red = 1
    player2Red = 1
    player1Blue = 1
    player2Blue = 1
    player1Attack = 1
    player2Attack = 1
    player1Defense = 0
    player2Defense = 0
    player1Green = 2
    player2Green = 2

def clear(): 
    sp.call('clear',shell=True)

def mainScreen():
    clear()
    print("Welcome to LCC GAME")
    print("")
    print("")
    print("")
    loop1()

def loop1():
    print("1. Play Game")
    print("2. Exit")
    print('')
    answer = input()
    if(answer == "1"):
        startGame()

    elif(answer == "2"):
        exit()

    else:
        print("Please enter 1 or 2")
        loop1()


def chooseWarrior():

    global player1Character
    global player2Character

    clear()
    print("Player 1, choose your warrior")
    print("")
    print("1. Akash")
    print("2. Arpit")
    print("3. Arjun")
    print("4. Kinshuk")
    print("5. Varun")
    print("6. Sarvagnya")
    print("7. Yatik")
    

    n = int(input())
    player1Character = list[n-1][1]
    print("Player 1 chose " + player1Character)

    print("Player 2, choose your warrior")
    print("")

    n = int(input())
    player2Character = list[n-1][1]
    print("Player 2 chose " + player2Character)


    loop2()

def loop2():
    print("Continue? [y/n]")
    inp = input()
    if(inp == "y"):
        clear()
    elif(inp == "n"):
        chooseWarrior()
    else:
        print("Type y or n please")
        loop2()


def player1Turn():
    clear()
    if((player1Health > 0) and (player2Health > 0)):
        print("Player 1's turn:")
        print("Player 1's HP = " + str(player1Health))
        print("Player 2's HP = " + str(player2Health))
        print("Player 1's MP = " + str(player1Magic))
        print("Player 2's MP = " + str(player2Magic))
        print("")
        
        loop3()
        sleep(3)
        player2Turn()
    
    elif(player1Health <= 0):

        print("Player 2 WINS!")
        gameOver()

    elif(player2Health <= 0):

        print("Player 1 WINS!")
        gameOver()

def loop3():
    
    print("What do you want to do?")
    print("")
    print("1. Basic Attack")
    print("2. Special Attack")
    print("3. Use Item")
    print("4. Surrender")

    global player2Health

    n = input()
    if(n == '1'):
        basic1()
    elif(n == '2'):
        special1()
    elif(n == '3'):
        items1()
    elif(n == '4'):
        checkSurrender1()
    else:
        print("Please enter valid input")
        
def player2Turn():
    clear()
    if((player1Health > 0) and (player2Health > 0)):
        print("Player 2's turn:")
        print("Player 1's HP = " + str(player1Health))
        print("Player 2's HP = " + str(player2Health))
        print("Player 1's MP = " + str(player1Magic))
        print("Player 2's MP = " + str(player2Magic))
        print("")
        
        loop4()
        sleep(2)
        player1Turn()
    
    elif(player1Health <= 0):
        print("Player 2 WINS!")
        gameOver()
    elif(player2Health <= 0):
        print("Player 1 WINS!")
        gameOver()


def loop4():

    print("What do you want to do?")
    print("")
    print("1. Basic Attack")
    print("2. Special Attack")
    print("3. Use Item")
    print("4. Surrender")

    global player1Health

    n = input()
    if(n == '1'):
        basic2()
    elif(n == '2'):
        special2()
    elif(n == '3'):
        items2()
    elif(n == '4'):
        checkSurrender2()
    else:
        print("Please enter valid input")

def startGame():

    init()
    
    chooseWarrior()
    print("Player 1 chose " + player1Character)
    print("Player 2 chose " + player2Character)
    countdown()
    clear()
    player1Turn()


def basic1():
    
    global player2Health
    
    print("")
    print(player1Character + " attacks!")
    print(player2Character + " looses "+ str(player1Attack * 10 - player2Defense * 5) +" HPs!")
    print("")
    player2Health = player2Health - ((player1Attack * 10) - (player2Defense * 5))

def basic2():
    
    global player1Health

    print("")
    print(player2Character + " attacks!")
    print(player1Character + " looses "+ str(player2Attack * 10 - player1Defense * 5) +" HPs!")
    print("")
    player1Health = player1Health - ((player2Attack * 10) - (player1Defense * 5))

def special1():
    
    global player1Magic
    global player2Health

    if(player1Magic > 0):
        if(player1Character == "Akash"):
            print("")
            print(player1Character + " steals "+ player2Character+"'s food!")
            print(player2Character + " looses "+ str(player1Attack * 20 - player2Defense * 5) +" HPs due to hunger!")
            print("")
            player2Health = player2Health - ((player1Attack * 20) - (player2Defense * 5))
        if(player1Character == "Arpit"):
            print("")
            print(player1Character + " gets drunk!")
            print(player1Character + " is trippy, but more confident! (Weird flex, but okay)")
            print(player2Character + " looses "+ str(player1Attack * 20 - player2Defense * 5) +" HPs!")
            print("")
            player2Health = player2Health - ((player1Attack * 20) - (player2Defense * 5))

        if(player1Character == "Arjun"):
                    print("")
                    print(player1Character + " punches "+ player2Character)
                    print(player2Character + " looses "+ str(player1Attack * 20 - player2Defense * 5) +" HPs due to nosebleed!")
                    print("")
                    player2Health = player2Health - ((player1Attack * 20) - (player2Defense * 5))

        if(player1Character == "Kinshuk"):
                    print("")
                    print(player1Character + " calls and threatens Trump!")
                    print("Trump sends an airstrike on" + player2Character)
                    print(player2Character + " looses "+ str(player1Attack * 20 - player2Defense * 5) +" HPs due to heavy damage!")
                    print("")
                    player2Health = player2Health - ((player1Attack * 20) - (player2Defense * 5))

        if(player1Character == "Varun"):
                    print("")
                    print(player1Character + " throws a glass!")
                    print(player2Character + " looses "+ str(player1Attack * 20 - player2Defense * 5) +" and has forgotten everything about 36:15")
                    print("")
                    player2Health = player2Health - ((player1Attack * 20) - (player2Defense * 5))

        if(player1Character == "Sarvagnya"):
                    print("")
                    print(player1Character + " Madarchod hai")
                    sleep(1)
                    print("Yeah nothing else")
                    print(player2Character + " looses "+ str(player1Attack * 20 - player2Defense * 5) +" HPs just because it is a special attack!")
                    print("")
                    player2Health = player2Health - ((player1Attack * 20) - (player2Defense * 5))

        if(player1Character == "Yatik"):
                    print("")
                    print(player1Character + " spanks "+ player2Character+"'s ass!")
                    print(player2Character + " looses "+ str(player1Attack * 20 - player2Defense * 5) +" HPs and his sense of security!")
                    print("")
                    player2Health = player2Health - ((player1Attack * 20) - (player2Defense * 5))
    
        player1Magic = player1Magic - 10

    else:
        print("You don't have enough Magic Points")
        loop3()


def special2():
    
    global player2Magic
    global player1Health

    if(player2Magic > 0):
        if(player2Character == "Akash"):
            print("")
            print(player2Character + " steals "+ player1Character+"'s food!")
            print(player1Character + " looses "+ str(player2Attack * 20 - player1Defense * 5) +" HPs due to hunger!")
            print("")
            player1Health = player1Health - ((player2Attack * 20) - (player1Defense * 5))
        if(player2Character == "Arpit"):
            print("")
            print(player2Character + " gets drunk!")
            print(player2Character + " is trippy, but more confident! (Weird flex, but okay)")
            print(player1Character + " looses "+ str(player2Attack * 20 - player1Defense * 5) +" HPs!")
            print("")
            player1Health = player1Health - ((player2Attack * 20) - (player1Defense * 5))

        if(player2Character == "Arjun"):
                    print("")
                    print(player2Character + " punches "+ player1Character)
                    print(player1Character + " looses "+ str(player2Attack * 20 - player1Defense * 5) +" HPs due to nosebleed!")
                    print("")
                    player1Health = player1Health - ((player2Attack * 20) - (player1Defense * 5))

        if(player2Character == "Kinshuk"):
                    print("")
                    print(player2Character + " calls and threatens Trump!")
                    print("Trump sends an airstrike on" + player1Character)
                    print(player1Character + " looses "+ str(player2Attack * 20 - player1Defense * 5) +" HPs due to heavy damage!")
                    print("")
                    player1Health = player1Health - ((player2Attack * 20) - (player1Defense * 5))

        if(player2Character == "Varun"):
                    print("")
                    print(player2Character + " throws a glass!")
                    print(player1Character + " looses "+ str(player2Attack * 20 - player1Defense * 5) +" and has forgotten everything about 36:15")
                    print("")
                    player1Health = player1Health - ((player2Attack * 20) - (player1Defense * 5))

        if(player2Character == "Sarvagnya"):
                    print("")
                    print(player2Character + " Madarchod hai")
                    sleep(1)
                    print("Yeah nothing else")
                    print(player1Character + " looses "+ str(player2Attack * 20 - player1Defense * 5) +" HPs just because it is a special attack!")
                    print("")
                    player1Health = player1Health - ((player2Attack * 20) - (player1Defense * 5))

        if(player2Character == "Yatik"):
                    print("")
                    print(player2Character + " spanks "+ player1Character+"'s ass!")
                    print(player1Character + " looses "+ str(player2Attack * 20 - player1Defense * 5) +" HPs and his sense of security!")
                    print("")
                    player1Health = player1Health - ((player2Attack * 20) - (player1Defense * 5))

        player2Magic = player2Magic - 10

    else:
        print("You don't have enough Magic Points")
        loop4()

def items1():
    print("Choose your item:")
    print("")
    print("1. Health Potion <Increases 30 health> <You have "+ str(player1Potions) +">")
    print("2. Red Potion <Increases attack power> <You have "+ str(player1Red) +">")
    print("3. Blue Potion <Increases defense> <You have " + str(player1Blue) + ">")
    print("4. Green Potion <Increases Magic Points> <You have " + str(player1Green) + ">")
    print("5. Cancel")
    print("")
    loop5()

def loop5():

    global player1Attack
    global player1Blue
    global player1Defense
    global player1Green
    global player1Health
    global player1Magic
    global player1Red
    global player1Potions

    n = input()
    
    if(n == '1'):
        if(player1Potions > 0):
            print(player1Character + " drank a Health Potion!")
            player1Health = player1Health + 30
            print(player1Character + "'s health is now " + str(player1Health))
            player1Potions = player1Potions - 1
        else:
            print("You don't have enough potions")
    
    elif(n == '2'):
        if(player1Red > 0):
            print(player1Character + " drank a Red Potion!")
            player1Attack = 2
            player1Red = 0
            print(player1Character + "'s attack power increased!")
        else:
            print("You don't have enough potions")

    elif(n == '3'):
        if(player1Blue > 0):
            print(player1Character + " drank a Blue Potion!")
            player1Defense = 1
            player1Blue = 0
            print(player1Character + "'s defense rose!")
        else:
            print("You don't have enough potions")

    elif(n == '4'):
        if(player1Green > 0):
            print(player1Character + " drank a Green Potion")
            player1Green = player1Green -1
            player1Magic = player1Magic + 10
            print(player1Character + "'s Magic Points are now " + str(player1Magic))
        else:
            print("You don't have enough potions")
    elif(n == 5):
        loop3()
    
    else:
        print("Enter Valid Input")
        loop5()
    

def loop6():

    global player2Attack
    global player2Blue
    global player2Defense
    global player2Green
    global player2Health
    global player2Magic
    global player2Red
    global player2Potions

    n = input()
    
    if(n == '1'):
        if(player2Potions > 0):
            print(player2Character + " drank a Health Potion!")
            player2Health = player2Health + 30
            print(player2Character + "'s health is now " + str(player2Health))
            player2Potions = player2Potions - 1
        else:
            print("You don't have enough potions")
    
    elif(n == '2'):
        if(player2Red > 0):
            print(player2Character + " drank a Red Potion!")
            player2Attack = 2
            player2Red = 0
            print(player2Character + "'s attack power increased!")
        else:
            print("You don't have enough potions")

    elif(n == '3'):
        if(player2Blue > 0):
            print(player2Character + " drank a Blue Potion!")
            player2Defense = 1
            player2Blue = 0
            print(player2Character + "'s defense rose!")
        else:
            print("You don't have enough potions")

    elif(n == '4'):
        if(player2Green > 0):
            print(player2Character + " drank a Green Potion")
            player2Green = player2Green -1
            player2Magic = player2Magic + 10
            print(player2Character + "'s Magic Points are now " + str(player2Magic))
        else:
            print("You don't have enough potions")  
    
    elif(n == 5):
        loop4()
    
    else:
        print("Enter Valid Input")
        loop6()
    

def items2():
    print("Choose your item:")
    print("")
    print("1. Health Potion <Increases 30 health> <You have "+ str(player2Potions) +">")
    print("2. Red Potion <Increases attack power> <You have "+ str(player2Red) +">")
    print("3. Blue Potion <Increases defense> <You have " + str(player2Blue) + ">")
    print("4. Green Potion <Increases Magic Points> <You have " + str(player2Green) + ">")
    print("5. Cancel")
    print("")
    loop6()

def checkSurrender1():

    global player1Health

    print("Are you sure you want to surrender? [y/n]")
    answer = input()
    if(answer == 'y'):
        print(player1Character + " surrenders all his HPs")
        print("")
        player1Health = 0
    else:
        loop3()


def checkSurrender2():

    global player2Health

    print("Are you sure you want to surrender? [y/n]")
    answer = input()
    if(answer == 'y'):
        print(player2Character + " surrenders all his HPs")
        print("")
        player2Health = 0
    else:
        loop4()

def countdown():
    n = 3
    print("The game starts in :")

    while(n > 0):
        print(n)
        sleep(1)
        n = n - 1

    print("FIGHT!")
    sleep(2)

def gameOver():
    
    print("What do you want to do next?")
    print("")
    print("1. Play again")
    print("2. Exit to Main Menu")
    print("3. Exit Program")
    loop7()

def loop7():
    
    final = input()
    
    if(final == '1'):
        startGame()
    elif(final == '2'):
        mainScreen()
    elif(final == '3'):
        exit()
    else:
        print("Enter Valid Input")
        loop7()



mainScreen()
