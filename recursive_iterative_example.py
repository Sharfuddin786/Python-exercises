# iterative approach for factorial

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n*factorial_iterative(n-1)

number = int(input("Enter a number:\n"))
print ("factorial by iterative method is:",factorial_iterative(number))
print ("Factorial by recursive method is:", factorial_recursive(number))
