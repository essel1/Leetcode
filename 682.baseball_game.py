from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = []
        print(operations)
        operations = operations[::-1]
        # print(operations.pop())
        while operations != []:
            char = operations.pop()
            # print(char)
            match char:
                case "+":
                    num_1 = answer[-1]
                    num_2 = answer[-2]
                    answer.append(num_1+num_2)
                case "C":
                    answer.pop()
                case "D":
                    num_1 = answer[-1]
                    answer.append(num_1 * 2)
                case _:
                    answer.append(int(char))
                
        # print(answer)
        sum = 0
        for i in range(len(answer)):
            sum += int(answer[i])
        
        return sum
    
if __name__ == "__main__":
    output = Solution().calPoints(operations=["5","2","C","D","+"])
    print(output)