# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr :
            #check where the p and q nodes are
            if p.val > curr.val and q.val > curr.val :
                #both are on right side of the node
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val :
                #both are on the left side of the node
                curr = curr.left
            else :
                # they are on opposite sides of the noe, so the node is the lca
                return curr
        return root