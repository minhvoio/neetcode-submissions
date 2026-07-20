class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        num_set = set(nums)
        starts = []

        for num in nums:
            if num - 1 not in num_set:
                starts.append(num)

        longest = 1
        
        for start in starts:
            count = 1

            while start + 1 in num_set:
                count += 1
                start += 1
                if count > longest:
                    longest = count

        return longest
