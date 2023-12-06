def bianry_search(list, item):
  low = 0
  high = len(list)
  while low < high and high > 0 and low >= 0:
    mid = (high + low) // 2
    guess = list[mid]
    if guess == item:
      return mid
    elif guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None


myList = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]
item = 23
# item = int(input())
print(bianry_search(myList, item))