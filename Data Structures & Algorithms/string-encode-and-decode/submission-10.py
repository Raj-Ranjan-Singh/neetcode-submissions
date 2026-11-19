class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res
    def decode(self, s: str) -> List[str]:
        fnl = []
        i = 0
        while(i<len(s)):
            f = s.find('#',i)
            cnt = s[i:f]
            i = f+1
            fnl.append(s[i:int(cnt)+i])
            i = int(cnt)+i
        return fnl