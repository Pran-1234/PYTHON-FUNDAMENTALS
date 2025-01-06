
import math  

# 2. Main Program Execution
if __name__ == "__main__":
    # 3. User Input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

  
    print(f"Addition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    
    
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Cannot divide by zero")
