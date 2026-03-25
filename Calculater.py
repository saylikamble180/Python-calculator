# Simple Calculator
choice = "yes"
while choice == "yes":

    n1 = float(input("Enter a value"))
    sym = input("Select operation: (+) or (-) or (*) or (/)")
    n2 = float(input("Enter second value"))

    if sym == "+":
        print(f"Result: {n1} + {n2} = {n1+n2}")
    elif sym == "-":
        print(f"Result: {n1} - {n2} = {n1-n2}")
    elif sym == "*":
        print(f"Result: {n1} * {n2} = {n1*n2}")
    elif sym == "/":
        if n2 == 0:
            print("Error")
        else:
            print(f"Result: {n1} / {n2} = {n1/n2}")
    else:
        print("Invalid operation")

    choice = input("Do you want to continue?(yes/no):")
    choice = choice.lower()