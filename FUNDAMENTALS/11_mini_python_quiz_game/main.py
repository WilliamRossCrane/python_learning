# 11 Mini Python Quiz Game
# This project combines many Python basics into one small program.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# A function is a reusable block of code.
# This function prints the title of the program.

def show_title():
    print("MINI PYTHON QUIZ GAME")
    print("---------------------")
    print("Answer the questions and see your final score.")
    print()


# This function asks one quiz question.
# question_data is a dictionary with a question and an answer.

def ask_question(question_data):
    print(question_data["question"])

    # input() lets the user type an answer.
    user_answer = input("Your answer: ")

    # lower() makes the answer lowercase.
    # strip() removes extra spaces at the start and end.
    # This helps avoid small typing problems.
    user_answer = user_answer.lower().strip()

    correct_answer = question_data["answer"].lower().strip()

    # This checks if the user's answer matches the correct answer.
    if user_answer == correct_answer:
        print("Correct!")
        print()
        return True
    else:
        print("Not quite.")
        print(f"The correct answer was: {question_data['answer']}")
        print()
        return False


# This is a list of dictionaries.
# The list stores all quiz questions.
# Each dictionary stores one question and one answer.

questions = [
    {
        "question": "What function shows text in the terminal?",
        "answer": "print"
    },
    {
        "question": "What symbol starts a comment in Python?",
        "answer": "#"
    },
    {
        "question": "What data type is used for text?",
        "answer": "string"
    },
    {
        "question": "What function lets the user type into a program?",
        "answer": "input"
    },
    {
        "question": "What keyword is used to create a function?",
        "answer": "def"
    }
]


# Start the program by showing the title.

show_title()


# This variable stores the player's score.
# It starts at 0.

score = 0


# A for loop goes through each question in the questions list.

for question in questions:
    was_correct = ask_question(question)

    # If the answer was correct, add 1 to the score.
    if was_correct:
        score = score + 1


# After the loop finishes, the quiz is over.

print("QUIZ COMPLETE")
print("-------------")


# len() tells us how many questions are in the list.

total_questions = len(questions)

print(f"Your final score was {score} out of {total_questions}.")


# Give feedback based on the score.

if score == total_questions:
    print("Amazing! You got every question correct.")
elif score >= 3:
    print("Good work! You are building solid Python knowledge.")
else:
    print("Keep practising. Every mistake helps you learn.")


print()
print("This quiz used lists, dictionaries, loops, functions, input, and if statements.")
print("That means you have started combining Python basics into real programs.")