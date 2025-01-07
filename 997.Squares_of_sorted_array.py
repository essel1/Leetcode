from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        The trivial way of squaring the nums and sorting them....
        
        squared_nums = [num ** 2 for num in nums]
        squared_nums.sort()
        return squared_nums
        
        """
        nums_length = len(nums)
        squared_nums = [1] * nums_length
        l = 0 
        r = nums_length - 1
        while l <= r:
            if nums[l] < 0:
                l_absolute = abs(nums[l])
                if l_absolute >= nums[r]:
                    squared_nums[r-l] = (l_absolute) ** 2
                    l += 1
                else:
                    squared_nums[r-l] = nums[r] ** 2
                    r -= 1
            else:
                squared_nums[r-l] = nums[r] ** 2
                r -= 1
        return squared_nums
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    output = Solution().sortedSquares(nums=[-12,-7,-3,2,3,11])
    print(output)
    # Output : [4,9,9,49,121,144]