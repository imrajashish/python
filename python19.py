#Write a Python program to convert a byte string to a list of integers.
x = b'ABC'
print( )
print(list(x))

#Write a Python program to list the special variables used within the language.
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()

#Write a Python program to get the system time.
import time
print(time.ctime())
print()

#Write a Python program to clear the screen or terminal.
import os
import time
# for windows
# os.system('cls')
os.system("ls")
time.sleep(6)
# Ubuntu version 10.10
os.system('clear')

#Write a Python program to get the name of the host on which the routine is running.
import socket
host_name = socket.gethostname()
print()
print("Host name:",host_name)
print()

#Write a Python program to access and print a URL's content to the console.
from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)

