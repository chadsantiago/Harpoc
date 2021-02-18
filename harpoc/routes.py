from harpoc import app
from flask import Flask, render_template, url_for, request, redirect
import random


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':

        # open txt file
        with open("new.txt", "r") as file: 
            allText = file.read()

            # convert into a list
            words = list(map(str, allText.split()))
        
        # select 16 random items from the list
        new = random.sample(words, 16)

        # remove brackets and commas
        word_list = str('\n'.join(new))

        # create a new list for the initials
        initials = []

        # iterate through the list "new"
        for word in new:
            # get the first character of each item and append to "initials"
            initials.append((word[0]))

        # remove brackets and commas
        letter = str('\n'.join(initials))

        # remove line breaks
        psd = letter.replace('\n', '')
        keyword = word_list.replace('\n', ' ')
        title = 'KEYWORDS:'

        return render_template('index.html', psd=psd, keyword=keyword, title=title)

    return render_template('index.html')
