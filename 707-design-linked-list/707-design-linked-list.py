class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
            
        if cur != self.right and cur and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, thenext, prev = Node(val), self.left.next, self.left
        thenext.prev = node
        prev.next = node
        node.next = thenext
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node, prev, thenext = Node(val), self.right.prev, self.right
        prev.next = node
        thenext.prev = node
        node.next = thenext
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, prev, thenext = Node(val), cur.prev, cur
            prev.next = node
            thenext.prev = node
            node.next  = thenext
            node.prev = prev
            
    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0 :
            cur = cur.next
            index -= 1
            
        if cur and index == 0 and cur.prev and cur.next:
            prev, thenext = cur.prev, cur.next
            prev.next = thenext
            thenext.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)