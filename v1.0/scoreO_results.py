"""
    File Name: scoreO_results.py
    Author: David Conner
    Date Created: Mon Feb  1 17:15:59 2016
    Date Last Modified: Thu 04 Feb 2016 01:23:56 PM EST
    Python Version: 3.5
    Description: This file reads the results from the Lake Raleigh
        Score-O event. It will remove duplicate punches and calculate
        the grade for each student dependent on the controls visited.
        The points scored for each control punched are printed for the student
        along with the total points earned in the event.
    Requires: File named 'scoreO_course.txt' that contains a comma-separated
        list of the control codes with the corresponding points. A file named
        'lr_score.csv' that contains the results with column names matching
        this order: Name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, Time, Penalty.
    TODO: Include a 'Help' argument that displays various information to the
        user regarding the requirements of the program. Allow the filenames
        to be requested on the command line, import a file with the fieldname
        keys, handle imported files which have row lengths that vary due to
        students punching duplicate controls, order the results by student
        last name when writing the final file, organize much of the code in
        reasonable functions that check for errors. Allow the user to enter
        the path and name of the final results file written to the disk.
"""

import csv


def is_number(s):
    """A quick function to check if a string is a number."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def remove_dup_punches(scores, scale):
    """Removes duplicate punches and returns a dictionary that contains the
        student's points for each valid control punch including a new fieldname
        for the total score."""

    # Temporary dictionary to store the data
    punch = {}
    info = {}
    for key, value in scores.items():
        # The values are imported as strings and I don't want to iterate
        # over the strings that aren't control numbers
        if is_number(key):
            if value in scale:
                if scale[value] not in punch.values():
                    punch[key] = scale[value]
                else:
                    # If the value is a duplicate, set the points to zero
                    punch[key] = '0'
            else:
                punch[key] = '0'
        else:  # The value must be a string like Name, Time or Penalty
            info[key] = scores[key]
    punch.update(info)   # merge the two dicts
    return punch


def total_points_earned(scores):
    """Calculate the total points earned by each student."""
    # Contains the total of all punched controls
    total_score = 0
    for key, value in scores.items():
        if is_number(key):
            total_score += int(value)

    # Now calculate the total by subtracting any penalties and
    # append the total to the temp dictionary before appending the
    # row to the new list containing the clean results.
    if 'Penalty' in scores:
        return (total_score + int(scores['Penalty']))
    else:
        return total_score


# I'm creating a dictionary of the control codes with the corresponding
# point values for each control from a CSV file - ie. code,point value
controls = {}
with open('scoreO_course.txt', 'r', newline='') as scores:
    reader = csv.reader(scores)
    for row in reader:
        controls[row[0]] = row[1]

# These are the fieldnames in order they appear in the results file
# I created. I'll need this list to provide an order for the data
# written to the final results file after the data is clean.
keys = ['Name', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
        'Time', 'Penalty']

# Add a column to the keys list that we'll calculate and write to the
# final results file.
keys.append('Total')

# This list will contain the rows from the results file with each row
# stored as an individual dictionary.
results = []
with open('lr_score.csv', 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        results.append(row)

# I want to remove duplicate punches so I'm creating an empty list
# to store the rows after I've removed the duplicates.
totals = []
for result in results:
    # Remove duplicate punches
    clean = remove_dup_punches(result, controls)

    # Get the total points for all valid punches
    clean['Total'] = total_points_earned(clean)

    # Append the students results to the array for printing
    totals.append(clean)

# After the data is cleaned up I want to write the results to a
# CSV file
with open('lr_score_results.csv', 'w') as results_file:
    writer = csv.DictWriter(results_file, fieldnames=keys)
    writer.writeheader()

    for row in totals:
        writer.writerow(row)
