def multiply(a,b):
    return a*b

if __name__ == "main":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = multiply(num1, num2)
    print(f"The result of multiplying {num1} and {num2} is: {result}")
