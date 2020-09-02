#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = 'Tyrell Williams with help from John'


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """

    # mimic_dict = {'':[]}
    # with open(filename) as f:
    #     text = f.read().split()
    #     mimic_dict[''].append(text[0])
    # for number,word in enumerate(text):
    #     if word in mimic_dict:
    #         mimic_dict[word].append(text[number+1])
    #     mimic_dict[word] = [text]

    mimic_dict = {}
    with open(filename, 'r') as f:
        words = f.read().split()
    previous_word = ''
    for word in words:
        if previous_word not in mimic_dict:
            mimic_dict[previous_word] = [word]
        else:
            mimic_dict[previous_word].append(word)
        previous_word = word
    for loop in mimic_dict:
        print(loop, ':' , mimic_dict[loop])
    return mimic_dict 
    

def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    
    start_word = ''
    result = ''
    for _ in range(num_words):
        if start_word in mimic_dict:
            random_word = random.choice(mimic_dict[start_word])
            result += ' ' + random_word + ' '
            start_word = random_word
    return result
    
    
    
    # for _ in range(200):
    #     print(start_word, end='')
    #     new_word = mimic_dict.get(start_word)
    #     if not new_word:
    #         new_word = mimic_dict['']


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
