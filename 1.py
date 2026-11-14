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

    max_element = nums[0]

    for num in counts:
        if counts[num] > counts[max_element]:
            max_element = num

    return max_element


nums = list(map(int, input("Sonlarni kiriting: ").split()))

print("Eng ko'p takrorlangan son:", majority_element(nums))


