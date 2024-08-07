class Solution(object):
    def reverseParentheses(self, s):
        char_stack = []
        
        s = "((" + s + "))"
        
        result = ""
        
        for char in s:
            if not char_stack or char != ')':
                char_stack.append(char)
            else:
                temp = []
                
                while char_stack[-1] != '(':
                    temp.append(char_stack.pop())
                
                char_stack.pop()  # pop '('
                
                result = ''.join(temp)
                
                for t in temp:
                    char_stack.append(t)
        
        return result