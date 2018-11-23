#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# print the number of lines in file
sum=0
with open("employee","r") as f:
	for line in f:
		sum=sum+1
print(sum)
