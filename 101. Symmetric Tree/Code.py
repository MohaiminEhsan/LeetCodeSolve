# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        node = []
        self.inorder(node, root)
        l = len(node)
        print(node)
        if l == 0:
            return True
        elif l==1:
            return True
        elif l%2==0:
            return False
        elif l%2==1:
            i = 0
            j = l-1
            while True:
                print(node[i], node[j])
                if node[i]!=node[j]:
                    return False
                i = i + 1
                j = j - 1
                if i==j:
                    return True



    def inorder(self, node, root):
        if root is None:
            return
        else:
            if root.left != None:
                self.inorder(node, root.left)
            node.append(root.val)
            if root.right != None:
                self.inorder(node, root.right)
                
                
                
######### ----------- Does not solve all the test cases

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.mirrorVisit(root.left, root.right)

    def mirrorVisit(self, left, right):
        if left is None and right is None:
            return True
        try:
            if left.val == right.val:
                if self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left):
                    return True
            return False
        except:
            return False

        
