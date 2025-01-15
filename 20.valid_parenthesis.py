class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ["(","[","{"]:
                stack.append(char)
            else:
                if stack == []:
                    return False
                else:
                    checking_str = stack.pop()
                    if char == ")" and checking_str == "(":
                        continue
                    elif char == "]" and checking_str == "[":
                        continue
                    elif char == "}" and checking_str == "{":
                        continue
                    else:
                        return False      
        if stack == []:
            return True
        else: return False  
        
        
        
        
if __name__ == "__main__":
    output = Solution().isValid(s="((")
    print(output)