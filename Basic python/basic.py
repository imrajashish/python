#indexing
s="ashish"
print(s[0])
print(len(s))
#slice
print(s[ : :-1])
#strip
p="suman"
print(p.lstrip())
#find
print(p.find("man"),len(s))
#count
print(s.count("s"))
#replace
print(s.replace("Ashish", "Reha"))
#upper
print(s[0: :1].upper()+s[2:].lower())
#title
print(p.title())
print(s.title())
#list
lst=[3,4,5,6,7,8,9]
print(len(lst))
#append
lst.remove(7)
print(lst)