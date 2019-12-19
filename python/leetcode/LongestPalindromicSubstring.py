class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 1
        max_sub = ''
        sl = len(s)
        #s = 'z'+s
        if sl == 0:
            max_sub = ""
        elif sl == 1:
            max_sub = s[0]
        for i in range(sl-1):
            if s[i] == s[i+1]:
                start,end = i,i+1
                while (start >= 0 and end < sl) and (s[start]==s[end]):
                    if len(s[start:(end+1)]) > len(max_sub):
                        max_sub = s[start:(end+1)]
                    start -= 1
                    end +=1
            if i>0 and s[i-1] == s[i+1]:
                start,end = i-1,i+1
                while (start >= 0 and end < sl) and (s[start]==s[end]):
                    if len(s[start:(end+1)]) > len(max_sub):
                        max_sub = s[start:(end+1)]
                    start -= 1
                    end +=1
        if sl>1 and len(max_sub)<1:
            max_sub=s[0]
        return max_sub