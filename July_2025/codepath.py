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
