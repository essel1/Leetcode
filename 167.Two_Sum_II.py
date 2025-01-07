from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l: index1
        # r: index2
        l = 0 
        check_number = float('inf')
        nums_length = len(numbers)
        while l < nums_length:
            if check_number == numbers[l]:
                l += 1
                continue
            # for r in range(nums_length - 1,l,-1):
            for r in range(l+1,nums_length):
                if numbers[l] + numbers[r] == target:
                    return [l+1,r+1]
            check_number = numbers[l]
            l += 1
        return [] 



if __name__ == "__main__":
    output = Solution().twoSum(numbers=[2,3,4],target=6)
    print(output)        