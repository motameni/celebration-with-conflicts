import numpy as np
import random

# Define the lists of first names and last names
first_names = ["Ali", "Zahra", "Reza", "Sara", "Mohammad", "Fatemeh", "Hossein", "Maryam", "Mehdi", "Narges", "Hamed",
               "Roya"]
last_names = ["Ahmadi", "Hosseini", "Karimi", "Rahimi", "Hashemi", "Ebrahimi", "Moradi", "Mohammadi", "Rostami",
              "Fazeli", "Hosseinzadeh", "Niknam"]

# Combine the lists of first names and last names
names = []
while len(names) < 40:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    name = first_name + " " + last_name
    if name not in names:
        names.append(name)

# Create conflict matrix
conflict_matrix = np.zeros((24, 24))
conflict_count = 0
while conflict_count < 40:
    person1 = random.randint(0, 23)
    person2 = random.randint(0, 23)
    if person1 != person2 and conflict_matrix[person1, person2] == 0:
        conflict_matrix[person1, person2] = 1
        conflict_count += 1
        # conflict_matrix[person2, person1] = 1

# Print the conflict matrix
count = np.count_nonzero(conflict_matrix)
print(count)
print(conflict_matrix)
