def first():
  a = [7, 5, 7, 5, 1, 2, 6, 1, 1, 6, 7, 8, 5, 7, 4]
  print(a)
  l = a[0]
  for i in a:
      if i == l:
          a.remove(i)
  return a


def second():
  l = [5, 5, 1, 2, 6, 1, 1, 6, 8, 5, 4]
  l.remove(max(l))
  return l


def min_item():
  l = [8, 5, 9, 6, 4, 2, 3, 1, 7, 5, 8, 1, 12]
  mn = min(l)
  l[l.index(mn)] = 0
  return l


def last():
  l = [8, 5, 9, 6, 4, 2, 3, 1, 7, 5, 8, 1, 12]
  print(l)
  a = l[0]
  l[0] = l[-1]
  l[-1] = a
  return l
