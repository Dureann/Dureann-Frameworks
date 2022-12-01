#RED Pattern Framework (RPF)
#Init, imports, vars
import random
import time
ptype = "Blank"
waittime = True
pttrnnum = 0
lcount = 0
hcount = 0
#Functuons
def length():
    global glength
    while True:
        glength = input("Enter length:")
        try:
            val1 = int(glength)
            if val1 >= 2 & val1 <= 10:
                break
            else:
                print("Length must be 2 or more, 10 or less.")
        except ValueError:
            print("Amount must be a whole number.")
    return val1
def height():
    global gheight
    while True:
        gheight = input("Enter height:")
        try:
            val2 = int(gheight)
            if val2 >= 2 & val2 <= 10:
                break
            else:
                print("Height must be 2 or more, 10 or less.")
        except ValueError:
            print("Amount must be a whole number.")
    return val2
#Intro + Type
print("""Welcome to the
 __  ___ __ 
[__)[__ |  \\
|  \[___|__/ Pattern Framework
v 1.8.5,
TR77, Durian Technologies 2022
""")
print("""Patterns:
\"A\" = Random Custom
\"B\" = \"Arrow\" Style 5x5
\"C\" = \"Butterfly\" Style 5x5
Commands:
\"X\" = Debug (REMOVE THIS IN FINAL VERSION)
\"Y\" = Toggle pause time
\"Z\" = Quit this Program""")
#Input line
while (ptype != "Z"):
    ptype = input("Enter a Letter:")
#Waittime toggle
    if ptype == "Y":
        waittime = not waittime
        print("Wait time toggled.")
        print("Wait time on?: " + str(waittime))
#Type A Custom
    if ptype == "A":
        length()
        height()
        print("Your grid is " + str(glength) + "x" + str(gheight))
        lcount = glength
        hcount = gheight
        llist = []
        for i in range(int(glength)):
            llist.append("X")
        for i in range(int(gheight)):
            print(llist)
#Type B Butterfly Patern
    if ptype == "B":
        cX1 = random.randint(1,3)
        cY1 = random.randint(1,3)
        cO1 = random.randint(1,3)
        cZ1 = random.randint(1,3)
        cR1 = random.randint(1,3)
        cT1 = random.randint(1,3)
        cL1 = random.randint(1,3)
        cF1 = random.randint(1,3)
        cC1 = random.randint(1,3)
        if cX1 == 1:
            cX2 = "░░░"
        elif cX1 == 2:
            cX2 = "▒▒▒"
        elif cX1 == 3:
            cX2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cY1 == 1:
            cY2 = "░░░"
        elif cY1 == 2:
            cY2 = "▒▒▒"
        elif cY1 == 3:
            cY2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cO1 == 1:
            cO2 = "░░░"
        elif cO1 == 2:
            cO2 = "▒▒▒"
        elif cO1 == 3:
            cO2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cZ1 == 1:
            cZ2 = "░░░"
        elif cZ1 == 2:
            cZ2 = "▒▒▒"
        elif cZ1 == 3:
            cZ2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cR1 == 1:
            cR2 = "░░░"
        elif cR1 == 2:
            cR2 = "▒▒▒"
        elif cR1 == 3:
            cR2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cT1 == 1:
            cT2 = "░░░"
        elif cT1 == 2:
            cT2 = "▒▒▒"
        elif cT1 == 3:
            cT2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cL1 == 1:
            cL2 = "░░░"
        elif cL1 == 2:
            cL2 = "▒▒▒"
        elif cL1 == 3:
            cL2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cF1 == 1:
            cF2 = "░░░"
        elif cF1 == 2:
            cF2 = "▒▒▒"
        elif cF1 == 3:
            cF2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        if cC1 == 1:
            cC2 = "░░░"
        elif cC1 == 2:
            cC2 = "▒▒▒"
        elif cC1 == 3:
            cC2 = "▓▓▓"
        else:
            print("error in random number generation.")
            quit()
        print("Arrow Pattern (C):")
        if waittime == True:
            time.sleep(.5)
        print(str(cR2) + str(cT2) + str(cL2) + str(cF2) + str(cC2))
        print(str(cZ2) + str(cR2) + str(cT2) + str(cL2) + str(cF2))
        print(str(cO2) + str(cZ2) + str(cR2) + str(cT2) + str(cL2))
        print(str(cY2) + str(cO2) + str(cZ2) + str(cR2) + str(cT2))
        print(str(cX2) + str(cY2) + str(cO2) + str(cZ2) + str(cR2))
        pttrnnum = pttrnnum + 1
        if waittime == True:
            time.sleep(1)
