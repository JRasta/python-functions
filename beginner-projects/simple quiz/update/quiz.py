"""
Author: J. Smith
Date: 28/10/2022
Title: Simple Quiz
Description: A simple quiz created from a csv file
"""

import time
import random

# variables
question_numbers = []
sample_list = []
question_list = []
question_count = 0
i = 0
score = 0
choices = ['a', 'b', 'c', 'd']
csv_file = 'C:\\Users\\jsmit638\\PycharmProjects\\pythonSnippets\\beginner-projects\\simple quiz\\update\\data.csv'

def get_question(number):
    """
    Pulls the question from the CSV file of questions
    :param number: number of question selected from CSV file
    :return: question, options & answer
    """

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        total_lines = csvfile.readlines()
        qtion = total_lines[number[0]]

    csvfile.close()
    return qtion

def create_question(details):
    """
    Formats the question to be shown to the user
    :param details: question, options & answer
    :return: answer
    """

    qst, opt1, opt2, opt3, opt4, ans = details.split(',')
    print()
    print(f'{qst}')
    print(f'a) {opt1}')
    print(f'b) {opt2}')
    print(f'c) {opt3}')
    print(f'd) {opt4}')
    return ans

def create_quiz_template():
    """
    Populates the quiz
    :return: full quiz
    """

    for no_of_questions in range(1, 51):
        sample_list.append(no_of_questions)

    for questions in range(1, 11):
        question_numbers.append(random.sample(sample_list, 1))

    for question_number in question_numbers:
        question_details = get_question(question_number)
        question_list.append(question_details)

def check_answer(c, a):
    """
    Validates the answer given by the user
    :param c: user's choice
    :param a: correct answer
    :return: update to the score
    """

    global score

    if c == 'a':
        temp_ans = x[1].strip()
        if temp_ans == a:
            score += 1
        else:
            score += 0

    if c == 'b':
        temp_ans = x[2].strip()
        if temp_ans == a:
            score += 1
        else:
            score += 0

    if c == 'c':
        temp_ans = x[3].strip()
        if temp_ans == a:
            score += 1
        else:
            score += 0

    if c == 'd':
        temp_ans = x[4].strip()
        if temp_ans == a:
            score += 1
        else:
            score += 0


create_quiz_template()

# Collect user details
print('Enter your name')
name = input('>>> ')
print('\nOK, ' + name + ', let\'s get started.')
time.sleep(2)

# Play quiz
for question in question_list:
    x = question_list[i].split(',')
    answer = x[5].strip()
    question_ans = create_question(question_list[i]).strip()
    choice = input('>>> ').lower()
    while True:
        if choice not in choices:
            print('Wrong input. Please try again')
            choice = input('>>> ').lower()
        else:
            break
    check_answer(choice, question_ans)
    i += 1

print(f'\n{name}, your final score is {score}/10')
