# # "You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. 
# # Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.

# # Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
# # Assume the input tree is balanced when calculating time and space complexity.

# """
# Umpire:
#   input: a binary tree
#   Output: a list of Node values
#   edge cases: if tree is empty -> empty list. If no right side, then return root

#   Match:  while right side 
  
#   Plan: 
#   Create an empty list
#         iterate through loop as long as root.right exists
#         append to value to list
# """

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right



# # def right_vine(root):  
# #   node_list = []
# #   if root is None:
# #     return node_list
# #   while root:
# #     node_list.append(root.val)
# #     root = root.right
  
#   # return node_list

# # ['Root', 'Node2', 'Leaf3']
# # ['Root']


# # ['Root', 'Node2', 'Leaf3']
# # ['Root']


# # Example Usage:

# # """
# #         Root
# #       /      \
# #     Node1    Node2
# #   /         /    \
# # Leaf1    Leaf2  Leaf3
# # """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# # """
# #       Root
# #       /  
# #     Node1
# #     /
# #   Leaf1  
# # """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# Example Output:

# ['Root', 'Node2', 'Leaf3']
# ['Root']

# =========================================================================================================================================================== ===========================================================================================================================================================

# If you implemented right_vine() iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.


"""
Umpire:
  input: a binary tree
  Output: a list of Node values
  edge cases: if tree is empty -> empty list. If no right side, then return root

  Match:  while right side 
  
  Plan: 
  Create an empty list
        iterate through loop as long as root.right exists
        append to value to list
"""

# def right_vine(root):
#   node_list = []
#   if not root:
#     return node_list
#   appendNode(root , node_list)
#   return node_list

# def appendNode(root, list):
#   if root is None:
#     return 
#   list.append(root.val)
#   appendNode(root.right , list)


# # ['Root', 'Node2', 'Leaf3']
# # ['Root']


# print(right_vine(ivy1))
# print(right_vine(ivy2))

# =========================================================================================================================================================== ===========================================================================================================================================================


# You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, you need to do a full survey of the tree to evaluate which sections need to be pruned.

# Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal.
# In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals are often used when deleting nodes from a tree.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.


def survey_tree(root):
  if root is None:
    return None
  
  list_node = []
  postAppend(root , list_node)
  return list_node
  
def postAppend(root, list_node):
  if root is None:
    return 
  postAppend(root.left, list_node)
  postAppend(root.right, list_node)
  list_node.append(root.val)
  
# ['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root'] 

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))


# ['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']


'''
Umpire:
  input: a binary tree
  Output: a list of Node values
  edge cases: if tree is empty -> empty list. If no right side, then return root

  M: Recursion
  
  P: Create a list
     
"it should work now "
  

['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root'] it works, this is the output
  '''

