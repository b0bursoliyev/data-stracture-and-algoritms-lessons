# listda yo'q elementlar berilsa error beryabdi
myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# myList = [i for i in input().split()]
print(myList)
x = int(input())
low = 0
high = len(myList)
while low<high and low>=0 and high>0:
  m = (low+high)//2
  if x==myList[m]:
    out = myList.index(x)
    break
  elif x>myList[m]:
    low = m+1
  elif x<myList[m]:
    high = m

NameError('None')
print("Output: ",out)
