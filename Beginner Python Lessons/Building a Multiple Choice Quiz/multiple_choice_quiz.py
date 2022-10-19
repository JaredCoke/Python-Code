# This is a sample Python script.
from question import Question
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are apples?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt) #gathers case insentive answers
        if str.lower(answer) == question.answer: #converts answers to lower case for easy comparision
            score += 1
    if score > 2: #need to count how many questions there are and return one less than max
        print("Oh yeah! You got " + str(score) + "/" + str(len(questions)) + " correct.")
    elif score > 0:
        print("Hmm... You got " + str(score) + "/" + str(len(questions)) + " correct.")
    else:
        print("Do better. You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)