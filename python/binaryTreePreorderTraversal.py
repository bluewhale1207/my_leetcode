"""

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        data = []
        
        while root:
            res.append(root.val)
            if root.right:
                data.append(root.right)
            if root.left:
                data.append(root.left)
            root = data.pop() if data else None
                
        return res

    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        data = []
        
        while root or data:
            if not root:
                root = data.pop()
            
            res.append(root.val)
            if root.right:
                data.append(root.right)
            root =  root.left
        return res
