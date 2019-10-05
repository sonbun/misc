#quizmaker advanced
usernamelist = []
userscore = []
number = 0
mathslist = []
chemilist = []
astrolist = []
cslist = []
while True:
    number += 1
    if number == 4:
        break
    else:
        username = input("\nWhat is your name?: ")
        totalpoints = 0
        #maths
        mathspoint = 0
        print("\nMaths: \n")
        answer1 = input("Q1: What is 2^3?: ")
        if answer1 in ['8','eight','Eight']:
            totalpoints += 1
            mathspoint += 1
        answer2 = input("Q2: What is 8/2?: ")
        if answer2 in ['4','four','Four']:
            totalpoints += 1
            mathspoint += 1
        answer3= input("Q3: What is sin(30°)?: ")
        if answer3 in ['1/2','one half','0.5','One half']:
            totalpoints += 1
            mathspoint += 1
        answer4 = input("Q4: What is tan(45°)?: ")
        if answer4 in ['1','one','One']:
            totalpoints += 1
            mathspoint += 1
        answer5 = input("Q5: What is cosec(90°)?: ")
        if answer5 in ['1','one','One']:
            totalpoints += 1
            mathspoint += 1
        #chemistry
        chemistry = 0
        print("\n Chemistry:\n")
        answer1 = input("Q1: What type of reaction is Acid + Base?: ")
        if answer1 in ['neutralisation','neutralization','Neutralisation','Neutralization','Acid-base reaction','acid-base reaction','acid base reaction','Acid base reaction']:
            totalpoints += 1
            chemistry += 1
        answer2 = input("Q2: Which piece of apparatus is used to measure 24.8 cm^3 of gas produced during a reaction?: ")
        if answer2 in ['conical flask','Conical flask']:
            totalpoints += 1
            chemistry += 1
        answer3= input("Q3: Which element is life based around?: ")
        if answer3 in ['Carbon','C','c','carbon']:
            totalpoints += 1
            chemistry += 1
        answer4 = input("Q4: How many electrons does an Oxygen atom have?: ")
        if answer4 in ['8','eight','Eight']:
            totalpoints += 1
            chemistry += 1
        answer5 = input("Q5: What is the first element on the periodic table?: ")
        if answer5 in ['H','h','Hydrogen','hydrogen']:
            totalpoints += 1
            chemistry += 1

        #astrophysics
        astrophysicspoints = 0
        astrophysics = 0
        print("\nAstrophysics:\n")
        answer1 = input("Q1: The sun is made mostly from what element?: ")
        if answer1 in ['Hydorgen','hydrogen','H','h']:
            totalpoints += 1
            astrophysics += 1
        answer2 = input("Q2: What is the process that 'powers' stars?: ")
        if answer2 in ['Nuclear fusion','nuclear fusion']:
            totalpoints += 1
            astrophysics += 1
        answer3= input("Q3: The final stage for the most massive stars is either a massive explosion known as a supernova or gravitational collapse into a …: ")
        if answer3 in ['black hole','blackhole','Blackhole','Black hole']:
            totalpoints += 1
            astrophysics += 1
        answer4 = input("Q4: The Kepler space telescope has found more what than any other telescope?: ")
        if answer4 in ['exoplanets','Exoplanets','exoplanet','Exoplanet']:
            totalpoints += 1
            astrophysics += 1
        answer5 = input("Q5: What is the stellar equivalent of a rogue planet?: ")
        if answer5 in ['Intergalactic star','intergalactic star']:
            totalpoints += 1
            astrophysics += 1

        #computerscience
        csscore = 0
        print("\nComputer Science:\n")
        answer1 = input("Q1: Convert 00000001 to denary: ")
        if answer1 in ['1','one','One']:
            totalpoints += 1
            csscore += 1
        answer2 = input("Q2: Convert 00000010 to denary: ")
        if answer2 in ['2','two','Two']:
            totalpoints += 1
            csscore += 1
        answer3= input("Q3: Convert 00000011 to denary: ")
        if answer3 in ['3','three','Three']:
            totalpoints += 1
            csscore += 1
        answer4 = input("Q4: Convert 00000100 to denary: ")
        if answer4 in ['4','four','Four']:
            totalpoints += 1
            csscore += 1
        answer5 = input("Q5: Convert 00000101 to denary: ")
        if answer5 in ['5','five','Five']:
            totalpoints += 1
            csscore += 1
        print("")
        if totalpoints <= 20 and totalpoints >=18:
            print("Your Grade: A  (", totalpoints,"/ 20 )")
        elif totalpoints <= 17 and totalpoints >= 15:
            print("Your Grade: B  (", totalpoints,"/ 20 )")
        elif totalpoints <= 14 and totalpoints >= 12:
            print("Your Grade: C  (", totalpoints,"/ 20 )")
        elif totalpoints <= 11 and totalpoints >= 9:
            print("Your Grade: D  (", totalpoints,"/ 20 )")
        elif totalpoints <= 8 and totalpoints >= 6:
            print("Your Grade: E  (", totalpoints,"/ 20 )")
        elif totalpoints <= 5:
            print("Your Grade: F  (", totalpoints,"/ 20 )")
        usernamelist.append(username)
        userscore.append(totalpoints)
        mathslist.append(mathspoint)
        chemilist.append(chemistry)
        astrolist.append(astrophysics)
        cslist.append(csscore)


print("")
averagepoints = len(userscore) / 3
if totalpoints <= 20 and averagepoints >=18:
    print("Average Grade: A ")
elif totalpoints <= 17 and totalpoints >= 15:
    print("Average Grade: B")
elif totalpoints <= 14 and totalpoints >= 12:
    print("Average Grade: C")
elif totalpoints <= 11 and totalpoints >= 9:
    print("Average Grade: D")
elif totalpoints <= 8 and totalpoints >= 6:
    print("Average Grade: E")
elif totalpoints <= 5:
    print("Average Grade: F")

print(usernamelist[0],"has scored a total of",userscore[0],"\nMaths: ",mathslist[0],"\nChemistry: ",chemilist[0],"\nAstrophysics: ",astrolist[0],"\nComputer Science: ",cslist[0])
print("")
print(usernamelist[1],"has scored a total of",userscore[1],"\nMaths: ",mathslist[1],"\nChemistry: ",chemilist[1],"\nAstrophysics: ",astrolist[1],"\nComputer Science: ",cslist[1])
print("")
print(usernamelist[2],"has scored a total of",userscore[2],"\nMaths: ",mathslist[0],"\nChemistry: ",chemilist[2],"\nAstrophysics: ",astrolist[2],"\nComputer Science: ",cslist[2])
