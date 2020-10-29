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
for filename in os.listdir("D:\-ICS-18092020\Лабораторна робота №5\the_first_group\\plugins"):    
    print(filename)