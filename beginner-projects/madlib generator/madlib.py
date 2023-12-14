"""
PROJECT: Matlib generator
DATE: 12/12/2023
VIDEO: Tech With Tim - YT
LINK: https://www.youtube.com/watch?v=21FnnGKSRZo&t=142s

NB: Added the JSON my self, not in the tutorial video

DESCRIPTION: This story will have replaceable words like an adjective or a location or a weather condition
whatever it may be. What we will then do is will ask the user to give us all the different words.
Well, then inject them in the story and read the story back out to the user. Now, the first thing we're
going to need for this is a story.
"""
import json

# variables
story = ''
i = 0
words = set()  # cannot contain duplicates
start_word = -1
target_start = "<"
target_end = ">"
answers = {}


# read JSON file of stories
with open("stories.json", "r") as f:
    story_list = json.loads(f.read())
    num_of_stories = len(story_list)


# select a story to import
while True:
    story_num = input(f"Select which story you wish to import (1 - {num_of_stories}): ")
    if story_num.isdigit():
        story_num = int(story_num)
        break
    else:
        print("Invalid selection, please try again.")

for s in story_list:
    if s in str(story_num):
        story = story_list[s]


# find all <words> in the story
for i, char in enumerate(story):
    if char == target_start:
        start_word = i
    if char == target_end and start_word != -1:
        word = story[start_word : i+1]
        words.add(word)
        start_word = -1

print()

# store answers related to <words>
for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer


# replace <word> with answer
for word in words:
    story = story.replace(word, answers[word])


# print the final story
print(f"\n{story}")
