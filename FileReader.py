''' ADVANCED AND REACH

Script
(i) reads house.data file
(ii)prints each line of the file - part needs to be uncommented
(iii) splits each line and prints it as an array

'''

f = open(file="housing.data")

"""Don't use readline(), as line in already acts as a read!"""
for line in f:

    """Uncomment next line to print each line of the file"""
    """print(line)"""

    print(line.split())

f.close()