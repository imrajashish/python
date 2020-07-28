import re
str = "take up One idea. One idea at a Time"
result = re.search(r'o\W',str)
print(result)

result = re.findall(r'o\w\W',str)
print(result)

result = re.match(r'T\w\W',str)
print(result)

result = re.sub(r'One','Two',str)
print(result)

#split
import re
str = "take up 1 One idea 123. One idea 4at a Time"
result = re.search(r'o\W',str)
print(result)

result = re.findall(r'o\w\W',str)
print(result)

result = re.match(r'T\w\W',str)
print(result.group())

result = re.sub(r'One','Two',str)
print(result)

result = re.findall(r'o\w{1,2}',str)
print(result)

re.split(r'\dt',str)
print(result)