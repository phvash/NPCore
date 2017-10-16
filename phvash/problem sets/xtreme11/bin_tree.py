class Node:

      def __init__(self,info): #constructor of class

          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined

      def __str__(self):

          return str(self.info) #return as string


class searchtree:

      def __init__(self): #constructor of class

          self.root = None


      def create(self,val):  #create binary search tree nodes

          if self.root == None:

             self.root = Node(val)

          else:

             current = self.root

             while 1:

                 if val < current.info:

                   if current.left:
                      current = current.left
                   else:
                      current.left = Node(val)
                      break;      

                 elif val > current.info:
                 
                    if current.right:
                       current = current.right
                    else:
                       current.right = Node(val)
                       break;      

                 else:
                    break 

      def bft(self): #Breadth-First Traversal

          self.root.level = 0 
          queue = [self.root]
          out = []
          current_level = self.root.level

          while len(queue) > 0:
                 
             current_node = queue.pop(0)
 
             if current_node.level > current_level:
                current_level += 1
                out.append("\n")

             out.append(str(current_node.info) + " ")

             if current_node.left:

                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  

             if current_node.right:

                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                      
                 
          print "".join(out)   


      def inorder(self,node):
            
           if node is not None:
              
              self.inorder(node.left)
              print node.info
              self.inorder(node.right)


      def preorder(self,node):
            
           if node is not None:
              
              print node.info
              self.preorder(node.left)
              self.preorder(node.right)


      def postorder(self,node):
            
           if node is not None:
              
              self.postorder(node.left)
              self.postorder(node.right)
              print node.info


def build_the_tree(max):                     
    tree = searchtree()     
    for i in range(max + 1):
        tree.create(i)
    return tree



# This function retturn pointer to LCA of two given values
# n1 and n2 
# v1 is set as true by this function if n1 is found
# v2 is set as true by this function if n2 is found
def findLCAUtil(root, n1, n2, v):
    
    # Base Case
    if root is None:
        return None

    # IF either n1 or n2 matches ith root's key, report
    # the presence by setting v1 or v2 as true and return
    # root (Note that if a key is ancestor of other, then 
    # the ancestor key becomes LCA)
    if root.key == n1 :
        v[0] = True
        return root

    if root.key == n2:
        v[1] = True
        return root

    # Look for keys in left and right subtree
    left_lca = findLCAUtil(root.left, n1, n2, v)
    right_lca = findLCAUtil(root.right, n1, n2, v)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root 

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


def find(root, k):
    
    # Base Case
    if root is None:
        return False
    
    # If key is present at root, or if left subtree or right
    # subtree , return true
    if (root.key == k or find(root.left, k) or
        find(root.right, k)):
        return True
    
    # Else return false
    return False

# This function returns LCA of n1 and n2 onlue if both
# n1 and n2 are present in tree, otherwise returns None
def findLCA(root, n1, n2):
    
    # Initialize n1 and n2 as not visited
    v = [False, False]

    # Find lac of n1 and n2 using the technique discussed above
    lca = findLCAUtil(root, n1, n2, v)

    # Returns LCA only if both n1 and n2 are present in tree
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and 
        find(lca, n1)):
        return lca

    # Else return None
    return None

if __name__ == '__main__':
    no_of_test_cases = int(input())
    for time in range(no_of_test_cases):
        node1, node2 = [int(i) for i in raw_input().strip(" ").split(" ")]
        max_node = max(node1, node2)
        bin_tree = build_the_tree(max_node)
        lca = findLCA(bin_tree, node1, node2)
        print(lca if lca else 0)
