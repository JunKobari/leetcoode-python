# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        s=1
        e=n      
        while(s<e):
            pos=s+(e-s)//2            
            if isBadVersion(pos):
                e=pos                
            else:
                s=pos+1
        return s
        