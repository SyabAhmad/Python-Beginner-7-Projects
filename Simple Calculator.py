def calculator():
    """
    A simple calculator that performs basic arithmetic operations.
    """
    print("Welcome to the calculator!")
    print("Enter 'q' to quit.")

    while True:
        # Get the user's input
        user_input = input("Enter an operation (+, -, *, /): ")

        # Quit if the user enters 'q'
        if user_input == 'q':
            print("Goodbye!")
            break

        # Get the operands
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Perform the operation
        if user_input == '+':
            result = num1 + num2
        elif user_input == '-':
            result = num1 - num2
        elif user_input == '*':
            result = num1 * num2
        elif user_input == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            else:
                result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            continue

        # Print the result
        print("The result is:", result)

calculator()