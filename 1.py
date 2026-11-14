# 1 masala


def majority_element(nums: list) -> int:
    if not nums:
        return -1

    counts = {}

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_elemen

nums = [2, 2, 1, 1, 1, 2, 2]

print(majority_element(nums))
t = nums[0]

    for num in counts:
        if counts[num] > counts[max_element]:
            max_element = num
    return max_element
