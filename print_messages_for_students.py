names = input("Enter names of the students separated by comma: ").split(',')
assignments = input("Enter missing assignment count for each student separated by comma: ").split(',')
grades = input("Enter grade for each student separated by comma: ").split(',')


def print_message(name, assignment_count, grade):

	msg = """
	Hi {},

	This is a reminder that you have {} assignments left to submit
	before you can graduate. Your current grade is {} and can increase
	to {} if you submit all assignments before the due date.
	""".format(name.title(), assignment_count, grade, int(grade)+2*int(assignment_count))

	print(msg)

for name, assignment, grade in zip(names, assignments, grades):
	print_message(name, assignment, grade)