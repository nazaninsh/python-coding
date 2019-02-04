print("1.")
import re
#split will produce a list
#1. spliting based on spaces(as many)
print(re.split(r'\s*','This is my world'))

print("2.")
#2. include this spaces in the list as well
print(re.split(r'(\s*)','This is my world'))

print("3.")
#3. spliiting based on the word "s"
print(re.split(r'(s*)','This is my world'))
print(re.split(r'(s*)','This is my worlds'))
print(re.split(r's*','This is my worlds'))

print("4.")
#4.make a list based on character "a" through "f" but we are not incude them.
print(re.split(r'[a-g]','nbuceuwjdiwdk2wojdhyeoppquyevcvxn,zla'))

print("5.")
#5.if we wanna look for more chaarcters..
print(re.split(r'[a-gA-G0-9h-l]','nbuceuwjdiwdk2wojdhyeoppquyevcvxn,zla'))

print("6.")
#using flags for pointing that there is no difference between capital and small letters
# #re.I(ignorecase), re.M (multiline it: if the input is multiline we can evaluate it continiously instead of individual line)
print(re.split(r'[a-gA-G0-9h-l]','nbuceuwjdiwdk2wojdhyeoppquyevcvxn,zla',re.I|re.M))

print("7.")
#7.we are looking for the exact amount of numbers(range)
print(re.findall(r'\d{3,8}','I am a robot age 6533827832'))
