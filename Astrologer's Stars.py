inp_int = int(input("Enter a number: \n"))
inp_bool = int(input('Enter 0/1 : \n'))
i = 0
while i<inp_int:
    if inp_bool== True:
        print("*"*(i+1))
        i+=1
    elif inp_bool== False:
        print("*"*inp_int)
        inp_int-=1
