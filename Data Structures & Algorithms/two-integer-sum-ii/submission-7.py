class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        numDex = dict()

        for idx, num in enumerate(numbers):
            numDex[num] = idx + 1

        for idx, num in enumerate(numbers):
            currentIdx = idx + 1
            if numDex.get(target - num) and currentIdx < numDex.get(target - num):
                return [currentIdx, numDex.get(target - num)]
                
