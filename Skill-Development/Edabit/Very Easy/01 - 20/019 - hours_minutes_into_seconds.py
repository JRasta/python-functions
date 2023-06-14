"""
Convert Hours and Minutes into Seconds

Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them
"""

def convert(h, m):
    h_to_s = h * 60 * 60
    m_to_s = m * 60

    result = h_to_s + m_to_s
    print(result)


convert(1, 3)
convert(2, 0)
convert(0, 0)
