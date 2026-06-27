# 12 Python Fundamentals Mini Assessment
# Teacher Answer Version

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 teacher_answer.py


# This answer file shows one possible completed version.
# Students may have different wording, variable names, or skills.
# That is okay if the program still works and uses the required concepts.


print("PYTHON FUNDAMENTALS MINI ASSESSMENT")
print("-----------------------------------")
print("This program creates a student learning report.")
print()


# input() asks the user a question.
# The user's answer is stored in a variable.

student_name = input("Enter student name: ")

year_level = input("Enter year level: ")


# input() gives us text first.
# int() changes the text into a whole number.
# We need a number so we can compare the score later.

score = int(input("Enter score out of 100: "))


# A list stores multiple values.
# This list stores the Python skills used in the assessment.

python_skills = [
    "print statements",
    "comments",
    "variables",
    "strings",
    "integers",
    "input",
    "lists",
    "dictionaries",
    "loops",
    "functions",
    "if, elif, and else"
]


# A dictionary stores related information using keys and values.
# This keeps the student's information together.

student = {
    "name": student_name,
    "year_level": year_level,
    "score": score
}


# A function is a reusable block of code.
# This function checks the score and returns feedback.

def get_feedback(score):
    if score >= 90:
        return "Excellent understanding. You are showing strong Python fundamentals."
    elif score >= 70:
        return "Strong progress. You understand many key Python basics."
    elif score >= 50:
        return "Developing understanding. Keep practising and testing your code."
    else:
        return "Needs more practice. Focus on small steps and ask for help when stuck."


# Call the function and store the returned feedback in a variable.

feedback = get_feedback(score)


# Print the final report.

print()
print("STUDENT LEARNING REPORT")
print("-----------------------")

print(f"Name: {student['name']}")
print(f"Year Level: {student['year_level']}")
print(f"Score: {student['score']} out of 100")


print()
print("Python Skills Practised:")
print("------------------------")


# A for loop repeats code for each item in the list.

for skill in python_skills:
    print(f"- {skill}")


print()
print("Teacher Feedback:")
print("-----------------")
print(feedback)


print()
print("Assessment complete.")