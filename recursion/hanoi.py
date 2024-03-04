def binary_search(arr, target, low=None, high=None):
    low, high = 0 or low, len(arr) - 1 or high
    mid = len(arr) // 2
    mid_num = arr[mid]

    if (target < mid_num):
        return binary_search(arr[])