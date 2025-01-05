class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict = {}
        s_length = len(s)
        t_length = len(t)

        if s_length > t_length:
            first_word = t
            second_word = s
        else:
            first_word = s
            second_word = t

        for letter in first_word:
            if letter in letter_dict.keys():
                letter_dict[letter] += 1
            else:
                letter_dict.update({letter:1})
        for letter in second_word:
            if letter not in letter_dict.keys():
                return False
            else:
                letter_dict[letter] -= 1
                if letter_dict[letter] < 0:
                    return False
        return True
    
if __name__ == "__main__":
    output = Solution()
    print(output.isAnagram(s="rat",t="car"))