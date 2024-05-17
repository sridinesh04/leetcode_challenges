class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        dict = 0
        for j in jewels:
            if j in counter:
                dict += counter[j]
        return dict    