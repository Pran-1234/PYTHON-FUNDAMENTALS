# Define a string
my_string = "Hello, world!"

# 1. Slice the string from index 1 to 5 (not including index 5)
substring_1 = my_string[1:5]

# 2. Slice the string from the beginning up to index 5 (not including index 5)
substring_2 = my_string[:5]

# 3. Slice the string from index 7 to the end
substring_3 = my_string[7:]

# 4. Slice the string with step 2 (every second character from index 0)
substring_4 = my_string[::2]

# 5. Slice the string with negative indexing (from the last character)
substring_5 = my_string[-5:]

# 6. Slice the string in reverse order
substring_6 = my_string[::-1]

# Print the results
print("Slice from index 1 to 5:", substring_1)
print("Slice from the beginning to index 5:", substring_2)
print("Slice from index 7 to the end:", substring_3)
print("Every second character from index 0:", substring_4)
print("Last 5 characters:", substring_5)
print("String in reverse order:", substring_6)
