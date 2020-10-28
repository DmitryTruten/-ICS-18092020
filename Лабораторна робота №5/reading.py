import csv
import sys
filename = "the_first_group.txt" 
fd = open("the_first_group.txt", "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader:
    print(row)
fd.close() 