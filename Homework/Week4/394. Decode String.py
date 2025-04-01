class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                encoded = ""
                while stack and stack[-1] != '[':
                    encoded = stack.pop() + encoded
                
                stack.pop()  # Remove '['
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(encoded * int(k))
        
        return "".join(stack)