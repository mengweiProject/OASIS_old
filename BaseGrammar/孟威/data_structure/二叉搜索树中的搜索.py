'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/31 17:31 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)


