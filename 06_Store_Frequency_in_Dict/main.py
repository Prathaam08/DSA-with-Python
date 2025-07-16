# Method 1

nums = [1,1,2,5,1,2,4,6,3,3,7,8,7,9,9]
x= 9

freq_map = dict()
for i in range(0 , len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map[x])

# Method 2

number = [5,4,5,1,2,8,4,6,1,1,3,3,4]
hash_map = dict()
x = 2
for i in range(0 , len(number)):
    hash_map[number[i]] = hash_map.get(number[i] , 0)+1
print(hash_map[x])

