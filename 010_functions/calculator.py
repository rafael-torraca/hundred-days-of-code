def calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."
    
should_continue = True
while should_continue:
    first_number = int(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    second_number = int(input("Enter the second number: "))
    result = calculator(first_number, operator, second_number)
    print(f"The result is: {result}")
    continue_input = input("Do you want to perform another calculation? (yes/no): ")
    if continue_input.lower() != "yes":
        should_continue = False
        print("Goodbye!")
