from random import randrange
def quicksort(arr):
  if len(arr)<2:
    return arr
  else:
    pivot = arr.pop(randrange(len(arr)))
    high = [i for i in arr if i>pivot]
    low = [i for i in arr if i<pivot]
    return quicksort(low) + [pivot] + quicksort(high)

arr = [1,5,4,8,9,6,5,7,4,2,5,15,3,10,23,51]
print(quicksort(arr=arr))