#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#importing os library  
import os
#we changed directory to /practice with os.chdir(" ")
os.chdir("/Users/nazaninshambayati/practice")
#get the current working directory plus adding new line after printing that
a=os.getcwd()
print(a,'\n')
#listing current directories plus adding a new line afterwards
b=os.listdir()
print(b,'\n')
