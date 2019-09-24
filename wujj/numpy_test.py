# First you should download the mpg.csv dataset from the above link to your computer. Then use the LEFT sidebar menue on this page
# (Files --> Upload) to upload the scv to your colab session. You would have to do this every time you close your colab session.
# After you uploaded the csv to your colab seccion, use this code to import the csv file into a list
import csv
import numpy as np

csvfile= open('/Users/wells_wang/Desktop/mpg.csv') # open the file into a variable
mpg = list(csv.reader(csvfile)) # read the file as csv and then transfer it to a list
mpg[:3] # check out the first three items in our list.

# 1. We do not need the column headings as the first item. Lets move the headings to another variable.

# headings = mpg[0]
# mpg = mpg[1:]
# print(headings)
# print(mpg)

# 2. Try transforming the mpg dataset to NumPy array. What happens?
        #Integer becomes string
    # Fix the issue by moving the name column to another list.
    # You may do this any way you can and print out both the names and the mpg datasets.
    # Can you do it with list comprehension?
    #  [x for b in a for x in b]
# mpg3 = [None for i in mpg for j in i if '?' in j]

print(mpg3)
npa = np.array(mpg3)
print(mpg)
print(npa)

# with open('/Users/wells_wang/Desktop/mpg.csv') as csvfile:
#     file = csv.reader(csvfile)
#     for row in file:
#         print(row)
# print(csv.reader(csvfile))
