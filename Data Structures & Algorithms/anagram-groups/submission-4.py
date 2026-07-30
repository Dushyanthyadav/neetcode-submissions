class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for word in strs:
            mylist = [0] * 26

            for letter in word:
                mylist[ord(letter) - 97] += 1
            
            mylist = tuple(mylist)
            if mylist in a:
                a[mylist].append(word)
            else:
                a[mylist] = [word]
        
        return list(a.values())
