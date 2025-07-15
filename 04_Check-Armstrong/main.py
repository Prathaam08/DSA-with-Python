# Armstrong Number 
# 153 = 1^3 + 5^3 + 2^3 = 153
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1634


n = 1634

num = n 
total = 0
length = len(str(num))
while num > 0:
    last_digit = num % 10 
    total = total + (last_digit ** length )
    num = num // 10 

print(total == n)

