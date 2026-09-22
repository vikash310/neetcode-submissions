class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []

        for s in strs:
            encoded_str.append(str(len(s)) + "#" + s)
        return "".join(encoded_str)

    def decode(self, strs: str) -> List[str]:
        ans = []
        i = 0
        while i < len(strs):
            delimiter_pos = strs.find("#", i)
            length_substrs = int(strs[i: delimiter_pos])
            i = delimiter_pos + 1
            ans.append(strs[i:i + length_substrs])
            i += length_substrs

        return ans