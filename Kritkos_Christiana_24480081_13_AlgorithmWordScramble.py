import random
from random import shuffle
from random import choice
import tkinter as tk
from tkinter import *

# Declaration of Tkinter variable
# required by Tkinter classes
root = tk.Tk()  # initialise tkinter module - create root widget
root.title("Algorithm Word Jumble") # set title of main window
root.iconbitmap("c:/gui/code.ico")
root.minsize(850, 650)
label = tk.Label(root, text="Hello Player! Welcome to Algorithm Word Jumble!")
label.pack()
score = 0

# Word list to be used in the game
terms = ["ALGORITHMS", "CATEGORIES", 'CLASSIFICATIONS', "CODES", "DATA", "DIRECTIONS", "INFORMATION", "OPERATIONS",
         "PARAMETERS", "PATTERNS", "PROCESSING", "PROFILING", "SYSTEMS", "VALUE"]

# main game
my_label = Label(root, text="", font=("Arial", 52))
my_label.pack()

def shuffler():
    # clear answer Box
    # pick a random term from list
    global word
    word = choice(terms)
    my_label.config(text=word)

    # making a python list
    # Break apart our chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)

    # turn shuffled list into a word
    global shuffled_word
    shuffled_word = " "
    #create loop - loop through terms list and take every letter and add onto it
    for letter in break_apart_word:
        shuffled_word += letter

    # print shuffled word
    # shuffling and outputting on the screen
    my_label.config(text=shuffled_word)

# creating a score function
def update():
    global score
    score = 0
    if answer_label == correct:
        score = score + 1
        scoreLabel.config(text="Your Score: " + str(score))

# create answer function
def answer():
    global score
    if word == entry_answer.get():
        answer_label.config(text="Correct! You got 1 point!")
        score += 1
        scoreLabel.config(text="Your Score: " + str(score))
    else:
        answer_label.config(text="Sorry that's not quite right! Try again!")

# run shuffler
# create entry boxes for players to type in answers
entry_answer = Entry(root, font=("Arial", 26))
entry_answer.pack(pady=20)

# create label to keep track of score
scoreLabel = Label(root, text="Your Score: " + str(score), font=("Arial", 26)) # create string to make 1 text
scoreLabel.place(x=25, y=25) # place score in upper left corner
scoreLabel. pack()

# create shuffle button - will shuffle and pick a different word every time
my_button = Button(root, text="Pick A Word", command=shuffler)
my_button.pack(pady=20)

# create answer button
# place button in route and have text equal shuffled word
answer_button = Button(root, text="Answer", command=answer)
answer_button.pack(pady=20)

answer_label = Label(root, text="", font=("Arial", 26))
answer_label.pack(pady=40)

root.mainloop()