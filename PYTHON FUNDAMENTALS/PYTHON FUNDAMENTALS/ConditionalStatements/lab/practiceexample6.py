
num = int(input("Enter a number: "))


if num <= 1:
    print(f"The number {num} is not a prime number.")

elif num == 2:
    print(f"The number {num} is a prime number.")

elif num % 2 == 0:
    print(f"The number {num} is not a prime number.")

elif num % 3 == 0:
    print(f"The number {num} is not a prime number.")

else:
    print(f"The number {num} is a prime number.")
