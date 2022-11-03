"""
Basketball Points

You are counting points for a basketball game, given the amount of 3-pointers scored and 2-pointers scored,
find the final points for the team and return that value ([2 -pointers scored, 3-pointers scored])
"""

def points(two_pts, three_pts):
    two_pts = two_pts * 2
    three_pts = three_pts * 3
    pts_total = two_pts + three_pts
    print(pts_total)


points(1, 1)
points(7, 5)
points(38, 8)
