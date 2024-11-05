arrayOne = [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1]
arrayTwo = [1, 0, 1, 0, 1, 0, 1, 0]
arrayThree = [0, 0, 1]

def orderedArray(nums):
    low, high = 0, len(nums) - 1

    while (low < high):
        if nums[low] == nums[high]:
            if nums[high] == 1:
                high = high - 1
            else:
                low = low + 1 
        else:
            if nums[high] == 0:
                nums[low], nums[high] = nums[high], nums[low]
                low = low + 1
            high = high - 1   
    return nums

print(orderedArray(arrayOne))
print(orderedArray(arrayTwo))
print(orderedArray(arrayThree))