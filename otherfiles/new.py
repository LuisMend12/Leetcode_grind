from collections import deque



def blueprint_approval(blueprints):
    q = deque()

    for x in blueprints:
        temp = deque()

        # Move all elements smaller than x to temp
        while q and q[0] < x:
            temp.append(q.popleft())

        # Insert x in the right place
        temp.append(x)

        # Put the rest of q back into temp
        while q:
            temp.append(q.popleft())

        # Update q
        q = temp

    return list(q)


            

            
            





print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 



# [1, 2, 3, 4, 5]
# [2, 4, 5, 6, 7]