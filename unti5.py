# # Problem 1: Greatest Node
# # Write a function find_max() that takes in the head of a linked list and returns the maximum value in the linked list. You can assume the linked list will contain only numeric values.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_max(head):
#     # # 
#     # if not head =! if head is None:
#     if head is None:
#         raise ValueError("Linked list is empty!")
    
#     max = head.value

#     current = head.next

#     while current:
#         if current.value > max:
#             max = current.value
        
#         current = current.next

#     return max

    


    

# # input: head of a linked list: O(n), O(1)

# # output: the max of the linked list

# head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))



# # Expected Output:

# # 8
# # 8





# Problem 2: Remove Tail
# The following code incorrectly implements the function remove_tail(). When correctly implemented, remove_tail() accepts the head of a singly linked list and removes the last node (the tail) in the list. The function should return the head of the modified list.

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against. Use print statements, print_linked_list(), and the stack trace to identify and fix any bugs so that the function correctly removes the last node from the list.

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
        
# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def remove_tail(head):
#     if head is None:
#         return None
#     if head.next is None:
#         return None 
        
#     current = head
#     while current.next.next: 
#         current = current.next

#     current.next = None 
#     return head
# # Example Usage:

# head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# # Linked List: Isabelle -> Alfonso -> Cyd
# print_linked_list(remove_tail(head))
# # Expected Output:

# # Isabelle -> Alfonso



# Problem 3: Delete Duplicates in a Linked List
# Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). The resulting list should maintain sorted order. Return the head of the linked list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# input: head of a sorted linked list
# output: linked list but with no dupes, Return the head of the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_dupes(head):
#     if head is None: #edge case to check if the linked list is empty
#         return None
    
#     temp=head.next
#     while temp.next.next:
#         if temp.next.value==temp.next.next.value:
#             temp=temp.next.next.next
#     return head
    
    


# # Example Usage:

# head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))
# # Example Output:

# # 1 -> 2 -> 4 -> 5




# Problem 4: Does it Cycle?
# A variation of the two-pointer technique introduced earlier in the course is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to write a function has_cycle() that returns True if the list has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# input: head of a linked list
# output: Either true or false if there is a cycle in the list

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def has_cycle(head):
    
#     if head is None: #edge case to check if the linked list is empty
#         return False
    
#     slow = head

#     fast = head

#     while fast and fast.next:
#         slow = slow.next          # Move slow pointer by one
#         fast = fast.next.next     # Move fast pointer by two

#         if slow == fast:          # If they meet, there's a cycle
#             return True
    
#     return False


# class Node:
#     def __init__(self, val, next=None):
#         self.value = val
#         self.next = next

# def has_cycle(head):
#     if not head:
#         return False
    
#     slow = head  # Starts at the head
#     fast = head  # Also starts at the head

#     while fast and fast.next:
#         slow = slow.next          # Move slow pointer by one
#         fast = fast.next.next     # Move fast pointer by two

#         if slow == fast:          # If they meet, there's a cycle
#             return True
    
#     return False


    




# peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# # Toad.next = Luigi
# peach.next.next.next = peach.next

# print(has_cycle(peach))
# # Example Output:

# True




# Problem 6: Careful Reverse
# Given the head of a singly linked list and an integer k, reverse the first k elements of the linked list. Return the new head of the linked list. If k is larger than the length of the list, reverse the entire list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
        
def reverse_first_k(head, k):
	pass



# Example Usage:

head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))
# Example Output:

# orange -> cherry -> apple -> peach -> pear