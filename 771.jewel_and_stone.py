class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_pair = {}
        count = 0 
        for jewel in jewels:
            jewel_pair.update({jewel:""})
        
        for stone in stones:
            if stone in jewel_pair.keys():
                # print(count)
                count += 1
        return count
    
if __name__ == "__main__":
    output = Solution()
    print(output.numJewelsInStones(jewels="z",stones="ZZ"))
    