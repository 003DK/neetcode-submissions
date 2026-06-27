class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h=''
        if len(s)>len(t):
            h=s
        else:
            h=t
        for i in h:
            if s.count(i) != t.count(i):
                return False
        return True