# https://leetcode.com/problems/powx-n/
# https://www.interviewbit.com/problems/implement-power-function/
def power(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    if power == -1:
        return 1/base
    blnInverse = True if power < 0 else False
    power = abs(power)
    result = 1
    while power > 0:
        if power % 2 == 0:
            base = base*base
            power = power//2
        else:
            result = result*base
            power = power - 1
    return result if blnInverse == False else 1/result

print(power(4, 17))