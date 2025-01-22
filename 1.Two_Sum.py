from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print(i)
            num = nums[i]
            remaining = target - num
            print(remaining)
            nums_updated = nums[:i]+nums[i+1:]
            print(nums_updated)
            if remaining in nums_updated:
                output = [i,nums.index(remaining,i+1)]
                return output
                    
                        
        return None
        # nums_dict = {key:target-key for key in nums}
            
        






if __name__ == "__main__":
    output = Solution().twoSum(nums=[-10,-1,-18,-19],target=-19)
    print(output)