class Node:
  def __init__(self, value):
    self.data = value
    self.right = None
    self.left = None

class Tree:
  def __init__(self):
    self.root = None





def print_preorder(root):
  if root != None:
    print root.value,
    print_preorder(root.left)
    print_preorder(root.right)

def print_postorder(root):
  if root!=None:
    print_postorder(root.left)
    print_postorder(root.right)
    print root.value,

def print_inorder(root):
  if root != None:
    print_inorder(root.left)
    print root.value,
    print_inorder(root.right)


def print_zigzag(root):
  if root != None:
    left_to_right = 0
    nodes_to_print = [root]
    while(1):
      old_nodes_to_print, nodes_to_print = nodes_to_print, []
      for current in old_nodes_to_print[::-1]:
        print current.value,
        if left_to_right == 1:
          if current.left:
            nodes_to_print.append(current.left)
          if current.right:
            nodes_to_print.append(current.right)
        else:
          if current.right:
            nodes_to_print.append(current.right)
          if current.left:
            nodes_to_print.append(current.left)
      if len(nodes_to_print) == 0:
        break
      left_to_right ^= 1


def print_left_view(root):
  if root:
    print root.value,
    if root.left:
      print_left_view(root.left)
    elif root.right:
      print_left_view(root.right)


def print_right_view(root):
  if root:
    print root.value
    if root.right:
      print_right_view(root.right)
    elif root.left:
      print_right_view(root.left)



def print_outer_layer_anticlock(root):

  def print_left_boundary(root):
    if root:
      if root.left:
        print root.value
        print_left_boundary(root.left)
      elif root.right:
        print root.value
        print_left_boundary(root.right)


  def print_right_boundary(root):
    if root:
      if root.right:
        print_right_boundary(root.right)
        print root.value
      elif root.left:
        print_right_boundary(root.left)
        print root.value
  def print_leaves(root):
    if root:
      print_leaves(root.left)
      if root.left is None and root.right is None:
        print root.value
      print_leaves(root.right)


  if root:
    print root.value
    print_left_boundary(root.left)
    print_leaves(root.left)
    print_leaves(root.right)
    print_right_boundary(root.right)





class resultNode:
  def __init__(self):
    self.size = 0
    self.maxi = float('-inf')
    self.mini = float('inf')
    self.isBst = True



def max_bst(root):

  def max_bst_util(root):
    r = resultNode()
    if root is None:
      return r
    if root.left is None and root.right is None:
      r.size = 1
      r.isBst = True
      r.mini = root.data
      r.maxi = root.data
      return r
    lResult = max_bst_util(root.left)
    rResult = max_bst_util(root.right)
    if (lResult.isBst and rResult.isBst and lResult.maxi < root.data and rResult.mini > root.data):
      r.mini = min(lResult.mini,min(root.data, rResult.mini))
      r.maxi = max(rResult.maxi, max(root.data, lResult.maxi))
      r.isBst = True
      r.size  = lResult.size + rResult.size + 1
      return r

    r.size = max(lResult.size, rResult.size)
    r.isBst = False
    return r
  return max_bst_util(root).size










if __name__=="__main__":

  # init a binary tree with default values
  tree = Tree()
  tree.root = Node(65)
  tree.root.left = Node(60)
  tree.root.right = Node(70)
  tree.root.left.left = Node(50)
  # tree.root.left.right = Node(4)
  # tree.root.right.left = Node(6)
  # tree.root.right.right = Node(7)
  root = tree.root

  print max_bst(root)

  # print "printing pre order"
  # print_preorder(root)

  # print "printing post order"
  # print_postorder(root)

  # print "printing in order"
  # print_inorder(root)

  # print_zigzag(root)
  # print_left_view(root)
  # print_right_view(root)
  # print_outer_layer_anticlock(root)




