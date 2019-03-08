#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# this program will print the total number of vacation days for all employees using csv library
#first we open the "vacation file" then read the file using csv.reader ( we chose "tab" as delimiter here)
# in order to get the total numbers of vacation day only we have to use "if function" in "for loop function"to pass the header 
import csv
with open("vacation.txt","r") as f:
    sumVacation=0
    sumSick=0
    line_count = 0
    reader = csv.reader(f,delimiter="\t")
    for line in reader:
        if line_count == 0:
            print(line)
            line_count += 1
        else:
            sumVacation = sumVacation+int(line[1])
            sumSick = sumSick + int(line[2])
            line_count += 1
print(sumVacation,sumSick)
