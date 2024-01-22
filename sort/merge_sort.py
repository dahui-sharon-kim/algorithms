def merge_sort(arr):
  # 길이가 1인 리스트만 남도록 계속 쪼개기
  if (len(arr) < 2):
    return arr
  mid = len(arr) // 2
  former_arr = merge_sort(arr[:mid])
  latter_arr = merge_sort(arr[mid:])

  merged_arr = []
  f = l = 0
  while (f < len(former_arr) and l < len(latter_arr)):
    if (former_arr[f] < latter_arr[l]):
      merged_arr.append(former_arr[f]) 
      f += 1
    else:
      merged_arr.append(latter_arr[l])
      l += 1

  merged_arr += former_arr[f:]
  merged_arr += latter_arr[l:]
  return merged_arr

print(merge_sort([4, 5, 1, 2, 3, 6]))
