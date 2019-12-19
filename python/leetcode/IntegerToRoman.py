class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: 'I',
                 4: 'IV',
                 5: 'V',
                 9: 'IX',
                 10: 'X',
                 40: 'XL',
                 50: 'L',
                 90: 'XC',
                 100: 'C',
                 400: 'CD',
                 500: 'D',
                 900: 'CM',
                 1000: 'M'}
        
        rom = ''
        while num > 0:
            if num >= 1000:
                rom += roman[1000]*(num//1000) 
                num = num%1000
            elif num >= 900:
                rom += roman[900]*(num//900)
                num = num%900
            elif num >= 500:
                rom += roman[500]*(num//500)
                num = num%500
            elif num >= 400:
                rom += roman[400]*(num//400)
                num = num%400
            elif num >= 100:
                rom += roman[100]*(num//100)
                num = num%100
            elif num >= 90:
                rom += roman[90]*(num//90)
                num = num%90
            elif num >= 50:
                rom += roman[50]*(num//50)
                num = num%50
            elif num >= 40:
                rom += roman[40]*(num//40)
                num = num%40
            elif num >= 10:
                rom += roman[10]*(num//10)
                num = num%10
            elif num >= 9:
                rom += roman[9]*(num//9)
                num = num%9
            elif num >= 5:
                rom += roman[5]*(num//5)
                num = num%5
            elif num >= 4:
                rom += roman[4]*(num//4)
                num = num%4
            else:
                rom += roman[1]*(num//1)
                num = num%1
            
        return rom