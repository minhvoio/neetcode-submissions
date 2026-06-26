class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexNum = dict()
        setNum = set(nums)
        for i, num in enumerate(nums):
            indexNum[num] = i

        for i, num in enumerate(nums):
            if (target - num) in setNum and i != indexNum.get(target - num):
                return [i, indexNum.get(target - num)]

        return False