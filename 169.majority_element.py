from typing import List
from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_length = len(nums)
        majority_factor = floor(nums_length/2)
        nums_set = set(nums)
        nums_dict = {num:nums.count(num) for num in nums_set }
        
        max_value = 0
        for key,value in nums_dict.items():
            if value >= max_value:
                max_value = value
                answer = key

        return answer

if __name__ == "__main__":
    output = Solution().majorityElement(nums=[2,2,1,1,1,2,2])
    print(output)