def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    fbList = []
    for num in range(1, n + 1):
        if num % 15 == 0:
            fbList.append('FizzBuzz')
        elif num % 5 == 0:
            fbList.append('Buzz')
        elif num % 3 == 0:
            fbList.append('Fizz')
        else:
            fbList.append(str(num))
    return fbList
