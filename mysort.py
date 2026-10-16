def my_sort(nums: list):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums)//2]

    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return my_sort(less) + equal + my_sort(greater)