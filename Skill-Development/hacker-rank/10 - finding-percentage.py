"""The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Author: J. Smith
Date: May 2024
Lang: Pypy3
"""

if __name__ == '__main__':
    total = 0.00

    n = int(input("Enter number of Student marks: "))
    student_marks = {}

    # Create dictionary
    for _ in range(n):
        name, *line = input("Enter Student name following by marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # Query dictionary
    query_name = input("Which Student are you looking for avg: ")
    query_scores = student_marks.get(query_name)

    # Avg scores
    for x in query_scores:
        total += x
    avg = format(total / len(query_scores), ".2f")
    print(avg)
