def samelen(strs):
    strs = sorted(strs, key=len)
    analist = []
    dumpy = []
    current_len = len(strs[0])
    i = 0
    while i < len(strs):
        if len(strs[i]) == current_len:
            dumpy.append(strs[i])
        else:
            analist.append(dumpy[0:len(dumpy)])
            dumpy.clear()
            current_len = len(strs[i])
            dumpy.append(strs[i])
            
        if i == len(strs)-1:
            analist.append(dumpy[0:len(dumpy)])
        i += 1

    return analist

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_analist = samelen(strs)  
        analist = []

        for li in sorted_analist:
            a = {}
            for word in li:
                sorted_word = "".join(sorted(word))

                if sorted_word in a:
                    a[sorted_word].append(word)
                else:
                    a[sorted_word] = [word]
            for (key, values) in a.items():
                analist.append(values)

        return analist

                       



