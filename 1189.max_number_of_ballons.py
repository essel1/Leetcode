class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict = {"b":0,"a":0,"l":0,"o":0,"n":0}
        ballon_values = [1,1,2,2,1]
        count = 0
        for letter in text:
            if letter in dict.keys():
                dict[letter] += 1
        values = list(dict.values())
        print(values)
        for i in range(int(len(text)/7)):
            if values == [1,1,2,2,1]:
                return (count+1)
            check_value = [0 if e2 > e1 else e1 for (e1,e2) in zip(values,ballon_values)]
            if 0 in check_value:
                return count
            values = [e1-e2 for (e1,e2) in zip(values,ballon_values)]
            count += 1
            
            
        return  count
    
if __name__ == "__main__":
    output = Solution().maxNumberOfBalloons(text="loonbalxballpoon")
    print(output)