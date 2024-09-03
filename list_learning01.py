
import os
# Define the file path
file_path = 'sports01.txt'

# Initialize the sports list


def read_sports(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []



def write_sports(file_path, sports_list):
    with open(file_path,'w') as file:
        for sport in sports_list:
            file.write(f"{sport}\n")




repeat = "yes"
while repeat== "yes":
# Append the new sport if provided
    sports = read_sports(file_path)

    new_sport = input("Enter your favourite sport:").capitalize().strip()

    if new_sport:
        if new_sport in sports:
            print(f"{new_sport} is already in the list.")
        else:
            sports.append(new_sport)
            print("Updated sports list:", sports)

    else:
        print("No new sport added.")


    write_sports(file_path, sports)

    print("Sports list:")
    for i, sport in enumerate(sports):
        print(f"Sport {i+1}: {sport}")

    repeat = input("Do you want to add more sports? (yes/no) ").strip()
print("Existing the program.")
