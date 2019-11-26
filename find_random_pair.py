# Use an import statement at the top
import random

names_file = "students.txt"
names_list = []

with open(names_file,'r') as names:
	for line in names:
		name = line.strip()
		names_list.append(name)

def generate_random_pair():
    random_words = random.sample(names_list, 2)
    return " - ".join(random_words)

# test your function
print(generate_random_pair())