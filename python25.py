# Write a Python program to use double quotes to display strings.
import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3,'kamal':4,'johan':5}))

#Write a Python program to split a variable length string into variables.
s = "  Ashish    "
print(s.split())

#Write a Python program to list home directory without absolute path.
import os.path
print(os.path.expanduser('~'))

#Write a Python program to calculate the time runs 
from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)

#Write a Python program to input two integers in a single line.
'''print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)'''

#Write a Python program to print a variable without spaces between values. Go to the editor
x = 30
print('value of x is "{}"'.format(x))

#Write a Python program to extract single key-value pair of a dictionary in variables.
d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)

#Write a Python program to valid a IP address. 
import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
	