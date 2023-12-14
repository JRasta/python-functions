"""
PROJECT: Timed Math Challenge
DATE: 12/12/2023
VIDEO: Tech With Tim - YT
LINK: https://www.youtube.com/watch?v=21FnnGKSRZo&t=142s

DESCRIPTION: We want to randomly generate a bunch of different math questions. Ask the user.
Those questions and then not let them continue until they get it. Correct.
Well, then time. How long it takes them to answer all the questions
"""
import random
import time

OPERATORS = ["+", "-", "*"]  # ÷, X
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

wrong = 0

def generate_problem():
    # create components for problem
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    # create problem
    problem_expr = str(left) + operator + str(right)
    # get answer
    problem_answer = eval(problem_expr)
    return problem_expr, problem_answer

input("Press enter to start!")
print("---------------------")

start_time = time.time()  # start timer

for i in range(TOTAL_PROBLEMS):
    expr, ans = generate_problem()
    while True:
        user_guess = input(f"Problem #{str(i+1)}: {expr} = ")
        if user_guess == str(ans):
            break
    wrong += 1

end_time = time.time()  # stop timer

total_time = end_time - start_time
total_time = int(total_time)

print("---------------------")
print(f"Nice work! You finished in {total_time} seconds")