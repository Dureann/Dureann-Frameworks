#EXP+QDRTC Franework Version
import time
import math
#Base Equasion setup
def base_info():
    print(" ")
    val_a = int(input("Your Value for a: "))
    val_b = int(input("Your Value for b: "))
    val_c = int(input("Your Value for c: "))
#Equasion (ax**2 + bx + c)
    print("Your Equasion = " + str(val_a) + "x^2 + " + str(val_b) + "x + " + str(val_c))
#Vertex (-b/2(a))
    vertex = ((-1) * (val_b)) / (2 * (val_a))
    Tvertex = vertex
#y-int (ax**2 + bx + c (x = 0))
    y_int = ((val_a ** 0) + (val_b * 0) + (val_c))
#Discriminant (b^2 - 4(a)(c))
    disc = ((val_b ** 2) - (4 * val_a * val_c))
    if disc < 0:
        deez = 2
    if disc == 0:
        deez = 1
    if disc > 0:
        deez = -2
#Solutions (-b +/- sqrt(disc))
    if deez == 2:
        solved_x1 = (((-1) * val_b) - math.sqrt((4 * val_a * val_c)))
        solved_x2 = (((-1) * val_b) + math.sqrt((4 * val_a * val_c)))
    if deez == 0:
        solved_x1 = (((-1) * val_b) - math.sqrt((4 * val_a * val_c)))


#Answers (base)
    #Equasion output already printed
    print("Vertex: " + str(Tvertex))
    print("y-int: " + str(y_int))
    print("Discriminant: " + str(disc))

    #Answers (solutions)
    if deez == 2:
        print("Solutions are: {" + str(solved_x1) + "," + str(solved_x2) + "}.")
    if deez == 0:
        print("Solutions are: {" + str(solved_x1) + "," + str(solved_x2) + "}.")
    if deez == -1:
        print("Solution contains no real numbers.")


#Intro
print("""            
 EXPUltimate (Framework Version)
 Made by Duraenn
 Anti-Club 2022""")
time.sleep(.5)
#Function
base_info()
time.sleep(2)
print(""); print("Thank You for using. Durian Technologies 2022.")
quit()
