class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for s in strs:
            freqS = [0] * 26

            for c in s:
                freqS[ord(c) - 97] += 1

            ans[tuple(freqS)].append(s)

        return list(ans.values())
        