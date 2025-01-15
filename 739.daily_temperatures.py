from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        # temperatures = temperatures[::1]
        stack = []
        for i in range(len(temperatures)):
            if stack == []:
                stack.append(i)
            else:
                while temperatures[stack[-1]] < temperatures[i]:
                    prev_index = stack.pop()
                    answer[prev_index] = i - prev_index
                    if stack == []:
                        break
                stack.append(i)
        return answer       
            
        


if __name__ == "__main__":
    output = Solution().dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73])
    print(output)