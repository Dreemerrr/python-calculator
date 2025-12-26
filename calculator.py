print ("Welcome to the Calculator Program!")
print ("You can perform addition, subtraction, multiplication, and division.")
print ("Type 'exit' to end the program.")
print ("1. Addition (+)")
print ("2. Subtraction (-)")
print ("3. Multiplication (*)")
print ("4. Division (/)")

option = int(input("Please select an operation (1/2/3/4): "))
if option in (1, 2, 3, 4):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if option == 1:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif option == 2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif option == 3:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif option == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not possible.")
else:
    print("Invalid input. Please select a valid operation.")

if option == 'exit':
    print("Exiting the program. Goodbye!")

while True:
    # Get user input
    user_input = input("Enter something: ")

    # Check if the input is the exit command
    if user_input.lower() == 'exit':
        print("Exit command received. Quitting program.")
        break  # This breaks the while loop, ending the program

    # Otherwise, process the input as usual
    print(f"You typed: {user_input}")

print("Program terminated.")
