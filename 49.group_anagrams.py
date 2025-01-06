from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        word_dict = {word:(strs.count(word),{letter:word.count(letter) for letter in set(word)}) for word in strs}
        word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1][0],reverse=True))
        while bool(word_dict):
            first_word = list(word_dict.keys())[0]
            dictionary = word_dict[first_word][1]
            
            words = [key for key,value in word_dict.items() if value[1] == dictionary]
            count = strs.count(first_word)
            
            if count > 1:
                repeating_words = [first_word] * (count-1)
                # print(repeating_words)
                words.extend(repeating_words)
            answer.append(words)
            word_dict = {key:value for key,value in word_dict.items() if key not in words}
        return answer
            
        
        
        
if __name__ == "__main__":
    output = Solution().groupAnagrams(strs=["rag","orr","err","bad","foe","ivy","tho","gem","len","cat","ron","ump","nev","cam","pen","dis","rob","tex","sin","col","buy","say","big","wed","eco","bet","fog","buy","san","kid","lox","sen","ani","mac","eta","wis","pot","sid","dot","ham","gay","oar","sid","had","paw","sod","sop"])
    print(output)
    # [["sop"],["sod"],["paw"],["oar"],["dot"],["ani"],["sen"],["kid"],["nev"],["ump"],["rob"],["cam","mac"],["len"],["gem"],["eta"],["tex"],["gay"],["sin"],["cat"],["wis"],["eco"],["tho"],["had"],["foe"],["bad"],["rag"],["ivy"],["orr"],["bet"],["pen"],["dis","sid","sid"],["lox"],["ron"],["col"],["buy","buy"],["ham"],["err"],["say"],["big"],["pot"],["wed"],["fog"],["san"]]