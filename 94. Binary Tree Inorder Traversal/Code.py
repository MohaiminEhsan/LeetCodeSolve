# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = []
        self.traversal(node, root)
        return node    
    #     res = []
    #     self.do_inorderTraversal(res, root)
    #     return res

    # def do_inorderTraversal(self, res, curr):
    #     if curr is None:
    #         return
    #     if curr.left is not None:
    #         self.do_inorderTraversal(res, curr.left)
    #     res.append(curr.val)
    #     if curr.right is not None:
    #         self.do_inorderTraversal(res, curr.right)

    def traversal(self, node, root):
        if root == None:
            return
        else:
            if root.left != None:
                self.traversal(node, root.left)
            node.append(root.val)
            if root.right != None:
                self.traversal(node, root.right)
    
         
