class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for word in strs:
            for letter in word:
                value = chr(ord(letter) ^ 1)
                mystr += value
            mystr += chr(0x0101)
        return mystr

    def decode(self, s: str) -> List[str]:
        mylist = []
        
        mystr = ""
        for i in s:
            if ord(i) == 0x0101:
                mylist.append(mystr)
                mystr = ""
            else:
                mystr += chr(ord(i) ^ 1)
        
        return mylist
