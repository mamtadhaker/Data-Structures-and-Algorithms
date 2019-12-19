class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sl = len(s)
        output = ''
        if numRows == 1 or sl < 1:
            return s
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                for j in range(i, sl,((numRows - 1)*2)):
                    output = output + s[j]
            else:
                j = i
                k = 0
                while j < sl:

                    output = output + s[j]
                    if k%2 == 0:
                        j += (numRows-i-1)*2
                    else:
                        j += (i)*2
                    k += 1
        return output