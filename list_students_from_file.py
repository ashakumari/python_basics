students = []

with open("students.txt") as f:
	for line in f:
		students.append(line.strip())

print(students)