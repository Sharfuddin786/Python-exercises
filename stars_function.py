def stars(int_input,bool_input):
    i = 0
    while i<int_input:
        if bool_input == True:
            print("*"*(i+1))
            i+=1
        elif bool_input == False:
            print("*"*int_input)
            int_input-=1

stars(10,1)
