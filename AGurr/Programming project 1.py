import random
import os
z = 1
J = 0
P1S = 0
P2S = 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
print("|                         WELCOME                        |")
print("#~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~#")
print("|       1)PlAY     |     2)SCORES     |   3)New Player   |")
print("#~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~#")


print("   ____")
print("  /\' . \    _____")
print(" /: \___\  / .  /\ ")
print(" \\' / . / /____/..\ ")
print("  \/___/  \\'  '\  /")
print("           \\'__'\/")

YES = int(input(">"))

f = open("PlayerScore.txt", "r")
user_file_lines = f.readlines()
f.close()

if YES == 2:
    found_user = False
    while found_user == False:
        P = input("Please Enter you Name ")
        y = 0
        while y < len(user_file_lines):
            if P == user_file_lines[y].strip():
                found_user = True
                break
            y = y + 1
        if found_user == False:
                print("user not found")
    while J == 0:
        Pass = input("Please enter your password ")
        Password = user_file_lines[y+1].strip()
        if Pass == Password:
            print("Sucsess welcome")
            P1 = P
            break
        else:
            print("Password Incorrect")
    print("Hello",P1,"here are your scores")
    print("")
    print(user_file_lines[y+2])
    print(user_file_lines[y+3])

    if os.path.exists("HighScores.txt"):
        f = open("HighScores.txt", "r")
        high_scores_lines = f.readlines()
        f.close()

    print()
    print("The hightest scores are :-")
    print()
    y=0
    while y < len(high_scores_lines):
        HSl = high_scores_lines[y].strip()
        print(y+1,":",HSl[:HSl.find(";")]," - ",HSl[HSl.find(";")+1:])
        y = y + 1

elif YES == 3:
    f = open("PlayerScore.txt", "a")
    P = input("Please Enter Your Name! ")
    Pass = input("Please Enter Your Password ")
    ConPass = input("Please confirm your Password ")
    while Pass != ConPass:
        print("Password doesn't match")
        ConPass = input("Please confirm your Password ")
    f.write(P)
    f.write("\n")
    f.write(Pass)
    f.write("\n")
    f.write("Win:0")
    f.write("\n")
    f.write("Loss:0")
    f.write("\n")
    f.close()


elif YES == 1:
    print("      Player 1      ")
    print("#~~~~~~~~~~~~~~~~~~#")
    print("|    To log In     |")
    print("|   Press return   |")
    print("#~~~~~~~~~~~~~~~~~~#")
    YES2 = input(">")


    f = open("PlayerScore.txt", "r")
    found_user = False
    while found_user == False:
        P = input("Please Enter you Name ")
        y = 0
        while y < len(user_file_lines):
            if P == user_file_lines[y].strip():
                found_user = True
                P1line = y
                break
            y = y + 1
        if found_user == False:
                print("user not found")
    while J == 0:
        Pass = input("Please enter your password ")
        Password = user_file_lines[y+1].strip()
        if Pass == Password:
            print("Sucsess welcome",P)
            P1 = P
            break
        else:
            print("Password Incorrect")
    f.close()

    print("      Player 2      ")
    print("#~~~~~~~~~~~~~~~~~~#")
    print("|    To log In     |")
    print("|   Press return   |")
    print("#~~~~~~~~~~~~~~~~~~#")
    YES2 = input(">")


    found_user = False
    while found_user == False:
        P = input("Please Enter you Name ")
        y = 0
        while y < len(user_file_lines):
            if P == user_file_lines[y].strip():
                found_user = True
                P2line = y
                break
            y = y + 1
        if found_user == False:
                print("user not found")
    while J == 0:
        Pass = input("Please enter your password ")
        Password = user_file_lines[y+1].strip()
        if Pass == Password:
            print("Sucsess welcome",P)
            P2 = P
            break
        else:
            print("Password Incorrect")




















    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    while z < 6:

        print ("Round ",z)
        print("|")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        P1G = random.randint(2,12)
        print (P1,"Got",P1G)
        P1S = (P1G + P1S)
        print("|")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        P1B = P1G % 2
        if P1B == 0:
            print (P1,"Even +10")
            P1S = P1S + 10
        else:
            print (P1,"Odd -5")
            if P1S < 6:
                P1S = 0
            else:
                P1S = P1S - 5
        if P1G == 2:
            P1DR2 = random.randint(1,6)
            print (P1,"Double Roll +",P1DR2)
            P1S = P1S +P1DR2
        elif P1G == 12:
            P1DR2 = random.randint(1,6)
            print (P1,"Double Roll +",P1DR2)
            P1S = P1S +P1DR2
        elif P1B == 0:
            P1DR = random.randint(1,11)
            if P1DR == 1:
                P1DR2 = random.randint(1,6)
                print (P1,"Double Roll +",P1DR2)
                P1S = P1S +P1DR2
        print("|")
        print (P1S)
        print("|")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        P2G = random.randint(2,12)
        print (P2,"Got",P2G)
        P2S = (P2G + P2S)
        print("|")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        P2B = P2G % 2
        if P2B == 0:
            print (P2,"Even +10")
            P2S = P2S + 10
        else:
            print (P2,"Odd -5")
            if P2S < 6:
                P2S = 0
            else:
                P2S = P2S - 5
        if P2G == 2:
            P2DR2 = random.randint(1,6)
            print (P2,"Double Roll +",P2DR2)
            P2S = P2S +P2DR2
        elif P2G == 12:
            P2DR2 = random.randint(1,6)
            print (P2,"Double Roll +",P2DR2)
            P2S = P2S +P2DR2
        elif P2B == 0:
            P2DR = random.randint(1,11)
            if P2DR == 1:
                P2DR2 = random.randint(1,6)
                print (P2,"Double Roll +",P2DR2)
                P2S = P2S +P2DR2
        print("|")
        print (P2S)
        print("|")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        z = (z+1)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    print (P1 ,"Got",P1S)
    print (P2 ,"Got",P2S)
    P1DR3 = P2DR3 = 0
    if P1S == P2S:
        print ("Sudden Death")
        while P1DR3 == P2DR3 :
            P1DR3 = random.randint(1,6)
            P2DR3 = random.randint(1,6)
            print (P1,P1DR3)
            print (P2,P2DR3)
            if P1DR3 == P2DR3 :
                print ("Scores still equal")

