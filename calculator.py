def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print("Simple Calculator App")
    print("Available operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please try again.")
                continue

            print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")
        except Exception as e:
            print("An error occurred:", e)

        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
