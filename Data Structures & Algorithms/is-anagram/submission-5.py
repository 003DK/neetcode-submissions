class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()
        for x in s:
            if x in s_map:
                s_map[x] = s_map[x] + 1
            else:
                s_map[x] = 1
        for x in t:
            if x in t_map:
                t_map[x] = t_map[x] + 1
            else:
                t_map[x] = 1
        return s_map == t_map
        