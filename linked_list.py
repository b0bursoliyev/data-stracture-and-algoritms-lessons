class Node:
  def __init__(self,data) -> None:
    self.data = data
    self.next = None

class Linkedlist:
  def __init__(self):
    self.head = None

  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def push(self,new_data):
    new_data = Node(new_data)
    new_data = self.head
    self.head = new_data
    return True


llist = Linkedlist()
llist.head = Node("Dushanba")
l2 = Node('Seshanba')
llist.head.next = l2
l3 = Node("Chorshanba")
l2.next = l3
l4 = Node("Payshanba")
l3.next = l4


#print(llist.head.next.next.data)
print(llist.push("Juma"))
print(llist.printList())