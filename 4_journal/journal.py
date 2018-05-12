"""
This contains the helper functions for the Journal app
"""

import os


def load(name):
    """
    This loads a journal data

    :param name: This is the name of the journal to load
    :return: Journal Data populated from file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as file_in:
            for entry in file_in.readlines():
                data.append(entry.rstrip())
    
    return data


def save(name, journal_data):
    """
    This saves active journal to file

    :param name: name of the journal
    :param journal_data: The active journals data
    """
    filename = get_full_pathname(name)
    print("Saving to: {}".format(filename))
    file_out = open(filename, 'w')

    for entry in journal_data:
        file_out.write(entry + '\n')

    file_out.close()


def get_full_pathname(name):
    """
    Gets the correct file path for a journal

    :param name: Name of the Journal
    :return: filepath as a string
    """
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))
    return filename

def add_entry(text, journal_data):
    """
    Adds a new entry to the active journal

    :param text: Text to be added to the journal
    :param journal_data: Current Journals data loaded into memory
    """
    journal_data.append(text)
    