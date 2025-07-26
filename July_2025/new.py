from collections import deque 

# Tree Node class
class TreeNode:
  def _init_(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


# def sort_plants(collection):
#     output = []
#     def helper(node):
#         nonlocal output
#         if not node:
#             return
#         helper(node.left)
#         if node:
#             output.append((node.key, node.val))
#         helper(node.right)
#     helper(collection)
#     return output
# #understand
#     """
#     we are given a list of nodes that contain names and rarities
#     we want to make a bst using the rarities of these plants

#     our output is going to be an array of plant nodes as tuples (key, val)
#     sorted from least to most rare
    
#     so we are doing inorder traversal
#     """
# #match
        
# #plan
#     """
#     we want to iterate through the tree inorder (all the way down left and, up and then right), left subtree, root node, right subtree
#     sort_plants(collection):
#         output = []
#         helper(collection)
#         def helper(node) 
#             helper(node.left)
#             if node:
#                 output.append((node.key, node.val))
#             helper(node.right)
#         return output
        
#     """
# #implement
# #review
# #evaluate




# """
#          (3, "Monstera")
#         /               \
#    (1, "Pothos")     (5, "Witchcraft Orchid")
#         \                 /
#   (2, "Spider Plant")   (4, "Hoya Motoskei")
# """

# # Using build_tree() function at the top of page
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))


# #example output: [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]


# # You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. The plants are organized according to their names (vals) in alphabetical order in the BST.

# # Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the flower is present in the garden and False otherwise.

# # Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

# #understand
# #    given root of the binary tree, our target a string which a naem for a flower
# #     out output of this function returns true or false if we find flower
   

# #match
        
# #plan
#     """
#     def helper(node, target):
#         if node.val == target:
#             return True
#         if node.right:
#         if node.val > target:
#             helper(node.right)
#         else:
#             helper(node.left)
        
#     """
# #implement


# #review
# #evaluate



class TreeNode():
     def _init_(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    def helper(node, name):
        if node is None:
            return False
        if node.val == name:
            return True
        if node.val >= name:
            return helper(node.right, name)
        else:
            return helper(node.left, name)
    return helper(inventory, name)


"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  Lilac  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

