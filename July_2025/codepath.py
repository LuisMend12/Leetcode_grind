def helper_trident(lst, counter, _max, index):

    if index == 0:
        if len(lst) == 0:
            return 0
        elif len(lst) == 1:
            return 1
        else:
            return helper_trident(lst, 1, 1, 1)
    
    else: 
        if index < len(lst):
           
            if lst[index - 1] + 1 == lst[index]: 
                counter += 1
            else:
                counter = 1
            _max = max(_max, counter)
            index += 1
                
            return helper_trident(lst, counter, _max, index)
        return _max

    

def longest_trident_sequence(gems):
    return helper_trident(gems, 0, 0, 0)


print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))
print(longest_trident_sequence([]))
print(longest_trident_sequence([1]))
print(longest_trident_sequence([5, 10, 6, 8, 3, 5]))

# 5
# 2
# 0
# 1
# 1


def check_stock(inventory, part_id):
    l, r = 0, len(inventory) - 1

    while l <= r:
        mid = (l + r) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            l = mid + 1
        else:
            r = mid - 1

    return False
        
print(check_stock([1, 2, 5, 20, 12], 20))
print(check_stock([1, 2, 5, 20, 12], 100))
'''
Problem 2: Find Millenium Falcon Part II
If you implemented your check_stock() function from the previous problem iteratively, implement it recursively.
If you implemented it recursively, implement it iteratively.
'''


# Understand: 
def check_stock_v2(inventory, part_id):
    inventory.sort()
    
    # base case 1: element was not found
    if len(inventory) == 0:
        return False

    mid = len(inventory) // 2

    # base case 2: element was found
    if inventory[mid] == part_id:
        return True
    
    elif inventory[mid] > part_id:
        return check_stock_v2(inventory[:mid], part_id)
    else:
        return check_stock_v2(inventory[mid+1:], part_id)

print(check_stock_v2([1, 2, 5, 20, 12], 20)) # true
print(check_stock_v2([1, 2, 5, 20, 12], 100))


'''
Problem 3: Find First and Last Frequency Positions
The Rebel Alliance has intercepted a crucial sequence of encrypted transmissions 
from the evil Empire. Each transmission is marked with a unique frequency code, represented as integers, 
and these codes are stored in a sorted array transmissions. As a skilled codebreaker for the Rebellion, 
write a function find_frequency_positions() that returns a tuple with the first and last indices of a specific 
frequency code target_code in transmissions. If target_code does not exist in transmissions, return (-1, -1).

Your solution must have O(log n) time complexity.

PLAN
1. Split input into two parts 
1. binary search on left part, until first occurance and record it
2. call binary searc
'''
def find_frequency_positions(transmissions, target_code):
    
#tuple = (min(), max())

print(find_frequency_positions([5,7,8,8,   9,9, 10], 8))
# [5,7,8,8     , 9,9, 10]
# [5, 7]      [8]
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))



# 
# output:
# (3, 4)
# (-1, -1)
# (-1, -1)




