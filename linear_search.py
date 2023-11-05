myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# myList = [i for i in input().split()]
x = int(input())
def lin_search(myList,x):
  for i in range(len(myList)):
    if myList[i]==x:
      return i
  return None
print(lin_search(myList,x))