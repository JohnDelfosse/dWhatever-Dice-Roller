import random


def rollD4(amountOfD4, totalSum):
    for die in range(amountOfD4):
        roll = random.randint(1, 4)
        print("d4 #", die + 1, ": ", roll)
        totalSum += roll
    return totalSum

def rollD6(amountOfD6, totalSum):     
    for die in range(amountOfD6):
        roll = random.randint(1, 6)
        print("d6 #", die + 1, ": ", roll)
        totalSum += roll
    return totalSum

def rollD8(amountOfD8, totalSum):     
    for die in range(amountOfD8):
        roll = random.randint(1, 8)
        print("d8 #", die + 1, ": ", roll)
        totalSum += roll
    return totalSum

def rollD10(amountOfD10, totalSum):     
    for die in range(amountOfD10):
        roll = random.randint(1, 10)
        print("d10 #", die + 1, ": ", roll)
        totalSum += roll
    return totalSum

def rollD12(amountOfD12, totalSum):     
    for die in range(amountOfD12):
        roll = random.randint(1, 12)
        print("d12 #", die + 1, ": ", roll)
        totalSum += roll
    return totalSum

def rollD20(amountOfD20, totalSum):     
    for die in range(amountOfD20):
        roll = random.randint(1, 20)
        print("d20 #", die + 1, ": ", roll)
        totalSum += roll
    return totalSum

def rollD100(amountOfD100, totalSum):     
    for die in range(amountOfD100):
        roll = random.randint(1, 100)
        print("d100 #", die + 1, ": ", roll)
        totalSum += roll
    return totalSum
        
def rollDice(amountOfD4, amountOfD6, amountOfD8, amountOfD10, amountOfD12, amountOfD20, amountOfD100):
    total = 0
    total = rollD4(amountOfD4, total)
    total = rollD6(amountOfD6, total)
    total = rollD8(amountOfD8, total)
    total = rollD10(amountOfD10, total)
    total = rollD12(amountOfD12, total)
    total = rollD20(amountOfD20, total)
    total = rollD100(amountOfD100, total)
    print("Total of all rolls: ", total)
    return

print("Welcome to the DND Dice Roller!")
print("-------------------------------")
print(" ")
print("**INSTRUCTIONS**")
print("You can roll d4, d6, d8, d10, d12, d20, and d100.")
print("You can roll up to 10 of each. Type 0 for any you don't want to roll.")
print("After you pick the amount of dice in each group, we'll list each roll and sum their total.")
print(" ")
### Validate input

## Deciding num of d4s
while True:
    try:
        numberOfD4s = int(input("Number of d4s: "))
        if(numberOfD4s >= 0 and numberOfD4s <= 10):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide an integer.")
## Deciding num of d6s
while True:
    try:
        numberOfD6s = int(input("Number of d6s: "))
        if(numberOfD6s >= 0 and numberOfD6s <= 10):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide an integer.")
## Deciding num of d8s
while True:
    try:
        numberOfD8s = int(input("Number of d8s: "))
        if(numberOfD8s >= 0 and numberOfD8s <= 10):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide an integer.")
## Deciding num of d10s
while True:
    try:
        numberOfD10s = int(input("Number of d10s: "))
        if(numberOfD10s >= 0 and numberOfD10s <= 10):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide an integer.")
## Deciding num of d12s
while True:
    try:
        numberOfD12s = int(input("Number of d12s: "))
        if(numberOfD12s >= 0 and numberOfD12s <= 10):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide an integer.")
## Deciding num of d20s
while True:
    try:
        numberOfD20s = int(input("Number of d20s: "))
        if(numberOfD20s >= 0 and numberOfD20s <= 10):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide an integer.")
## Deciding num of d100 rolls
while True:
    try:
        numberOfD100s = int(input("Number of d100s: "))
        if(numberOfD100s >= 0 and numberOfD100s <= 10):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide an integer.")
        


rollDice(numberOfD4s, numberOfD6s, numberOfD8s, numberOfD10s, numberOfD12s, numberOfD20s, numberOfD100s)