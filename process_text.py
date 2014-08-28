#!/usr/bin/python

# Import necessary libraries
import os 
import re

# Variable definitions
file_list = []
patterns = [">Discussion<", ">History<", ">View source<", ">What links here<", 
           "<li id=\"disclaimer\">" ]
dir_path = "/home/tony/public_html/test/"

# Get all files have .html extension
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".html"):
            file_list.append(os.path.join(root, file))


for i in range(len(file_list)):
    # Open each file for reading
    file = file_list[i]
    f = open(file, "r");
    lines = f.readlines()
    f.close()

    # Omit the lines contain the search pattern
    f = open(file, "w")
    start_write = "true"

    # Check all lines
    for line in lines:
        start_write = "true"
        for p in patterns:
            # If line matches one pattern, skip
            if re.search( r"%s" % p, line):
                start_write = "false"
        if (start_write == "true"):
            f.write(line)
    f.close()
