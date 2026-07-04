class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count0 = 0
        product = 1
        index0 = None

        for i, n in enumerate(nums):
            if n == 0:
                count0 += 1
                index0 = i
                if count0 > 1:
                    return [0]*len(nums)
            else:
                product *= n

        res = [0] * len(nums)
        
        if count0 == 1:
            res[index0] = product
            return res
        
        for i in range(len(nums)):
            res[i] = product // nums[i]

        return res
