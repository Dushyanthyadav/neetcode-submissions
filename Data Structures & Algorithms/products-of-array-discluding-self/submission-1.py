class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        res = [1] * len(nums)
        zero_count = 0
        index = None;
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                index = i
            if not prefix:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i]*prefix[-1])

        if zero_count >= 2:
            return [0]*len(nums)
        elif zero_count == 1:
            output = [0]*len(nums)
            product = 1
            for i in range(len(nums)):
                if i == index:
                    continue
                product *= nums[i]
            output[index] = product
            return output
        else:
            for i in range(len(nums)):
                if i == 0:
                    res[i] = int(prefix[len(nums)-1]/prefix[i])
                    continue
                res[i] = int(prefix[i-1]*(prefix[len(nums)-1]/prefix[i]))
        return res

