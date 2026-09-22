print('Hello')
print("Your Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI")

website = input("Enter website: ")
website = "datawithbaraa.com"
print(f"info@{website}"), print("info@",website)
print(f"support@{website}")
print(f"www.{website}")

text = "hi"
number = 5
print(text)
print(number)
print(type(text)) # type() function is used to get the data type 
                  # of a variable/value, so you know what kind of object it is.
print(type(number))
print(len(text))  # len() gives/returns the total count of items insode a value, so it can be used to get the length of a string, list, tuple, etc.
print(len(str(number)))
# print(len(number)) # This will give an error because len() cannot be used on an integer. You need to convert the integer to a string first, as shown in the previous line.
print(text.upper()) # upper() method is used to convert a string to uppercase letters.
# number.upper() # This will give an error because upper() method cannot be used on an integer. 'int' object has no attribute 'upper'.
print(number.bit_length()) # method of <class int> # returns the length of a number in bits/binary representation. For example, the number 5 in binary is 101, which has a length of 3 bits.

age = 25
height = 5.9
name = "Baraa"
are_you_a_student = True
something = None
print(age, height, name, are_you_a_student, something)
print(type(age), type(height), type(name), type(are_you_a_student), type(something))
print(len(str(age)), len(str(height)), len(name), len(str(are_you_a_student)), len(str(something)))

