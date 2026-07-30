class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for word in strs:
            mystr += str(len(word))
            mystr += '#'
            for letter in word:
                mystr += chr(ord(letter) ^ 1)
        
        return mystr

    def decode(self, s: str) -> List[str]:
        i = 0
        mylist = []
        length = 0
        word_length = ""
        mystr = ""
        while i < len(s):
            if s[i] == '#':
                length = int(word_length)
                for j in range(length):
                    mystr += chr(ord(s[i+1+j]) ^ 1)
                i += length+1
                length = 0
                mylist.append(mystr)
                mystr = ""
                word_length = ""
            else:
                word_length += s[i]
                i += 1

        return mylist
