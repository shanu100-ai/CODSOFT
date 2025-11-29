print("=== SIMPLE CALCULATOR ===")

# Taking inputs
num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Calculation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        result = "Error: Division by zero!"
    else:
        result = num1 / num2
else:
    result = "Invalid operator!"

# Output
print("Result:", result)

# Window ko close hone se bachaye
input("\nPress Enter to exit...")