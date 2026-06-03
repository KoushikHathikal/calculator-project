num1=float(input("Enter a number"))
num2=float(input("Enter a number:"))
operator=input("Enter operator(+,-,*,/):")

if operator=="+":
    print("Result:",num1+num2)
elif operator=="-":
    print("Result:",num1-num2)
elif operator=="*":
    print("Result:",num1*num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation")


