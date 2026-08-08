class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l={}

        if len(s) != len(t):
            return False

        for i in s:
            l[i] = l.get(i,0)+1
        
        for j in t:
            if j not in l:
                return False
            
            l[j]-=1

            if l[j] < 0:
                return False
        return True
        



        