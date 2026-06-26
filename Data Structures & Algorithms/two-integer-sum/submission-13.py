class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexNum = dict()

        for i, num in enumerate(nums):
            if indexNum.get(target - num) is not None:
                return [indexNum.get(target - num), i]
            
            indexNum[num] = i




