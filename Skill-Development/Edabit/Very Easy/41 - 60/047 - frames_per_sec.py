"""
Frames Per Second

Create a function that returns the number of frames shown in a given number of minutes for a certain FPS
"""

def frames(f, m):
    fps = f * m * 60
    print(fps)


frames(1, 1)
frames(10, 1)
frames(10, 25)
