class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for letter in magazine:
            if letter in magazine_dict.keys():
                magazine_dict[letter] += 1
            else:
                magazine_dict.update({letter:1})                
        for letter in ransomNote:
            if letter in magazine_dict.keys() and magazine_dict[letter] >=1:
                magazine_dict[letter] -= 1
                print(magazine_dict)
            else:
                return False
        return True
    
    
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ransomNote_list = list(ransomNote)
#         magazine_list = list(magazine)
#         diff = [letter for letter in ransomNote if letter not in magazine_list]
#         print(diff)
        
if __name__ == "__main__":
    output = Solution()
    print(output.canConstruct(ransomNote="aabb",magazine="aab"))