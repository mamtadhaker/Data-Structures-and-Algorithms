class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniquec = set()
        cur_len = 0
        max_len = 0
        prev_pos = dict()       
        sl = len(s)
        i=0
        for j in range(i,sl):
            if s[j] not in prev_pos:
                prev_pos[s[j]] = j
                cur_len = len(s[i:j+1])
            else:
                if cur_len > max_len:
                    max_len = cur_len
                i = max(prev_pos[s[j]]+1,i)
                prev_pos[s[j]] = j
                if j+1<=sl:
                    cur_len = len(s[i:j+1])
        if cur_len > max_len:
            max_len = cur_len
        return max_len