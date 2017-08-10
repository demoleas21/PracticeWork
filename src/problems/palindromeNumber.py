def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    y = x
    pal = 0
    while y > 0:
        y, pal = y / 10, pal * 10 + y % 10
    if pal == x:
        return True
    else:
        return False
