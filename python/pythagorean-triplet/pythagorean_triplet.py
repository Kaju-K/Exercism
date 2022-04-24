from math import *

#for this problem we have two conditions:
#a + b + c = N      and      a**2 + b**2 = c**2
#doing a little bit of math, we have that:
#b = (N**2 - 2*a*N)/(2*(N - a))
#and we also have the same condition for a as function of b
#a = (N**2 - 2*b*N)/(2*(N - b))
#which means that at some point this function start giving smaller values than the input
#so our go is to keep guessing the smaller number until we get to this point
#after that we would be receiving smaller numbers, so if it is an answer, we already passed it
#so to get to this point we do x > (N**2 - 2*x*N)/(2*(N - x))
#and see that this condition is satisfied when 
#x < (2 - sqrt(2))*N/2 --> x ~= 0.29*N 
#or x > (2 + sqrt(2))*N/2 --> x ~= 1.71*N   --> we don't need this since a + b + c = N and all the numbers should be positive
#so, using the first solution, we test the numbers for a until we get to that point
#after that, there is no more new list of numbers that fit the conditions

def limit(number):
    return floor((2 - sqrt(2))*number/2)

def testing(number, a):
    return (number**2 - 2*a*number)/(2*(number - a))
    

def triplets_with_sum(number):
    pythagorean_triple = []
    last_number = limit(number)
    for i in range(last_number):
        a = i+1
        b = testing(number, a)
        if b % 1 != 0:              #test if b is an integer
            continue
        c = sqrt(a**2 + b**2)       #no need to do this calculation before knowing if b is an integer or not
        if c % 1 != 0:              #test if c is an integer
            continue
        pythagorean_triple.append([a, b, c])    #uhul, we found them!!
    return pythagorean_triple
