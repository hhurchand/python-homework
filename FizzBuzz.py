''' Homework Week 6
    This code prints messages at different step-size (3 and 5)
    H Hurchand @ 24. 10. 2019
'''

c = ["FizzBuzz","Fizz","Buzz"]

for i in range(1,101):
    '''Multiples of 3 and 5 = Multiple of 15'''
    if (i%15 == 0):
        print(c[0])
    elif(i%3 == 0):
        print(c[1])
    elif(i%5 == 0):
        print(c[2])
    else:
        print(i)

