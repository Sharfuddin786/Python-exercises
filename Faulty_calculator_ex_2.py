# Make a calculator which returns correct answers except these 45*3 = 555. 56+9 = 77 , 56/6 = 4.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
dict1 = {'+': (num1+num2), '-': (num1-num2), '*': (num1*num2), '/': (num1/num2), '//': (num1//num2), '%': (num1 % num2),'':("This operation is not available on this calculator.")}
print("Select an operation: \n + : add \n - : subtract \n * : multiply \n / : division \n // : divisor \n % : remainder ")
oper = dict1[input()]
while oper =
if oper == '*' and num1 == 45 or num2 == 3:
        print("solution is: 555")
elif oper == '+' and num1 == 56  or num2 == 9:
        print("solution is: 77")
elif oper == '/' and num1 == 56 or num2 == 6:
        print("solution is: 4")
elif oper == "+" or "-" or "/" or "//" or "%":
        print("solution is:", oper)

