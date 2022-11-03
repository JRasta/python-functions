"""
Letter Counter

Counts the letters within a given word
"""

def letter_counter(text):
    count = 0
    for _ in text:
        count += 1
    print(count)


letter_counter("halloween")
letter_counter("happy")
letter_counter("christmas")
letter_counter("birthday")
