import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        
        First reversing the word with only alphanumeric value and comparing
        
        
        reverse_s = [char.lower() for char in s if char.isalnum()==True]
        s = "".join(reverse_s)
        l = 0
        r = len(s) - 1
        while l < r:
            temp = reverse_s[l]
            reverse_s[l] = reverse_s[r]
            reverse_s[r] = temp
            l += 1
            r -= 1
        reverse_string = "".join(reverse_s)
        if s == reverse_string:
            return True
        else:
            return False
            
        """
        
        
        """
        Implementing the checking mechanism inside the loop instead of comparing the entire strings. 
        Runtime wasn't that much fast than the above.
        
        reverse_s = [char.lower() for char in s if char.isalnum()==True]
        l = 0
        r = len(reverse_s) - 1
        while l < r:
            if reverse_s[l] == reverse_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
        """
        # pattern = "[\W]"
        s = s.lower()
        pattern = "[^a-z0-9]"
        reverse_s = re.sub(pattern,"",s)
        print(reverse_s)
        l = 0
        r = len(reverse_s) - 1
        while l < r:
            print(l,r)
            if reverse_s[l] == reverse_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
        
            
        
        
if __name__ == "__main__":
    output = Solution().isPalindrome(s="ab_a")
    print(output)
            
        