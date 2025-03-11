class Solution(object):
    def reverseWords(self, s):
        words = []
        word = []
        for char in s:
            if char != ' ':
                word.append(char)
            elif word:  
                words.append(''.join(word))
                word = []
        
        # last word
        if word:
            words.append(''.join(word))
        
        # reverse
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        return ' '.join(words)