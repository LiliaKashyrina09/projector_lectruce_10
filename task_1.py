import string
import random

file_summary = {}

for letter in string.ascii_uppercase:
    random_number = random.randint(1, 100)
    file_name = letter + ".txt"
    with open(file_name, "w") as file:
        file.write(str(random_number))
    file_summary[file_name] = random_number  

with open("summary.txt", "w") as summary:
    for name, number in file_summary.items():
        summary.write(f"{name}: {number}\n")