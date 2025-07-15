# Method : 01
n = 54115

num = n 
count = 0

while num > 0:
    count+=1
    num = num // 10
print(count)


# Method : 02
from math import *

def count_digit(number):
    return int(log10(number) + 1)

print(count_digit(164))

# Here Time complexity will be 0(log10(N))   log base 10 -- if num // 2 then log base 2