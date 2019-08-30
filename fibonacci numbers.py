# Fibonacci numbers using recursive method.

def fib_recur(number):
    if number==0:
                return 0
    elif number==1:
                return 1
    else:
        return (fib_recur(number-2)+fib_recur(number-1))

number =int(input("\n Enter a number: \n"))
for num in range(0,number):
    print(fib_recur(num))

# Fibonacci numbers using iterative method.

def fib_iter(number):
    fib = 0
    first_num = 0
    second_num = 1
    while(fib<number):
        if (fib<=1):
            Next = fib
        else:
            Next = first_num+second_num
            first_num = second_num
            second_num = Next
        print(Next)
        fib +=1
number = int(input("\n Enter a number: \n "))
fib_iter(number)

