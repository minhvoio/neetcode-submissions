class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "@" + s

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = s.find("@", i)

            length = int(s[i:j])
            content = s[j + 1 : j + 1 + length]

            i = j + 1 + length
            res.append(content)

        return res