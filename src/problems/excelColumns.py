def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    countNum = 0
    if not s: return countNum
    idx = len(s) - 1
    n = len(s) - 1
    while idx > -1:
        countNum += (26 ** (n - idx)) * (ord(s[idx]) - 64)
        idx -= 1
    return countNum
