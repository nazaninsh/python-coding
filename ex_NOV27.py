#!/usr/bin/python
#open files and read them
#string.rstrip() removes the white space after the string
with open("DNA.txt","r") as a:
    for line in a:
        print(line.rstrip())
#read lines from the begining and store them in the list called "lines"
    a.seek(0)
    lines=a.readlines()
    print(lines)
# read 100 charactors begining from 50th charactor in the DNA.txt files
    a.seek(50)
    charactors=a.read(100)
    print(charactors)
