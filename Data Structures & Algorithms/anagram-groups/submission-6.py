class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        def freqS(s: str):
            freq = [0]*26

            for c in s:
                freq[ord(c) - 97] += 1

            return tuple(freq)

        for s in strs:
            countCharS = freqS(s)
            ans[countCharS].append(s)

        return list(ans.values())
        