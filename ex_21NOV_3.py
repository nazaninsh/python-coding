#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# this program will print the total number of vacation days for all employees
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
