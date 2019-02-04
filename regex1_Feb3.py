#match only search at the begining of the string
import re
print("1.")
match=re.match("c","abcdef")
print(match) #1.will not work and give NONE

print("2.")
#2.search, searches anywhere
search=re.search("c", "abcdwfgcccg") #but just printing the first instances
print(search.group())
a=re.search('\w\w\w\w','abcdefg')
print(a.group())

print("3.")
#3.finding the repition of the "ab" by putting it in the groups
string="abababababab"
result=re.search('(ab)+', string)
print(result.group())

print("4.")
#(): pull out the specific pattern
#[]: pull out the letters with no specific pattern..just searching for the letter with as many repition as will happen
b=re.search('(ab)+', 'ababbbbb')
print(b.group())
#
d=re.search('[ab]+', 'bababaababab')
print(d.group())

print("5.")
#5. '(ab)+\w+' is the same as '[ab]+'
c=re.search('(ab)+\w+', 'abababbbbbbb')
print(c.group())

print("6.")
d=re.search('(ab)+','ababababab')
#6.we are only creating one group and overwritten each time
print(d.group())
print(d.group(0)) #both of these give entire match and it is not really a group

print("7.")
# print(d.group(2)) #7.no value cause we r only creating one group not multiple
print(d.groups())#7. shows the groups and that we have only one group too

print("8.")
#using 2 groups
e=re.search('(ab)+(ab)', 'abababababab')
print(e.groups())
#8.first ab(group one) is going to consume all the ab..cause its gready
#and then it realize it has to consider group 2(second ab) so it starts the next ab from the end( last ab)

print("9.")
#9. printing the second group's span
print(e.span(2)) #yani span group2

print("10.")
f=re.search('(\d)+','123456789')
print(f.groups())
#10. here each value is a group, all of them satisfies the group we have,casue
#we r using quantifiers(+) and the value of the group getting updated each time
#so when we r using quantifiers we get the last value of that group and we get only one groups

print("11.")
g=re.findall('(\d)+','123456789')
print(g)#it behave like the previous and does not pull out the entire matche
# #cause it is findall, so it pulls out only the group and the final mkone
