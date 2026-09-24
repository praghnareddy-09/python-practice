# G. Lists (42–61)
# Create a list of 5 numbers and print the first and last elements.
list_of_numbers = [10, 20, 30, 40, 50]
print(f"First element: {list_of_numbers[0]}")
print(f"Last element: {list_of_numbers[-1]}") 

# Add a new element to a list.
list_of_numbers.append(60)  

# Remove an element from a list.
list_of_numbers.remove(30)  # Removes the first occurrence of 30

# Create a list of 4 colors and print its length.
colors = ["red", "blue", "green", "yellow"]
print(f"Length of colors list: {len(colors)}")

# Check if "red" exists in a list of colors.
if "red" in colors:
    print("Red is in the list.")

# Print the second to fourth elements of a list.
print(f"Second to fourth elements: {list_of_numbers[1:4]}")

# Print the last 3 elements of a list.
print(f"Last 3 elements: {list_of_numbers[-3:]}")

# Store 5 names in a list and print the name at index 2.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"Name at index 2: {names[2]}")

# Reverse a list.
list_of_numbers.reverse()
print(f"Reversed list: {list_of_numbers}")

# Replace the second element of a list with "Python".
list_of_numbers[1] = "Python"
print(f"List after replacement: {list_of_numbers}")

# Create a list of 5 numbers. Check if a number entered by the user exists in the list.
user_number = int(input("Enter a number to check: "))
if user_number in list_of_numbers:
    print("Number found in the list.")
else:
    print("Number not found in the list.")

# Store 5 subjects in a list. Ask the user to enter a subject name. If it exists, print "Found", else "Not Found".
subjects = ["Math", "Science", "English", "History", "Geography"]
user_subject = input("Enter a subject name: ")
if user_subject in subjects:
    print("Found")
else:
    print("Not Found")

# Create a list of marks. If the average is ≥ 50, print "Pass", else "Fail".
marks = [60, 70, 80, 90, 50]
average = sum(marks) / len(marks)
if average >= 50:
    print("Pass")
else:
    print("Fail")

# Check if the first and last elements of a list are equal.
if list_of_numbers[0] == list_of_numbers[-1]:
    print("First and last elements are equal.")
else:
    print("First and last elements are not equal.")

# Create a list of strings. Print "Contains Python" if "Python" is in the list.
strings = ["Java", "C++", "Python", "JavaScript"]
if "Python" in strings:
    print("Contains Python")

# Create a list of 5 numbers. Print the largest and smallest numbers.
print(f"Largest number: {max(list_of_numbers)}")
print(f"Smallest number: {min(list_of_numbers)}")

# Count how many times "apple" appears in a list.
fruits = ["apple", "banana", "apple", "orange", "apple"]
print(f"Number of apples: {fruits.count('apple')}")

# Store 5 numbers in a list. Print only the even numbers.
even_numbers = [num for num in list_of_numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")
# Check if a list is empty.
if not list_of_numbers:
    print("The list is empty.")
    
# Create a list of 5 numbers. If all numbers are positive, print "All Positive", else "Contains Negative".
if all(num > 0 for num in list_of_numbers):
    print("All Positive")
else:
    print("Contains Negative")

# H. Mixed Concept Questions (62–70)
# Store 5 numbers in a tuple. Check if the number 10 is present.
numbers_tuple = (5, 10, 15, 20, 25)
if 10 in numbers_tuple:
    print("Number 10 is present in the tuple.")

# Create a dictionary with student names as keys and marks as values. Check if "Rahul" is in the dictionary.
student_dict = {"Alice": 85, "Bob": 90, "Rahul": 78}
if "Rahul" in student_dict:
    print("Rahul is in the dictionary.")

# Take a string input and check if it contains "Python".
user_string = input("Enter a string: ")
if "Python" in user_string:
    print("The string contains 'Python'.")

# Ask the user for two numbers. Print "Equal" if they are equal, "First is greater" if the first is larger, else "Second is greater".
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 == num2:
    print("Equal")
elif num1 > num2:
    print("First is greater")
else:
    print("Second is greater")

# Check if a number is divisible by 2 OR 5.
user_number = int(input("Enter a number: "))
if user_number % 2 == 0 or user_number % 5 == 0:
    print("The number is divisible by 2 or 5.")

# Create a dictionary with 3 employees and their salaries. Print the salary of the employee with the highest pay.
employee_salaries = {"Alice": 50000, "Bob": 60000, "Charlie": 55000}
highest_paid_employee = max(employee_salaries, key=employee_salaries.get)   
print(f"Highest paid employee: {highest_paid_employee}")    

# Check if a string entered by the user contains both "a" and "b".
user_string = input("Enter a string: ")
if "a" in user_string and "b" in user_string:
    print("The string contains both 'a' and 'b'.")

# Store 5 subjects in a tuple. Ask the user to enter a subject name. If it exists, print "Subject Found", else "Not Found".
subjects = ("Math", "Science", "English", "History", "Geography")
user_subject = input("Enter a subject name: ")
if user_subject in subjects:
    print("Subject Found")
else:
    print("Not Found")

# Check if a number entered by the user is both even and between 10 and 50.
user_number = int(input("Enter a number: "))
if user_number % 2 == 0 and 10 <= user_number <= 50:
    print("The number is even and between 10 and 50.")
else:
    print("The number does not meet both criteria.")

# I. Strings – Built-in Practice (71–80)
# Convert a string to uppercase.
user_string = input("Enter a string: ")
print(user_string.upper())

# Convert a string to lowercase.
print(user_string.lower())

# Remove extra spaces from a string.
print(user_string.strip())

# Replace one word in a string with another.
string = "I love programming in Python."
new_string = string.replace("Python", "Java")   
# Split a string into a list of words.
words = string.split()
# Join a list of words into a single string.
joined_string = " ".join(words)
# Count how many times a letter appears in a string.
letter_count = string.count("a")
# Find the position of a character in a string.
position = string.find("Python")
# Check if a string contains only letters and numbers.
is_alphanumeric = string.isalnum()
# Check if a string contains only digits.
is_digit = string.isdigit()

# J. Lists – Built-in Practice (81–90)
# Add an element to the end of a list.
my_list = [1, 2, 3]
my_list.append(4)
# Add multiple elements to a list at once.
my_list.extend([5, 6, 7])
# Insert an element at a specific position in a list.
my_list.insert(0, 0)
# Remove a specific element from a list.
my_list.remove(3)
# Remove the last element from a list.
my_list.pop()
# Arrange the elements of a list in ascending order.
my_list.sort()

# Reverse the order of elements in a list.
my_list.reverse()

# Find the position of an element in a list.
position = my_list.index(5)

# Count how many times a number appears in a list.
count = my_list.count(5)

# Remove all elements from a list.
my_list.clear()

# K. Dictionaries – Built-in Practice (91–100)
# Print all keys of a dictionary.
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys())

# Print all values of a dictionary.
print(my_dict.values())

# Print all key-value pairs of a dictionary.
print(my_dict.items())

# Access the value of a key safely.
value = my_dict.get("a")

# Add a new key-value pair to a dictionary.
my_dict["d"] = 4

# Remove a specific key from a dictionary.
del my_dict["a"]

# Remove the last inserted item from a dictionary.
my_dict.popitem()

# Check if a key exists in a dictionary.
if "a" in my_dict:
    print("Key exists.")

# Create a dictionary with given keys and the same default value.
keys = ["a", "b", "c"]
default_value = 0
my_dict = dict.fromkeys(keys, default_value)

# Make a copy of a dictionary.
my_dict_copy = my_dict.copy()
