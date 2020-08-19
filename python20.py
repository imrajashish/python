#Write a Python program to extract the filename from a given path.
import os
print()
print(os.path.basename('/users/system/student/homework-1.py'))
print()

# Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.
import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()

#Write a Python program to get the users environment.
import os
print(os.environ)

#Write a Python program to divide a path on the extension separator.
import os.path
for path in['text.txt','filename','/user/system/text.txt','/','']:
    print('"%s":'%path,os.path.splitext(path))

#Write a Python program to retrieve file properties
import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
