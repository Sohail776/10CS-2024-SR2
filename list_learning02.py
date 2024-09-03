
import os
# Define the file path
file_path = 'sports01.txt'

# Initialize the sports list


if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        sports = [line.strip() for line in file.readlines()]


repeat = "yes"
while repeat== "yes":
# Append the new sport if provided
    new_sport = input("Enter your favourite sport: ")



    if new_sport:
        if new_sport in sports:
            print(f"{new_sport} is already in the list.")
        else:
            sports.append(new_sport)
            print("Updated sports list:", sports)

    else:
        print("No new sport added.")


    with open(file_path, 'w') as file:
        for sport in sports:



    print("Sports list:")
    for i, sport in enumerate(sports):
        print(f"Sport {i+1}: {sport}")

    repeat = input("Do you want to add more sports? (yes/no) ").strip()
print("Existing the program.")
