class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 1
        max_sub = ''
        sl = len(s)
        for i in range(1,sl-1):
            if s[i-1] == s[i]:
                start,end = i-1,i
                while (s[start]==s[end]) and (start >= 0 and end < sl):
                    if len(s[start:end+1]) > len(max_sub):
                        max_sub = s[start:end+1]
                    start -= 1
                    end +=1
            elif s[i-1] == s[i+1]:
                start,end = i-1,i+1
                while (s[start]==s[end]) and (start >= 0 and end < sl):
                    if len(s[start:end+1]) > len(max_sub):
                        max_sub = s[start:end+1]
                    start -= 1
                    end +=1
        return max_sub   