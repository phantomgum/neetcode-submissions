from collections import deque
class Solution:

    def isValid(self, s: str) -> bool:
        #we'll loop through the brackets and whenever we see opening put in stack
        #if we see a closing then pop the stack and the opening should match the closing

        stack = deque()
        #use a dictionary to connect the opening to the closing brackets
        pairs = {")" : "(", "}" : "{", "]" : "["}
        for bracket in s :
            #if its an opening bracket, add it to the stack
            if bracket in '({[':
                stack.append(bracket)
            #check if its a closing bracket
            if bracket in ')}]' :
                #check if the stack is empty
                if not stack :
                    return False
                #now check if this closing matches the recent open
                if stack[-1] == pairs[bracket] :
                    stack.pop()
                else :
                    return False
                
        if len(stack) == 0 :
            return True
        else :
            #there are still some brackets in the stack
            return False

    