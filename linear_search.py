myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# myList = [i for i in input().split()]
x = int(input())
def lin_search(myList,x):
  for i in myList:
    if i==x:
      output = myList.index(i)
      break
    else:
      output = None
  return output
print(lin_search(myList,x))