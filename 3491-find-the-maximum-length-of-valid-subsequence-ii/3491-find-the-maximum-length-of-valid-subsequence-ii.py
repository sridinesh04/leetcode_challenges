from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1  # Each element itself is a valid subsequence
        
        for i in range(n):
            for j in range(i):
                mod_val = (nums[j] + nums[i]) % k
                # Extend subsequence ending at j with same mod_val
                dp[i][mod_val] = max(dp[i][mod_val], dp[j][mod_val] + 1)
            # Starting new subsequence at i
            for mod in range(k):
                dp[i][mod] = max(dp[i][mod], 1)
            max_len = max(max_len, max(dp[i].values()))
        
        return max_len
