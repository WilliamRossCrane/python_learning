# 12 Python Fundamentals Mini Assessment
# Student Version

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 student_assessment.py


# Assessment Task:
# Build a small Python learning report.
#
# Your program should:
# - ask the user for their name
# - ask the user for their year level
# - ask the user for a score out of 100
# - store skills in a list
# - store student information in a dictionary
# - use a function to create feedback
# - use if, elif, and else
# - print a clear final report


print("PYTHON FUNDAMENTALS MINI ASSESSMENT")
print("-----------------------------------")
print("Complete the program to create a student learning report.")
print()


# TODO 1:
# Ask the user for their name.
# Store the answer in a variable called student_name.

student_name = input("Enter student name: ")


# TODO 2:
# Ask the user for their year level.
# Store the answer in a variable called year_level.

year_level = input("Enter year level: ")


# TODO 3:
# Ask the user for their score out of 100.
# input() gives text, so use int() to turn it into a whole number.

score = int(input("Enter score out of 100: "))


# TODO 4:
# Add at least 5 Python skills to this list.

python_skills = [
    "print statements",
    "variables",
    "input"
]


# TODO 5:
# Create a dictionary called student.
# It should store:
# - name
# - year level
# - score

student = {
    "name": student_name,
    "year_level": year_level,
    "score": score
}


# TODO 6:
# Complete this function.
# The function should return feedback based on the score.
#
# Suggested rules:
# 90 or higher = Excellent understanding
# 70 or higher = Strong progress
# 50 or higher = Developing understanding
# below 50 = Needs more practice

def get_feedback(score):
    # Replace this starter feedback with your own if, elif, and else code.
    return "Feedback goes here."


# TODO 7:
# Store the feedback from the function in a variable.

feedback = get_feedback(score)


# TODO 8:
# Print a clear final report.

print()
print("STUDENT LEARNING REPORT")
print("-----------------------")

print(f"Name: {student['name']}")
print(f"Year Level: {student['year_level']}")
print(f"Score: {student['score']} out of 100")

print()
print("Python Skills Practised:")
print("------------------------")


# TODO 9:
# Use a for loop to print each skill in the python_skills list.

for skill in python_skills:
    print(f"- {skill}")


print()
print("Teacher Feedback:")
print("-----------------")
print(feedback)


print()
print("Assessment complete.")