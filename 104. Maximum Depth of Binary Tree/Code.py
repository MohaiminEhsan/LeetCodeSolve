# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = 0
        if root == None:
            return d
        else:
            d = self.depth(root, d)
            print(d)
            return d
    
    def depth(self, root, d):
        if root != None:
            d = d + 1
            print(d)
            dl = self.depth(root.left, d)
            dr = self.depth(root.right, d)

            if dl>=dr:
                d=dl
            else:
                d=dr

        return d
