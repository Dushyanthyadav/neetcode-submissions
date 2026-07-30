class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 0
        
        mylist = [(key, value) for key, value in a.items()]

        for i in range(len(mylist)):
            for j in range(i+1,len(mylist)):
                if mylist[i][1] < mylist[j][1]:
                    a = mylist[j]
                    mylist[j] = mylist[i]
                    mylist[i] = a
        
        li = []
        for i in range(k):
            li.append(mylist[i][0])
    
        return li



        