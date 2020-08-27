# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def tree_paths_sum(root):
    # base case -> if no node, return
    if root == None:
        return 0 
    
    # recursively traverse all nodes and add up node values
    return root.value + tree_paths_sum(root.left) + tree_paths_sum(root.right)