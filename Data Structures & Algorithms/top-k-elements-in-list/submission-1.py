class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 0
        
        mylist = [(key, value) for key, value in a.items()]

        mylist.sort(key=lambda x: x[1], reverse=True)

        li = []
        for i in range(k):
            li.append(mylist[i][0])
    
        return li



        