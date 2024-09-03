#!/usr/bin/env python
# coding: utf-8

# # Quiz on Python Basics, Control Flow, Functions, Lists, and File I/O
# 
# This quiz covers topics from weeks 1, 2, 3, and file I/O from week 4. Answer each question and run the corresponding cell to check your answer.

# In[ ]:


# Import necessary libraries
import json


# ### Question 1: Print "Hello, World!"
# 
# Write a Python program that prints "Hello, World!".

# In[ ]:


# Your code here
def q1():
    pass

print(q1())

# Test Function
def test_q1():
    assert q1() == "Hello, World!", "The output should be 'Hello, World!'"
    print("Question 1 is correct!")

test_q1()


# ### Question 2: Add a comment to the following code
# 
# Add a comment to the following code: `print("Hello, World!")`

# In[1]:


# Your code here
print("Hello, World!")

# Test Function
def test_q2():
    # Check if a comment is added (this is more of a manual check)
    print("Check if a comment is added above the print statement.")
    print("Question 2 is correct if a comment is present.")

test_q2()


# ### Question 3: Perform arithmetic operations
# 
# Write a program that adds, subtracts, multiplies, and divides two numbers.

# In[ ]:


# Your code here
def arithmetic_operations(a, b):
    pass

print(arithmetic_operations(8, 2))

# Test Function
def test_q3():
    assert arithmetic_operations(8, 2) == (10, 6, 16, 4.0), "The arithmetic operations should return correct results"
    print("Question 3 is correct!")

test_q3()


# ### Question 4: Variable declaration and printing
# 
# Write a program that declares variables and prints their values.

# In[ ]:


# Your code here
def variable_declaration():
    pass

print(variable_declaration())

# Test Function
def test_q4():
    assert variable_declaration() == ("Alice", 25), "The variables should be correctly declared and printed"
    print("Question 4 is correct!")

test_q4()


# ### Question 5: Input and output
# 
# Write a program that takes the user's name as input and prints a greeting.

# In[ ]:


# Your code here
def greet_user(name):
    pass

print(greet_user("Bob"))

# Test Function
def test_q5():
    assert greet_user("Bob") == "Hello, Bob!", "The greeting should be correctly printed"
    print("Question 5 is correct!")

test_q5()


# ### Question 6: String length
# 
# Write a program that takes a string input and prints its length.

# In[ ]:


# Your code here
def string_length(s):
    pass

print(string_length("Hello, World!"))

# Test Function
def test_q6():
    assert string_length("Hello, World!") == 13, "The length of the string should be correctly calculated"
    print("Question 6 is correct!")

test_q6()


# ### Question 7: String manipulation
# 
# Write a program that converts a string to uppercase and prints it.

# In[ ]:


# Your code here
def string_to_upper(s):
    pass

print(string_to_upper("hello"))

# Test Function
def test_q7():
    assert string_to_upper("hello") == "HELLO", "The string should be correctly converted to uppercase"
    print("Question 7 is correct!")

test_q7()


# ### Question 8: String concatenation
# 
# Write a program that concatenates two strings.

# In[ ]:


# Your code here
def concatenate_strings(s1, s2):
    pass

print(concatenate_strings("Hello, ", "World!"))

# Test Function
def test_q8():
    assert concatenate_strings("Hello, ", "World!") == "Hello, World!", "The strings should be correctly concatenated"
    print("Question 8 is correct!")

test_q8()


# # Week 2: Control Flow

# ### Question 9: If statements
# 
# Write a program that checks if a number is positive, negative, or zero.

# In[ ]:


# Your code here
def check_number(n):
    pass

print(check_number(5))
print(check_number(-3))
print(check_number(0))

# Test Function
def test_q9():
    assert check_number(5) == "Positive", "The number should be correctly identified as positive"
    assert check_number(-3) == "Negative", "The number should be correctly identified as negative"
    assert check_number(0) == "Zero", "The number should be correctly identified as zero"
    print("Question 9 is correct!")

test_q9()


# ### Question 10: Logical operators
# 
# Write a program that checks if a number is within a specific range.

# In[ ]:


# Your code here
def in_range(n, start, end):
    pass

print(in_range(5, 1, 10))
print(in_range(15, 1, 10))

# Test Function
def test_q10():
    assert in_range(5, 1, 10) == True, "The number should be within the range"
    assert in_range(15, 1, 10) == False, "The number should be outside the range"
    print("Question 10 is correct!")

