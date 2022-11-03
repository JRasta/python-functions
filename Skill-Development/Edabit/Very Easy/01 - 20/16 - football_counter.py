"""
Football Points

Create a function that takes the number of wins, draws and losses and calculates the
number of points a football team has obtained so far

* wins get 3 points
* draws get 1 point
* losses get 0 points
"""

def football_points(win, draw, loss):
    total_win = win * 3
    total_draw = draw * 1
    total_loss = loss * 0
    print(f'Total points: {total_win + total_draw + total_loss}')


football_points(3, 4, 2)
football_points(5, 0, 2)
football_points(0, 0, 1)
