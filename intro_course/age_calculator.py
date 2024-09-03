import os
repeat = "yes"
while repeat == "yes":
    #Get the user to input their name
    #Get the user to input their birth year
    #Calculate the user's age

    name = input("What is your name?: ").strip()
    year = int(input("What year were you born in?: ").strip())
    age = int(2024-year)
    birthday = input("Have you had your birthday this year (Yes/No): ").lower().strip()
    if birthday == "no":
        age = age -1


    print(f"Hi {name}, you are {age} years old.")
    repeat = input("Would you like to run program again? (Yes/No): ").lower().strip()
    os.system('cls||clear')
# if repeat == "no": thank the user and exit the program
print("Thank you for using the age calculator.")