test_q10()


# ### Question 11: For loop
# 
# Write a for loop that prints numbers from 1 to 10.

# In[ ]:


# Your code here
def print_numbers():
    pass

print(print_numbers())

# Test Function
def test_q11():
    assert print_numbers() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "The numbers should be correctly printed"
    print("Question 11 is correct!")

test_q11()


# ### Question 12: While loop
# 
# Write a while loop that prints "Hello" 5 times.

# In[ ]:


# Your code here
def print_hello():
    pass

print(print_hello())

# Test Function
def test_q12():
    assert print_hello() == ["Hello", "Hello", "Hello", "Hello", "Hello"], "The word 'Hello' should be printed 5 times"
    print("Question 12 is correct!")

test_q12()


# ### Question 13: Nested loops
# 
# Write a program that prints a multiplication table.

# In[ ]:


# Your code here
def multiplication_table():
    pass

print(multiplication_table())

# Test Function
def test_q13():
    assert multiplication_table()[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "The first row should be correct"
    assert multiplication_table()[9] == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "The last row should be correct"
    print("Question 13 is correct!")

test_q13()


# ### Question 14: Nested conditionals
# 
# Write a program that prints prime numbers between 1 and 100.

# In[ ]:


# Your code here
def prime_numbers():
    pass

print(prime_numbers())

# Test Function
def test_q14():
    assert prime_numbers() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], "The prime numbers should be correctly identified"
    print("Question 14 is correct!")

test_q14()


# # Week 3: Functions and Lists

# ### Question 15: Define a function
# 
# Write a function that takes two numbers and returns their sum.

# In[ ]:


# Your code here
def add(a, b):
    pass

print(add(3, 4))

# Test Function
def test_q15():
    assert add(3, 4) == 7, "The function should correctly add two numbers"
    print("Question 15 is correct!")

test_q15()


# ### Question 16: Call a function
# 
# Write a function that checks if a number is even or odd and call it.

# In[ ]:


# Your code here
def is_even(n):
    pass

print(is_even(4))
print(is_even(5))

# Test Function
def test_q16():
    assert is_even(4) == True, "The function should return True for even numbers"
    assert is_even(5) == False, "The function should return False for odd numbers"
    print("Question 16 is correct!")

test_q16()


# ### Question 17: Create a list
# 
# Write a program that creates a list of favorite movies and prints it.

# In[ ]:


# Your code here
def favorite_movies():
    pass

print(favorite_movies())

# Test Function
def test_q17():
    assert favorite_movies() == ["Inception", "The Matrix", "Interstellar"], "The list of favorite movies should be correctly created"
    print("Question 17 is correct!")

test_q17()


# ### Question 18: Use list methods
# 
# Write a program that adds a new movie to the list and prints the updated list.

# In[ ]:


# Your code here
def add_movie():
    pass

print(add_movie())

# Test Function
def test_q18():
    assert add_movie() == ["Inception", "The Matrix", "Interstellar", "The Dark Knight"], "The new movie should be added to the list"
    print("Question 18 is correct!")

test_q18()


# ### Question 19: Iterate over a list
# 
# Write a program that prints each item in a list of numbers.

# In[ ]:


# Your code here
def print_list(numbers):
    pass

print(print_list([1, 2, 3, 4, 5]))

# Test Function
def test_q19():
    assert print_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "The numbers should be correctly printed"
    print("Question 19 is correct!")

test_q19()


# ### Question 20: List slicing
# 
# Write a program that slices a list and prints the first three items.

# In[ ]:


# Your code here
def slice_list(lst):
    pass

print(slice_list([1, 2, 3, 4, 5]))

# Test Function
def test_q20():
    assert slice_list([1, 2, 3, 4, 5]) == [1, 2, 3], "The first three items should be correctly sliced"
    print("Question 20 is correct!")

test_q20()


# ### Question 21: Nested loops with lists
# 
# Write a program that prints a 2D list in a tabular format.

# In[ ]:


# Your code here
def print_2d_list(lst):
    pass

