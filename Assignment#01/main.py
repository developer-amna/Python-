# Python Fundamentals -Assignment 01

#Question 1:Variables and Data Types

#a) Create three variables: - Your name (string) - Your age (integer) - Your GPA (float) Print them
# with appropriate labels:

# Defining Variables
name="Amna"
age=21
GPA=3.75

# printing with labels
print("Name:",name)
print("Age:",age)
print("GPA:",GPA)

#Output:
#Name: Amna
#Age: 21
#GPA: 3.75

#  b) Conceptual Question: Why does Python allow reassigning a variable from a string to an
# integer, while C++ does not?

" " "
Python is dynamically typed, meaning the type of a variable is determined at runtime and can change. You can assign a string to a variable and later reassign an integer to it.
C++ is statically typed, so the type of a variable is fixed at compile time. Reassigning a different type causes a compilation error.

" " "
#Question 2: Input Handling

" " "
a) Write a program that asks the user for: - Favorite color - Favorite food - Favorite hobby Then print
 a complete sentence using the answers.
 " " "
 
 # Asking user for their favorites
favorite_color=input("Enter your favorite color: ")
favorite_food=input("Enter your favorite food: ")
favorite_hobby=input("Enter your favorite hobby: ")

# Constructing a sentence
print("Your favorite color is",{favorite_color},"you love eating",{favorite_food},"and enjoy",{favorite_hobby},"in your free time.")

#Output:
#Enter your favorite color: Blue
#Enter your favorite food: Pizza
#Enter your favorite hobby: Painting
#Your favorite color is {'Blue'} you love eating {'Pizza'} and enjoy {'Painting'} in your free time.

" " "  b) Conceptual Question: What happens if the user presses Enter without typing anything? Should
 your program crash, or should it handle empty input gracefully?
    
If the user presses Enter without typing anything, the input will be an empty string ("").
Your program shouldn't crash—it should handle empty input gracefully, perhaps by prompting again or using default values.
" " "

# Question 3: Type Casting

"""
 a) Ask the user for two numbers (input as strings). Convert them into integers and print: - Sum 
Difference - Product - Quotient.
"""
# Asking for two numbers as strings
num1_str=input("Enter first number:")
num2_str=input("Enter second number:")

# Converting to integers
num1=int(num1_str)
num2=int( num2_str)

# Performing operations
print("Sum: ",num1+num2)
print("Difference: ",num1-num2)
print("product: ",num1*num2)
print("Quotient: ",num1/num2)

#Output:
#Enter first number:10
#Enter second number:2
#Sum:  12
#Difference:  8
#product:  20
#Quotient:  5.0

"""
 Why does int("5.0") cause an error, while float("5.0") works?
 
 int("5.0") causes an error because "5.0" is a string representation of a float, not a valid integer string.
float("5.0") works because "5.0" is a valid float string.

"""

#Question 4: Comments

"""
a) Write a program that calculates the area of a rectangle using length × width. - Use single-line
 comments (#) to explain each step. - Use a multi-line docstring (""" ... """) at the top to describe the
 program.
"""

"""
This program calculates the area of a rectangle.
It takes length and width as input and multiplies them.
"""
# Taking input from user

length = float(input("Enter the length of the rectangle: "))  # Length input
width = float(input("Enter the width of the rectangle: "))    # Width input

# Calculating area
area = length * width  # Area formula

# Displaying result
print("Area of the rectangle:", area)

#Output:
#Enter the length of the rectangle: 5.0
#Enter the width of the rectangle: 3.0
#Area of the rectangle: 15.0

"""
 b) Conceptual Question: Do comments always make code better? Can excessive or poor
 comments make code worse? Explain briefly?
 
 Comments can improve code readability, especially for beginners or collaborators.
However, excessive or unclear comments can clutter the code and confuse readers.
Good comments explain why, not just what.
"""

#Question 5:Data Types & Checking


# a) Take a single input from the user. - Print the value. - Print its type using the type() function.

# Taking input
user_input = input("Enter something: ")

# Printing value and type
print("You entered:", user_input)
print("Type of input:", type(user_input))

#Output:
#Enter something: Hello
#You entered: Hello
#Type of input: <class 'str'>

"""
 If Python is dynamically typed, why do we sometimes still need to check
 the type of a variable?
 
 Even though Python is dynamically typed, type checking is useful when:
- Validating user input
- Performing type-specific operations
- Debugging complex code It helps ensure the program behaves as expected.
    """
    
    
              #End of Assignment 01