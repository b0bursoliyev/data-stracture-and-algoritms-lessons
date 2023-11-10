def sum(arr):
  if len(arr)==1:
    return 1
  else:
    return arr.pop()+sum(arr)
arr = [1,15,8,6,2,5,4,8,9,5,0]
print(sum(arr=arr))