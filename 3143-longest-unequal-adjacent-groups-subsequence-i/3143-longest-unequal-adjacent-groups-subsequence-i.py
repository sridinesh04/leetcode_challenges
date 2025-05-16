from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        max_subseq = []

        for i in range(n):
            curr_subseq = [words[i]]
            curr_group = groups[i]
            for j in range(i + 1, n):
                if groups[j] != curr_group:
                    curr_subseq.append(words[j])
                    curr_group = groups[j]
            if len(curr_subseq) > len(max_subseq):
                max_subseq = curr_subseq

        return max_subseq
