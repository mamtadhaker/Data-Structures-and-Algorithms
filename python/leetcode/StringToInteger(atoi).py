class Solution:
    def myAtoi(self, str: str) -> int:
        sl = len(str)
        out = ''
        sign = ''
        for i in range(sl):
            if str[i] in (['+','-']) and sign not in (['+',"-"]) :
                sign = str[i]
                j = i+1
                while(j < sl and str[j].isdigit()):
                    out += str[j]
                    j += 1
                break
            elif str[i] == ' ':
                pass
            elif str[i].isdigit() and len(sign)<=1:
                j = i
                while(j < sl and str[j].isdigit()):
                    out += str[j]
                    j += 1
                break  
            else:
                break
        print(sign,out)
        if out == '':
            return 0
        elif int(sign+out) >= -2**31 and int(sign+out) <= 2**31-1:
            return int(sign+out)
        elif int(sign+out) < -2**31 :
            return -2**31
        elif int(sign+out) > (2**31 - 1):
            return 2**31-1
        else:
            return 0
        