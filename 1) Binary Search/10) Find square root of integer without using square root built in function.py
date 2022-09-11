import math
# @param A : integer
def sqrt(A):
    # We start using binary search between 0 and A/2 when encounter mid*mid = A then we return mid.
    low     =   0
    high    =   math.ceil(A/2)
    ans     =   0
    while(low <= high):
        mid     =   (low + (high - low)//2)
        mul     =   mid*mid
        if(mul == A):
            return mid
        elif(mul < A):
            # This can be possible answer similar question to floor value as if perfect square is not found we need to return floor
            ans     =   mid
            low     =   mid + 1
        else:
            high    =   mid - 1
    return ans

print(sqrt(5))