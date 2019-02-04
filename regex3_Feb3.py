#GROUP
print("1.")
import re
#the characteristics of findall is that it ony pull out the groups
string='Sara has 4 dogs but I think Mike has 5 cats and Dan has 8 fishes.'
example1=re.findall(r'([A-Za-z]+) \w+ \d+ \w+', string)
print(example1)#1.grouping out first names only

print("2.")
#2.print numbers only
ex2=re.findall(r'[A-Za-z]+ \w+ (\d)+ \w+', string)
print(ex2)

print("3.")
#3.group out only the animals
ex3=re.findall(r'[A-Za-z]+ \w+ \d+ (\w+)' , string)
print(ex3)

print("4.")
#4.print names, numbers and animals only
example1=re.findall(r'([A-Za-z]+) \w+ (\d+) (\w+)', string)
print(example1)

print("5.")
#5. organize the data by data types
#zip :organize ur data by categories by using index numbers
print(list(zip(*example1)))

print("6.")
#grouping out with re.search is more precise
#6.serach only pull out the first instances of the matche patterns
match=re.search(r'([A-Za-z]+) \w+ (\d+) (\w+)', string)
print(match.group())

print("7.")
#7.span gives the index of the group
print(match.span(2))

print("8.")
#only printing the groups
info=re.findall(r'([A-Za-z]+) \w+ (\d+) (\w+)', string)
print(info)

print("9.")
#9.only printing the first group
info=re.findall(r'([A-Za-z]+) \w+ (\d+) (\w+)', string)[0]
print(info)

# #findall has no group function so it does not work
# #in order to make it work we have to make another big group first and use for loops
info=re.findall(r'([A-Za-z]+) \w+ (\d+) (\w+)', string)[1]
print(info)

print("10.")
#10.printing the main group followd by subgroups
info=re.findall(r'(([A-Za-z]+) \w+ (\d+) (\w+))', string)
print(info)

print("11.")
#11.printing the second group only
for i in info:
    print(i[2])
