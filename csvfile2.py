#Just read lines one by one :
import csv
with open("vacation.txt","r") as f:
    reader =csv.reader(f,delimiter="\t")
    for line in reader:
        print(line)

#skip the first row which is header and only print the line number 2 in a list
with open("vacation.txt","r") as f:
    reader=csv.reader(f,delimiter="\t")
    next(reader)
    for line in reader:
        print(line[2])
#write a new file with dash delimiter
with open("vacation.txt","r") as f:
    reader=csv.reader(f,delimiter="\t")

    with open("newvacation.txt","w") as d:
        writer=csv.writer(d,delimiter="-")

        for line in reader:
            writer.writerow(line)

#reading csv files with DictReader :
with open("vacation.txt","r") as f:
    reader=csv.DictReader(f,delimiter="\t")

    for line in reader:
        print(line["Sick"])
