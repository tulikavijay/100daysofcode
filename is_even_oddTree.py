# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = [root]
        turn = 0
        level = [root]
        while level:
            new_level = []
            # even indexed. odd int. strictly increasing
            last_seen = None
            for node in level:
                if turn %2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if node.val and last_seen and node.val <= last_seen:
                        return False
                    last_seen = node.val
                else:
                    if node.val % 2 != 0:
                        return False
                    if node.val and last_seen and node.val >= last_seen:
                        return False
                    last_seen = node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            turn += 1
            level = new_level
        return True
            
                    