# I should make a TEMP copy of the file in case the program crashes
    if os.path.exists("PlayerScore.txt"):
        os.remove("PlayerScore.txt")
    if (P1S + P1DR3) > (P2S + P2DR3):
        print (P1 ,"Wins")
# Update file lines array with P1 win
        P1Wins_line = user_file_lines[P1line+2].strip()
        P1Wins = int(P1Wins_line[4:])
        P1Wins = P1Wins + 1
        P1Wins_line = "Win:"+str(P1Wins)+"\n"
        user_file_lines[P1line+2] = P1Wins_line
# Update file lines array with P2 loss
        P2Losses_line = user_file_lines[P2line+3].strip()
        P2Losses = int(P2Losses_line[5:])
        P2Losses = P2Losses + 1
        P2Losses_line = "Loss:"+str(P2Losses)+"\n"
        user_file_lines[P2line+3] = P2Losses_line

    else:
        print (P2,"Wins")
# Update file lines array with P2 win
        P2Wins_line = user_file_lines[P2line+2].strip()
        P2Wins = int(P2Wins_line[4:])
        P2Wins = P2Wins + 1
        P2Wins_line = "Win:"+str(P2Wins)+"\n"
        user_file_lines[P2line+2] = P2Wins_line
# Update file lines array with P1 loss
        P1Losses_line = user_file_lines[P1line+3].strip()
        P1Losses = int(P1Losses_line[5:])
        P1Losses = P1Losses + 1
        P1Losses_line = "Loss:"+str(P1Losses)+"\n"
        user_file_lines[P1line+3] = P1Losses_line

    f = open("PlayerScore.txt", "a")
    y = 0
    while y < len(user_file_lines):
        f.write(user_file_lines[y])
        y = y + 1
    f.close

# Check is file exists - read it and then delete ready to write out new scores
# I should make a TEMP copy of the file in case the program crashes
    if os.path.exists("HighScores.txt"):
        f = open("HighScores.txt", "r")
        high_scores_lines = f.readlines()
        f.close()
        os.remove("HighScores.txt")
        HSs = len(high_scores_lines)
        y = HSs - 1
        print(y,HSs)
        while y >= 0:
            HSl = high_scores_lines[y].strip()
            print(HSl)
            HS = int(HSl[HSl.find(";")+1:])
            if P1S > P2S:
                if P1S > HS:
                    high_scores_lines[y]=P1+";"+str(P1S)+"\n"
                    if y < HSs:
                        if y+1 > HSs -1:
                            high_scores_lines.append(HSl+"\n")
                        else:
                            high_scores_lines[y+1]=HSl+"\n"
                else:
                    if HSs < 5 and y == HSs - 1:
                        high_scores_lines.append(P1+";"+str(P1S)+"\n")
                    break
            else:
                if P2S > HS:
                    high_scores_lines[y]=P2+";"+str(P2S)+"\n"
                    if y < HSs:
                        if y+1 > HSs -1:
                            high_scores_lines.append(HSl+"\n")
                        else:
                            high_scores_lines[y+1]=HSl+"\n"
                else:
                    if HSs < 5 and y == HSs - 1:
                        high_scores_lines.append(P2+";"+str(P2S)+"\n")
                    break
            y = y - 1
    else:
        high_scores_lines=[]
        if P1S > P2S:
            high_scores_lines.append(P1+";"+str(P1S)+"\n")
        else:
            high_scores_lines.append(P2+";"+str(P2S)+"\n")

    f = open("HighScores.txt", "a")
    y = 0
    while y < 5:
        f.write(high_scores_lines[y])
        y = y + 1
    f.close
