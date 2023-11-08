def max(arr):
  t = arr[0]
  for i in arr:
    if i>t:
      t = i
  return t

def selection_sort(arr):
  sorted_arr = []
  while arr:
    a = max(arr)
    sorted_arr.append(a)
    arr.remove(a)
  return sorted_arr
arr = [12,35,6,58,4,5,6,9,45,8]
print(selection_sort(arr))