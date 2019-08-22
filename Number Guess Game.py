# Number guess game
secret_num = 50
print("Welcome to Guess the number.")
print("You have 5 chances to guess.")
print("Start!!")
i = 0
j = 5
while (i < 5):
    inp = int(input("Enter the number: \n"))
    if inp < secret_num :
        print("Try a bigger number.\n")
        i += 1
        print("Still", j-i, "chances remaining.")
    elif inp > secret_num:
        i += 1
        print("Try a smaller number.\n")
        print("Still", j- i, "chances remaining.")
    elif inp == secret_num:
        print("BINGO. You won !")
        break

if j-i == 0 :
    print("Game Over!!")