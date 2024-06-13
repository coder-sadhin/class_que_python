def find_unique_numbers(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    unique_numbers = [num for num, cnt in count.items() if cnt == 1]
    return unique_numbers

# lis_num = list(input())
newLst=find_unique_numbers([1,9,8,8,7,6,1,6])
newLst1=find_unique_numbers([5,5,2,3,3,3,8,8,8,11])
print(newLst)
print(newLst1)