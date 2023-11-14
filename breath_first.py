from collections import deque

def search(start,target):
    search_deque = deque()
    search_deque += graph[start]
    searched = set()

    while search_deque:
      person = search_deque.popleft()
      if person not in searched:
        if person==target:
          print(f"{target} ni topdik")
          return True
        else:
          search_deque += graph[person]
          searched.append(person)
    return False