class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = 0 - num
            left, right = i + 1, len(nums) - 1

            while left < right:
                if target - nums[right] == nums[left]:
                    ans.append([nums[left], nums[right], num])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif target - nums[right] > nums[left]:
                    left += 1
                else: 
                    right -= 1
                
        return ans

