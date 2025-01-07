from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l<r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        return s 
        
        
if __name__ == "__main__":
    output = Solution().reverseString(s=["H","a","n","n","a","h"])
    print(output)
    
    # output: ["o","l","l","e","h"]