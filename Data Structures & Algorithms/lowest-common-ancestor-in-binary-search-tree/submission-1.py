# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root
        #traverse tree and keep checking where each p and q node are at
        while curr :
            if p.val < curr.val and q.val < curr.val :
                #move to left side of tree
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val :
                #move to the right side of the tree
                curr = curr.right
            else :
                #both are on opposite sides of tree or we are at one 
                #of the nodes and the other is somewhere else.
                return curr