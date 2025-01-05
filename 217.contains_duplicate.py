from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False
    
if __name__ == "__main__":
    output = Solution()
    print(output.containsDuplicate(nums = [1,2,3,4]))
                