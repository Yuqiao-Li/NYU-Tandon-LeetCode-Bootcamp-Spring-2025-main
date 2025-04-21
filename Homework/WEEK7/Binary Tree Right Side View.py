class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        
        # BFS approach
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.pop(0)
                
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result