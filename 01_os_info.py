import platform
import sys
#strange
info = 'OS info \n {} \n\nPython Version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture()
)
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)
