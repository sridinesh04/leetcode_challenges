class Solution:
    def scoreOfString(self, s: str) -> int:
      
        return sum(abs(ord(x)-ord(y))for x,y in pairwise(s))