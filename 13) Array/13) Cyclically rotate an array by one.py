# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1#

def rotate( arr, n):
    # insert will do the same process as 
        # 1) Store last element in a variable say x.
        # 2) Shift all elements one position ahead.
        # 3) Replace first element of array with x.
    arr.insert(0, arr.pop())