print(print_2d_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# Test Function
def test_q21():
    expected_output = "1\t2\t3\t\n4\t5\t6\t\n7\t8\t9\t\n"
    assert print_2d_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == expected_output, "The 2D list should be printed in a tabular format"
    print("Question 21 is correct!")

test_q21()


# ### Question 22: List comprehension
# 
# Write a program that uses list comprehension to create a list of squares of numbers from 1 to 10.

# In[ ]:


# Your code here
def squares_list():
    pass

print(squares_list())

# Test Function
def test_q22():
    assert squares_list() == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], "The list of squares should be correctly created"
    print("Question 22 is correct!")

test_q22()


# ### Question 23: List methods
# 
# Write a program that sorts a list of numbers in ascending order.

# In[ ]:


# Your code here
def sort_list(lst):
    pass

print(sort_list([3, 1, 4, 1, 5, 9]))

# Test Function
def test_q23():
    assert sort_list([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9], "The list should be correctly sorted"
    print("Question 23 is correct!")

test_q23()


# # Week 4: File I/O

# ### Question 24: Read from a file
# 
# Write a program that reads the contents of a file and prints them.

# In[ ]:


# Your code here
def read_file(filename):
    pass

# Create a sample file for testing
with open("sample.txt", "w") as file:
    file.write("Hello, World!")

print(read_file("sample.txt"))

# Test Function
def test_q24():
    assert read_file("sample.txt") == "Hello, World!", "The file content should be correctly read"
    print("Question 24 is correct!")

test_q24()


# ### Question 25: Write to a file
# 
# Write a program that writes user input to a file.

# In[ ]:


# Your code here
def write_file(filename, content):
    pass

print(write_file("output.txt", "This is a test."))

# Test Function
def test_q25():
    assert write_file("output.txt", "This is a test.") == "Write successful", "The content should be correctly written to the file"
    with open("output.txt", "r") as file:
        assert file.read() == "This is a test.", "The file content should match the input"
    print("Question 25 is correct!")

test_q25()


# ### Question 26: Append to a file
# 
# Write a program that appends a new line of text to a file and reads the updated file.

# In[ ]:


# Your code here
def append_file(filename, content):
    pass

print(append_file("output.txt", "Appending this line."))

# Test Function
def test_q26():
    updated_content = append_file("output.txt", "Appending this line.")
    assert "Appending this line." in updated_content, "The new line should be appended to the file"
    print("Question 26 is correct!")

test_q26()


# ### Question 27: Read file into a list
# 
# Write a program that reads the lines of a file into a list.

# In[ ]:


# Your code here
def read_file_to_list(filename):
    pass

print(read_file_to_list("output.txt"))

# Test Function
def test_q27():
    assert read_file_to_list("output.txt") == ["This is a test.\n", "Appending this line.\n", "Appending this line.\n"], "The lines should be correctly read into a list"
    print("Question 27 is correct!")

test_q27()


# ### Question 28: Write list to a file
# 
# Write a program that writes the elements of a list to a file.

# In[ ]:


# Your code here
def write_list_to_file(filename, lst):
    pass

print(write_list_to_file("list_output.txt", ["Line 1", "Line 2", "Line 3"]))

# Test Function
def test_q28():
    assert write_list_to_file("list_output.txt", ["Line 1", "Line 2", "Line 3"]) == "Write successful", "The list should be correctly written to the file"
    with open("list_output.txt", "r") as file:
        assert file.read() == "Line 1\nLine 2\nLine 3\n", "The file content should match the list items"
    print("Question 28 is correct!")

test_q28()


# ### Question 29: File I/O with exception handling
# 
# Write a program that handles file not found errors when reading a file.

# In[ ]:


# Your code here
def read_file_with_exception_handling(filename):
    pass

print(read_file_with_exception_handling("non_existent_file.txt"))

# Test Function
def test_q29():
    assert read_file_with_exception_handling("non_existent_file.txt") == "File not found", "The function should handle file not found errors"
    print("Question 29 is correct!")

test_q29()


# ### Question 30: File I/O with dictionaries
# 
# Write a program that reads student names and grades from a file into a dictionary.

# In[ ]:


# Your code here
def read_grades_to_dict(filename):
    pass

# Create a sample file for testing
with open("grades.txt", "w") as file:
    file.write("Alice,90\nBob,85\nCharlie,95")

print(read_grades_to_dict("grades.txt"))

# Test Function
def test_q30():
    assert read_grades_to_dict("grades.txt") == {"Alice": 90, "Bob": 85, "Charlie": 95}, "The student names and grades should be correctly read into a dictionary"
    print("Question 30 is correct!")

test_q30()

