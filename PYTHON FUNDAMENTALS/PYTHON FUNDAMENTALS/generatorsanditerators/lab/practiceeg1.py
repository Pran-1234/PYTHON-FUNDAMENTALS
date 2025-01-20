def generate_even_numbers():
    num = 0
    while num < 20:  # We want the first 10 even numbers (0, 2, 4, ..., 18)
        yield num
        num += 2

# Example usage:
even_numbers = generate_even_numbers()
for number in even_numbers:
    print(number)
