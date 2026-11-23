class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        i=0;j=i+1
        st=set()
        st.add(s[i])
        ans=float("-inf")
        while(i<j<len(s)):
            while(s[j] in st):
                st.remove(s[i])
                i+=1
            st.add(s[j])
            j+=1
            ans = max(len(st), ans)
        return ans