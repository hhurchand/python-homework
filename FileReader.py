''' ADVANCED AND REACH

Script
(i) reads house.data file
(ii)prints each line of the file
(iii) splits each line and prints it as an array

'''

f = open(file="housing.data")

for line in f:
    b = f.readline()
    print(b.split())

f.close()