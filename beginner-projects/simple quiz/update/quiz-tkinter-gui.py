"""
Author: J. Smith
Date: 23/11/2022
Title: Simple Quiz
Description: A simple quiz gui created from a JSON file
Inspired by GeeksforGeeks
"""

# imports
from tkinter import *
from tkinter import messagebox as mb
import json


class Quiz:
    def __init__(self):
        """Overall class that starts the initialization of the functionality and the GUI
        :param: none
        :return: GUI and GUI functionality
        """

        # set question to 0
        self.q_no = 0

        # creates GUI elements for title and question
        self.display_title()
        self.display_question()

        # opt_selected holds Tkinter integer variable
        self.opt_selected = IntVar()

        # creates the options for the current question
        self.opts = self.radio_buttons()

        # creates GUI element displaying the options for the current question
        self.display_options()

        # creates GUI elements for the buttons
        self.buttons()

        # no of questions in the data file
        self.data_size = len(question)

        # counter for number of correct answers
        self.correct = 0

    def display_result(self):
        """Displays the final result(s) when the quiz has finished
        :param: none
        :return: messagebox dialog
        """

        # calculates wrong count
        wrong_count = self.data_size - self.correct
        correct = f'Correct: {self.correct}'
        wrong = f'Wrong: {wrong_count}'

        # calculates percentage for correct answers
        score = int(self.correct / self.data_size * 100)
        result = f'Score: {score}%'

        # message box to display the result
        mb.showinfo('Result', f'{result}\n{correct}\n{wrong}')

    def check_answer(self, q_no):
        """Displays the final result(s) when the quiz has finished
        :param: the current question number
        :return: boolean
        """

        # if selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        """Checks the answer and then continues onto the next question, if there is one
        :param: none
        :return: none
        """

        # if answer is correct
        if self.check_answer(self.q_no):
            # increment correct
            self.correct += 1

        # incrementing q_no counter
        self.q_no += 1

        # if q_no size equal data_size
        if self.q_no == self.data_size:

            # if it is display the score
            self.display_result()

            # destroy gui
            gui.destroy()
        else:
            # show next question
            self.display_question()

            # show question options
            self.display_options()

    def buttons(self):
        """Add Next and Exit buttons to the GUI
        :param: none
        :return: none
        """
        # Next button used to move to the next question
        next_button = Button(gui, text='Next', command=self.next_btn,
                             width=10, bg='blue', fg='white', font=('ariel', 16, 'bold'))
        # place button
        next_button.place(x=350, y=380)

        # Quit button used to Quit the GUI
        quit_button = Button(gui, text='Quit', command=gui.destroy,
                             width=5, bg='black', fg='white', font=('ariel', 16, 'bold'))
        # place button
        quit_button.place(x=700, y=50)

    def display_options(self):
        """Add the possible answers to the GUI
        :param: none
        :return: none
        """
        val = 0

        # deselecting options
        self.opt_selected.set(val)

        # looping over options to be displayed
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        """Add the question to the GUI
        :param: none
        :return: none
        """

        # create a label for the question
        quest = Label(gui, text=question[self.q_no], width=60, font=('ariel', 16, 'bold'), anchor='w')
        # place question
        quest.place(x=40, y=100)

    @staticmethod
    def display_title():
        """Add the title to the GUI
        :param: none
        :return: none
        """

        # create a label for the title
        title = Label(gui, text='JCI Quiz', width=50, bg='green', fg='white', font=('ariel', 20, 'bold'))
        # place title
        title.place(x=0, y=2)

    def radio_buttons(self):
        """Add the possible answers to a list
        :param: none
        :return: 4x possible answers
        """

        # initialise list of options
        option_list = []

        # position of first option
        y_pos = 150

        # append options to the list
        while len(option_list) < 4:
            # create the radio button for the possible answer(s)
            radio_btn = Radiobutton(gui, text='', variable=self.opt_selected,
                                    value=len(option_list) + 1, font=('ariel', 14))
            # place button
            radio_btn.place(x=40, y=y_pos)

            # add button to the list
            option_list.append(radio_btn)

            # increment the y pos by 40
            y_pos += 40

        # return the list
        return option_list


# create GUI
gui = Tk()

gui.geometry('800x450')  # set the size of the GUI
gui.title('General Knowledge Quiz')  # set title of the GUI window

# get the data from the json file
with open('quiz_data.json') as f:
    data = json.load(f)

# set the question, options and answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# create an object of the Quiz class
quiz = Quiz()

# start the GUi
gui.mainloop()
