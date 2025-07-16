# Q.1 To print the how many times the number in list 2 is occured in list 1 

'''
Constraints = 
1.  1 < n[i] <= 10
2.  n can have 10^8 elements
3.  m can have 10^8 elements
'''

# Method 1 but it is not satisfy the constraints 
m = [1,2,2,3,4,5]
n = [12,554,2,455]

for num in n:
    count = 0
    for x in m:
        if x == num:
            count += 1
    print(f"The {num} occurs {count} in m")


# Method 2

hash_list = [0] * 11
for num in m:
    hash_list[num] += 1
for num in n:
    if num < 1 or num >10:
        print(0)
    else:
        print(hash_list[num])
    

# Method 3 -- using dictionary

a = [1,2,2,2,3,4,4,5,5,5,8]
b = [4,1,5,7,8,66,2]
freq_map = {}
for num in a:
    freq_map[num] = freq_map.get(num , 0)+ 1
for num in b:
    print(f"{num} occurs {freq_map.get(num , 0)} times in a")

print()


# Q.2 
'''
Constraint =
'a' <= str1[i] <= 'z' 
'''
str1 = "azcsaabczz"
str2 = ["a","b","z","s"]
freq_map1 = {}
for char in str1:
    freq_map1[char] = freq_map1.get(char , 0) + 1
for char in str2:
    print(f"{char} occurs {freq_map1.get(char , 0)} in str1")