class MyCircularDeque(object):

    def __init__(self, k):
    
        self.deque = [None] * k
        self.maxsize = k
        self.size =  0
        self.head = 0
        self.tail = 0
        

    def insertFront(self, value):
    
        if self.isEmpty():
            self.deque[self.head] = value
            self.size += 1
            return True
        elif not self.isFull():
            self.head = (self.head - 1) % self.maxsize
            self.deque[self.head] = value
            self.size += 1
            
            return True
        else:
            return False
        

    def insertLast(self, value):
        if self.isEmpty():
            self.deque[self.tail] = value
            self.size += 1
            return True
        
        elif not self.isFull():
            self.tail = (self.tail + 1) % self.maxsize
            self.deque[self.tail] = value
            self.size += 1
            return True 
        else:
            return False
 
        

    def deleteFront(self):
        if not self.isEmpty():
            self.deque[self.head] = None
            if self.size != 1:
                self.head = (self.head + 1) % self.maxsize
            self.size -= 1
            return True
        else:
            return False
            
            
    def deleteLast(self):
        if not self.isEmpty():
            self.deque[self.tail] = None
            if self.size != 1:
                self.tail = (self.tail - 1) % self.maxsize
            self.size -= 1
            return True
        else:
            return False
        

    def getFront(self):
        
        return self.deque[self.head] if not self.isEmpty() else -1
     
        

    def getRear(self):
        return self.deque[self.tail] if not self.isEmpty() else -1
     
    
        

    def isEmpty(self):
        return self.size == 0
        

    def isFull(self):
        return self.size == self.maxsize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()