import csv 
import sys 
filename = "the_first_group.txt"
fd = open(filename, "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader:     
    print(row)
fd.close()
fd = open(filename, "a+")
x=input(1 or 2)
if(x==1):
    print("Ok")