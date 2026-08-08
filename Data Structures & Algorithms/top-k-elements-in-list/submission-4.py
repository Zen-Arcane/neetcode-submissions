class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = 0
        l=[]

        counts = {}


        for i in nums:

            counts[i] = counts.get(i,0) + 1
        

        for t in sorted(counts, key=lambda x: counts[x], reverse=True):
            if c < k:
                l.append(t)
                c+=1

          
        return l

