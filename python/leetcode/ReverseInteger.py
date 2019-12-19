class Solution:
    def reverse(self, x: int) -> int:
        unr = -2**31
        sr = 2**31-1
        sign = ''
        
        if x < 0:
            sign = str(x)[0]
            x = int(str(x)[1:])
        rev = 0
        while x>0:
            rev = rev*10 + (x%10)
            x = x //10
            if rev < unr or rev > sr:
                return 0
        if sign == '-':
            rev = int(sign+str(rev))
            if rev < unr or rev > sr:
                return 0
            return rev
        else:
            return rev
        return 0;