while True:
    try:
        num1 = float(input("enter first number: "))
        operator = input("enter an operator(+ - / * ): ")
        num2 = float(input("enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
        else:
            print("Invalid operator")
            continue  # Skip to the next iteration of the loop

        print(round(result, 3))

    except ValueError:
        print("Invalid input. Please enter valid numbers.")