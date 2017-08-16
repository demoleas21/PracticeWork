def moveZeros(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    zero = 0
    current = 0
    while current < len(nums):
        if nums[current] != 0:
            nums[zero] = nums[current]
            zero += 1
        current += 1
    nums[zero:] = [0] * (len(nums) - zero)
    return nums
