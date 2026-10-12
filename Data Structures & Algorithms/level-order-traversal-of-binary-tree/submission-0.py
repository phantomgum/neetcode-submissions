from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #empty tree
        if not root :
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue :
            #take note of the current length of the queue for the current level
            qLen = len(queue)
            level = []
            #loop through queue level and add nodes to the list
            for i in range(qLen) :
                node = queue.popleft()
                level.append(node.val)
                #now add its children to the queue
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            #add that list to the output list
            result.append(level)
        
        return result