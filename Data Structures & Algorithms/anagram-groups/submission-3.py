class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #This solution i have to check it up
        a = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in a:
                a[sorted_word].append(word)
            else:
                a[sorted_word] = [word]

        return list(a.values()) 