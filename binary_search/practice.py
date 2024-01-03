# def bin_search(arr, val, low=None, high=None):  
#   low, high = low or 0, high or len(arr) - 1
#   mid = (low + high) // 2
#   if low > high:
#     return -1
#   if arr[mid] < val:
#     return bin_search(arr, val, mid+1, high)
#   if arr[mid] > val:
#     return bin_search(arr, val, low, mid)
#   if arr[mid] == val:
#     return mid

# print(bin_search(["a", "b", "c", "d", "e", "f", "g", "h"], "b"))

def bin_search(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] > target:
      high = mid - 1
    if arr[mid] < target:
      low = mid + 1