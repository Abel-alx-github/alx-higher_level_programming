#!/usr/bin/python3
""" module that defube function"""


def text_indentation(text):
    """ print text with . or : or ? at the end"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    text_ = ""

    for i in range(len(text)):
        if text[0] == ' ':
            continue
        elif i > 0 and i < len(text) and text[i - 1] in ['.', ':', '?']\
                and text[i] == ' ':
            continue
        else:
            text_ += text[i]
    for char in text_:
        print(char, end='')
        if char in ['.', ':', '?']:
            print("\n")
