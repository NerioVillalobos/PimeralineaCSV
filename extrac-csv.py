import csv
from collections import defaultdict

columns = defaultdict(list)


with open('Account.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k


#with open('Account2.csv') as d:
#    reader2 = csv.DictReader(d)
#    for row in reader2: # read a row as {column1: value1, column2: value2,...}
#        for (k,v) in row.items(): # go over each column name and value 
#            columns[k].extend(v) # append the value into the appropriate list
                                 # based on column name k

formatted_string = "\n".join(columns['name'])
print(formatted_string)