def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    aStr = str()
    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1
    for _ in range(len(str(x))):
        aStr, x = aStr + str(x % 10), x/10
    result = int(aStr) * sign
    if abs(result) > 2147483647:
        result = 0
    print type(result)
    return result
