# Lake Raleigh Score Report

## Objective

The report generated by the control unit provides a CSV file with several columns. The data for each participant is listed in a row. I need to re-organize the data by removing the unnecessary fields and performing some minor calculations such as the total time on the course and the total points scored based on the controls which were punched.

## SI Report Data File (Useful Columns)

1. ID Number - SI-Card
1. Start time - ST-Time
1. Finish time - FI-Time
1. Number of punches - No. of punched
1. The control number of each control punched - These are listed in the columns labeled by the punch number, i.e. `1.CN`

## Course File

1. Control Numbers on the Course
1. Point value

## Required Output

1. ID Number - maybe replace with or include the student name
1. Control Numbers punched
1. Value for each control punched
1. Overall time
1. Total Score - not necessary, but if easy to implement...

## Anticipated Problems - Priority Level

### Student punches duplicate control point - Major

The duplicates will need to be removed. Consider storing the control numbers punched in a list, then just check to see if the number already exists in the list before inserting it.

### Duplicate id numbers can exist in the SI report - Major

This could be difficult to solve. A possible solution would be to process each row, then check to see if the id number already exists in the new list before it's added. If the new row has more controls punched then it replaces the current row. Otherwise, it can be skipped.

### Time calculations will require conversion to mins - Major

Convert all times to seconds, perform any calculations required, then convert to minutes for the final report.

### The SI report might contain blank column fields - Minor

The report file is in CSV format. Some versions of the report have a series of blank column fields which can add a series of commas at the end of the useful fieldnames. Such columns shoud be removed when the file is read to reduce memory usage and prevent errors.

### Updates to the SI report may change the field names in the future - Minor

The latest firmware for the SI unit will change the fieldnames again. If the current fieldnames are hardcoded into the script, it will require continual refactoring of the code each time the fieldnames change. However, using a separate file to list the fieldnames which are relevant to the needs of the output is worth consideration.