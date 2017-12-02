# scoreO-report-generator

## Description

Organizes, edits and outputs the results for an orienteering score event. 

## Version 1.0

The initial attempt to write a script to help automate the steps to grade the performances on the score event. This script required the input of a manually created csv file summarizing the controls punched for each participant which were listed in the raw file produced by the SportIdent software. The script replaced the control number with the corresponding point value, removed duplicate punches, and totaled the participant's score before exporting the results to a csv file. 

To improve this script, the new version should be able to import, analyze, modify, and output the summary of results expected using the raw csv file exported by the SI software eliminating the need to manually create an intermediary file.

## Requirements

This script expects the results file in CSV format which is output by the SportIdent BS7 control station and a text file which provides the course information needed for the report, such as a map of the control numbers and values.
