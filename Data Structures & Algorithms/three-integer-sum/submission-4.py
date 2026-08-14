class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 3 and sum(nums) != 0:
            return []
        
        nums.sort()
        ans = []

        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            leftIdx, rightIdx = idx + 1, len(nums) - 1

            while leftIdx < rightIdx:
                left = nums[leftIdx]
                right = nums[rightIdx]
                complement = 0 - num - left

                if complement == right:
                    ans.append([num, left, right])

                    while leftIdx < rightIdx and nums[leftIdx] == left:
                        leftIdx += 1

                    while leftIdx < rightIdx and nums[rightIdx] == right:
                        rightIdx -= 1

                elif complement < right:
                    rightIdx -= 1

                else: 
                    leftIdx += 1

        return ans