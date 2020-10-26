import random
count = 5
countnum = 1
yourpoint = 0
compoints=0

while countnum <= count:
    mylist = ["S","G","W"]
    ran = random.choice(mylist)
    print ("Enter your  S/G/W")
    your= input(str())
    if your not in mylist:
        print("You entered wrong choice and lost this count, ENTER again")
    if your == ran:
        print(f"you entered {your}  and com entered {ran}")
        print("Its a Tie")
        print("you points", yourpoint)
        print("com points", compoints)
        print("ENTER again")
    elif your == "W" and ran == "S":
        print(f"you entered, {your}  and com enetered, {ran}")
        print("you won and com lost")
        yourpoint = yourpoint + 1
        print("you points" , yourpoint)
        print("com points", compoints)
    elif your == "W" and ran == "G":
        print(f"you entered, {your}  and com enetered, {ran}")
        print("you won and com lost")
        yourpoint = yourpoint + 1
        print("you points", yourpoint)
        print("com points", compoints)
    elif your == "G" and ran == "S":
        print(f"you entered, {your}  and com enetered, {ran}")
        print("you won and com lost")
        yourpoint = yourpoint + 1
        print("you points", yourpoint)
        print("com points", compoints)
    elif your == "G" and ran == "W":
        print(f"you entered, {your}  and com enetered, {ran}")
        print("you lost and com won")
        compoints = compoints + 1
        print("you points", yourpoint)
        print("com points", compoints)

    elif your == "S" and ran == "W":
        print(f"you entered, {your}  and com enetered, {ran}")
        print("you lost and com won")
        compoints = compoints + 1
        print("you points", yourpoint)
        print("com points", compoints)

    elif your == "S" and ran == "G":
        print(f"you entered, {your}  and com enetered, {ran}")
        print("you lost and com won")
        compoints = compoints + 1
        print("you points", yourpoint)
        print("com points", compoints)
    #print("countnum is ", countnum)
    print("Choice left", count - countnum)
    countnum = countnum+1

    #print("countnum after update ", countnum)

if count < countnum:
        print("GAME OVER")
        print("Total score is")
        print("yourpoint", yourpoint)
        print("compoints", compoints)
