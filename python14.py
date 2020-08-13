#Write a Python program to calculate midpoints of a line.
x1 = float(input("Enter the x1: "))
x2 = float(input("Enter the x2: "))
y1 = float(input("Enter the y1: "))
y2 = float(input("Enter the y2: "))

c = (x1+x2)/2
d = (y1+y2)/2

print("mid point c is :",c)
print("mid point d is :",d)

#Write a Python program to hash a word.
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()