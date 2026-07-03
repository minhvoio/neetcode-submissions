class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            lenS = len(s)
            result += str(lenS) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = s.find("#", i)
            lenS = int(s[i:j])

            content = s[j+1: j+1+lenS]
            res.append(content)
            i = j + 1 + lenS

        return res