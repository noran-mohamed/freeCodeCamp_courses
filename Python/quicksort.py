def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    sub1 = []
    sub2 = []
    sub3 = []
    
    for num in nums:
        if num < pivot:
            sub1.append(num)
        elif num > pivot:
            sub3.append(num)
        else:
            sub2.append(num)

    sorted_nums = quick_sort(sub1) + sub2 + quick_sort(sub3)
    return sorted_nums

print(quick_sort([20, 3, 14, 1, 5]))
