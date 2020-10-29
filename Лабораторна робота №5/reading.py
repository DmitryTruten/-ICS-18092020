import csv 
import sys
import glob  
import os
filename = "the_first_group.txt"
fd = open(filename, "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader:     
    print(row)
fd.close()