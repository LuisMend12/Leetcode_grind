def edit_dna_sequence(head, m, n):
    current = head
    while current: # traverse linked list

        for i in range(1, m): # setting up for range loop to keep m nodes, it goes from 1 to m, because we are going to have at least one node
            if current is None: # if we don't have a next node 
                return head # we return the head of the linked list
            current = current.next # we iterate through the linked list
        
        if current is None: # if we don't have a next node from prev then we break the function
            break

        temp = current.next # we set a variable 

        for j in range(n): # we set another for range loop to skip n nodes
            if temp is None: # we check if the current.next node is empty
                break   # if that is the case then we break the function
            temp = temp.next # we iterative through the linked list

        current.next = temp #we set out current.next to temp 
        current = temp # we set temp to current

    return head