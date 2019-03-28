def countSetBits( n ): 
    count = 0
    while n: 
        print(n,count)
        count += n & 1
        n >>= 1
    return count 
      
# Function that return count of 
# flipped number 
def FlippedCount(a , b): 
  
    # Return count of set bits in 
    # a XOR b 
    return countSetBits(a^b) 
  
# Driver code

if '__name__' == '__main__':
    a = 10
    b = 20
    print(FlippedCount(a, b)) 