#Type C Butterfly Patern
    if ptype == "C":
        if waittime == True:
            time.sleep(.5)
        typectype = input("""
Type of Pattern:
\"A\" = Complex
\"B\" = Basic""")
        typectype = input("Enter a Letter:")
        if typectype == "A":
            cX1 = random.randint(1,6)
            cY1 = random.randint(1,6)
            cO1 = random.randint(1,6)
            if cX1 == 1:
                cX2 = "░"
            elif cX1 == 2:
                cX2 = "▒"
            elif cX1 == 3:
                cX2 = "▓"
            elif cX1 == 4:
                cX2 = "█"
            elif cX1 == 5:
                cX2 = "▯"
            elif cX1 == 6:
                cX2 = "◇"
            else:
                print("error in random number generation.")
                quit()
            if cY1 == 1:
                cY2 = "▞"
            elif cY1 == 2:
                cY2 = "▟"
            elif cY1 == 3:
                cY2 = "◯"
            elif cY1 == 4:
                cY2 = "▬"
            elif cY1 == 5:
                cY2 = "◍"
            elif cY1 == 6:
                cY2 = "◦"
            else:
                print("error in random number generation.")
                quit()
            if cO1 == 1:
                cO2 = "■"
            elif cO1 == 2:
                cO2 = "▢"
            elif cO1 == 3:
                cO2 = "▣"
            elif cO1 == 4:
                cO2 = "▦"
            elif cO1 == 5:
                cO2 = "▧"
            elif cO1 == 6:
                cO2 = "▩"
            else:
                print("error in random number generation.")
                quit()
        if typectype == "B":
            cX1 = random.randint(1,3)
            cY1 = random.randint(1,3)
            cO1 = random.randint(1,3)
            if cX1 == 1:
                cX2 = "░"
            elif cX1 == 2:
                cX2 = "▒"
            elif cX1 == 3:
                cX2 = "▓"
            else:
                print("error in random number generation.")
                quit()
            if cY1 == 1:
                cY2 = "░"
            elif cY1 == 2:
                cY2 = "▒"
            elif cY1 == 3:
                cY2 = "▓"
            else:
                print("error in random number generation.")
                quit()
            if cO1 == 1:
                cO2 = "░"
            elif cO1 == 2:
                cO2 = "▒"
            elif cO1 == 3:
                cO2 = "▓"
            else:
                print("error in random number generation.")
                quit()
        print("Butterfly Pattern (C):")
        if waittime == True:
            time.sleep(.5)
        print(str(cX2) + " " + str(cX2) + " " + str(cO2) + " " + str(cX2) + " " + str(cX2))
        print(str(cX2) + " " + str(cY2) + " " + str(cO2) + " " + str(cY2) + " " + str(cX2))
        print(str(cO2) + " " + str(cO2) + " " + str(cO2) + " " + str(cO2) + " " + str(cO2))
        print(str(cX2) + " " + str(cY2) + " " + str(cO2) + " " + str(cY2) + " " + str(cX2))
        print(str(cX2) + " " + str(cX2) + " " + str(cO2) + " " + str(cX2) + " " + str(cX2))
        pttrnnum = pttrnnum + 1
        if waittime == True:
            time.sleep(1)
#debug
    if ptype == "X":
        print("Wait Time: " + str(waittime))
        print("Pattern Count: " + str(pttrnnum))
#Input not recognized
    if ptype == "Z":
        print("Thank you for using RPF.")
        quit()