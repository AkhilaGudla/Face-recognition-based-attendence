import csv

# field names
fields = ['Name']

# data rows of csv file
rows = [['Nikhil'],
        ['Sanchit'],
        ['Aditya' ],
        ['Sagar'],
        ['Prateek'],
        ['Sahil']]

# name of csv file
filename = "attend.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)