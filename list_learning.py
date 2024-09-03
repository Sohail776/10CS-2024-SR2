'''
sports = ["Basketball"]

print(sports)
print(type(sports))
print(len(sports))
print(sports[0])
print(sports[-1])
print(sports[-2])
print(sports[0:3])

for sport in sports:
    print(type(sport))
    print(sport)
'''
repeat ="yes"
sports = ["Basketball"]
while repeat == "yes":
    new_sport = input("Enter your favourite sport: ") # Get user input
    if new_sport:
        sports.append(new_sport)
        print("Updated sports list: ", sports)
    else:
        print("No new sport added. ")
        print("Sports list:") # 1. Fix this line

    for i, sport in enumerate(sports): # loop through the sports list with index
        print(f"Sport {i+1}: {sport}") # Print the index and sport

    repeat = input ("Do you want to add another sport? (yes/no): ").strip().lower()
print("Existing the program.")
# Suggested Improvements


