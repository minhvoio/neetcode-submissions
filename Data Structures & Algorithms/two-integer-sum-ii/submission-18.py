class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        leftIdx, rightIdx = 0, len(numbers) - 1

        while leftIdx < rightIdx:
            leftVal, rightVal = numbers[leftIdx], numbers[rightIdx]

            if target - leftVal == rightVal:
                return [leftIdx + 1, rightIdx + 1]

            if target - rightVal > leftVal:
                leftIdx += 1
                continue

            if target - rightVal < leftVal:
                rightIdx -= 1
                continue
                
