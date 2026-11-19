class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res
    def decode(self, s: str) -> List[str]:
        # fnl = []
        # word = ''
        # cnt = ''
        # i=0
        # while(i<len(s)):
        #     if s[i]=='#' and cnt:
        #         temp = int(cnt)+i+1
        #         for k in range(i+1,temp):
        #             if k==len(s) or k>len(s):
        #                 k = temp
        #             else:
        #                 word += s[k]
        #         i = temp-1
        #         fnl.append(word)
        #         word = ''
        #         cnt = ''
        #     elif s[i]!='#':
        #         cnt += s[i]
        #     i += 1
        # return fnl
        fnl = []
        i = 0
        while(i<len(s)):
            f = s.find('#',i)
            cnt = s[i:f]
            i = f+1
            fnl.append(s[i:int(cnt)+i])
            i = int(cnt)+i
        return fnl