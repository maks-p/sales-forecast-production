import csv

with open('csv/rest_1_both_pos_by_check.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
