class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m1={}
        for c in s:
            m1[c] = m1.get(c,0)+1
        m2={}
        for c in t:
            if c not in m1 or m2.get(c,0)>m1.get(c):
                return False
            m2[c] = m2.get(c,0)+1
        for key,val in m1.items():
            if m2.get(key)!=val:
                return False
        return True