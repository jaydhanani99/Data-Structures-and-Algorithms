# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
# https://practice.geeksforgeeks.org/problems/reverse-a-string/1

def reverseWord(s):
    n = len(s)
    output = ""
    return s[:n//2:-1]+s[n//2::-1]