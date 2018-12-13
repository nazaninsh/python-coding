#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# opening the file "employee" and printing the number of lines in that file using 'for' function
sum=0
with open("employee","r") as f:
	for line in f:
		sum=sum+1
print(sum)
