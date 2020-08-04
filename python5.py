# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)

#Write a Python program to get OS name, platform and release information.
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
