import datetime

def gettime():
    return datetime.datetime.now()

def log(info):
    if info == 1:
        select = int(input("\n Enter 1 to log Food or 2 for Exercise. \n"))
        if select == 1:
            Input = input("\n Type here.\n")
            with open("Harry_food_log.txt","a") as op:
                op.write(str(str(gettime()))+ ":"+ Input + ".\n")
            print("Log Updated Successfully.")
        elif info == 2:
            Input = input("\n Type here. \n")
            with open ("Harry_exercise_log.txt","a") as op:
                op.write(str(str(gettime()))+":"+ Input+".\n")
            print("Log Updated Successfully.")

    elif info == 2:
        select = int(input("\n Enter 1 to log Food or 2 for Exercise \n"))
        if select == 1:
              Input = input("\n Type here. \n")
              with open ("Rohan_food_log.txt","a") as op:
                  op.write(str(str(gettime()))+ ":" +Input+ ".\n")
              print("Log Updated Successfully.")
        elif select == 2:
            Input = input("\n Type here. \n")
            with open ("Rohan_exercise_log.txt","a") as op:
                op.write(str(str(gettime()))+":" + Input + ".\n")
            print("Log Updated Successfully.")

    elif info == 3:
        select = int(input("\n Enter 1 to logFod or 2 for Exercise. \n"))
        if select == 1:
            Input = input("\n Type here. \n")
            with open("Hammad_exercise_log.txt","a") as op:
                op.write(str(str(gettime()))+ ":"+Input+ ".\n")
            print("Log Updated Sucessfully.")
        elif select == 2:
            Input = input("\n Type Here: \n")
            with open("Hammad_exercise_log.txt","a") as op:
                op.write(str(str(gettime()))+":" +Input+".\n")
            print("Log Updated Sucessfuly.")

def retrive(info):
    if info == 1:
        select =int(input("\n Enter 1 to retrive log of Food or 2 for Exercise. \n"))
        if select == 1:
            with open ("Harry_food_log.txt") as op:
                for i in op:
                    print(i, end="")
        elif select ==2:
            with open("Harry_exercise_log.txt") as op:
                for i in op:
                    print(i, end="")

    elif info==2:
        select = int(input("\n Enter 1 to retrive log of Food or 2 for Exercise. \n"))
        if select == 1:
            with open("Rohan_food_log.txt") as op:
                for i in op:
                    print(i, end="")
        elif select == 2:
            with open("Rohan_exercise_log.txt") as op:
                for i in op:
                    print(i, end="")

    elif info ==3:
        select = int(input("\n Enter 1 to retrive log of Food or 2 for Exercise. \n"))
        if select == 1:
            with open("Hammad_food_log.txt") as op:
                for i in op:
                    print(i, end="")
        elif select ==2:
            with open("Hammad_exercise_log.txt") as op:
                for i in op:
                    print(i, end="")


    else:
        print("Enter the right Input.")


print("Welcome to SRK's Health Management System.")
choice = int(input("Enter 1 for log or 2 for retrive."))

if choice == 1:
    name = int(input("Enter: \n 1. for Harry \n 2. for Rohan \n 3. for Hammad \n"))
    log(name)
else:
    name = int(input("Enter: \n 1. for Harry \n 2. for Rohan \n 3. for Hammad \n"))
    retrive(name)





