#!/usr/bin/python3
"""Module with Text Indention related functions

Parameters:
    None

Methods:
    test_indention -  prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
     Prints a text with 2 new lines after each
     of these characters: ., ? and :

     Parameters:
     - text (str): String to be processed

     Raises:
     - TypeError: text is not str

     Returns:
     None
    """

    # Trim function
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    trimmed_text = text.strip()

    # Update text to automatically add double new lines where necessary
    updated_text = ""
    added_newline = False

    for char in trimmed_text:
        if added_newline and char.isspace():
            added_newline = False
            continue

        updated_text += char
        if char in (':', '?', '.'):
            updated_text += "\n\n"
            added_newline = True

    # Print text
    print(updated_text, end="")
