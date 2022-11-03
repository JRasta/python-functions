"""
GUI version of OTT Settler
"""
print("Enter Odds or 'E' to exit")
while True:
    first_input = input("Enter your odds: ")

    if first_input.strip() == 'E' or first_input.strip() == 'e':
        break
    else:
        x, y = first_input.split("/")
        int(x), int(y)
        odds_total = x / y
        print(odds_total)


