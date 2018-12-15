#using regular expression for pulling out all the numbers and names from
#the string called "exampleString"
#we use re library for thsi purpose
import re

exampleString ='''
Jess is 10 years old, and Dan is 16 years oldself.
Edd is 50,and his grandfather, Oscar, is 102.
'''
#we wanna search for numbers so we use \d and also we wanna search for ages that have digits between 1 and 3 so we use: {1,3}
#so the first parameter would be r'\d{1,3}' : we use r cause its regular expression
#so the firs parameter would be the regular expression we search for
#second parameter is where we wanna search for the re? 
#returns all the non-overlapping matches of patterns in astring as a list of strings
ages=re.findall(r'\d{1,3}',exampleString)
# [A-Z] or [a-z] and * says that we are looking for [A-z] or [a-z] but as many of them(zero or more)
names=re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)
# so we are getting list of these data(pulling out the ages and names)

#now we wanna make a dictionary to know which age is related to which names
#we define an empty dict first and then in the loop we add the keys and related values
#because we wanna add numbers one by one and one after another we say x+=1


ageDict={}
x=0
for eachname in names:
    ageDict[eachname]=ages[x]
    x+=1
print(ageDict)
