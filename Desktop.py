'''
This script prints all files in the Desktop.
The script prints the file in rows
H Hurchand @ 25.10.2019
'''

import os

path = 'C:/Users/hhurc/OneDrive/Desktop'
a = os.listdir(path)

for p in range(1,len(a)):
    print(a[p])
