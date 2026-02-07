def selection_sort(nums):
    for i in range(len(nums)): 
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
