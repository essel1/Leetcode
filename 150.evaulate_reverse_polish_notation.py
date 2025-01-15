from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char in ["+","*","/","-"]:
                num_1 = stack.pop()
                num_2 = stack.pop()
                if char == "+":
                    stack.append(num_1+num_2)
                elif char == "*":
                    stack.append(num_1*num_2)
                elif char == "/":
                    stack.append(int(num_2/num_1))
                else:
                    stack.append(num_2 - num_1)
            else:
                stack.append(int(char))
        return stack.pop()




if __name__ == "__main__":
    output = Solution().evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(output)