import csv
from collections import defaultdict
import numpy

#columns = defaultdict(list)
columns = numpy.array([1,2,3])

with open('Account.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            #columns[k].append(v) # append the value into the appropriate list
            newArray = numpy.insert(columns, [1, columns[k].append(v)])
                                 # based on column name k


#with open('Account2.csv') as d:
#    reader2 = csv.DictReader(d)
#    for row in reader2: # read a row as {column1: value1, column2: value2,...}
#        for (k,v) in row.items(): # go over each column name and value 
#            columns[k].extend(v) # append the value into the appropriate list
                                 # based on column name k

#formatted_string = "\n".join(columns['name'])
print(newArray)