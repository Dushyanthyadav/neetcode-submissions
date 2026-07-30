class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in a.items():
            bucket[freq].append(num)

        result = []
        for buck in range(len(bucket)-1, 0, -1):
            for num in bucket[buck]:
                result.append(num)
                if len(result) == k:
                    return result


        