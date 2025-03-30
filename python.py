def get_user_input():
    """Get two numbers and a mathematical operation from the user."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    return num1, num2, operation

def perform_operation(num1, num2, operation):
    """Perform the specified mathematical operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
def main():
    """Run the simple calculator program."""
    num1, num2, operation = get_user_input()
    result = perform_operation(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    main()
    
