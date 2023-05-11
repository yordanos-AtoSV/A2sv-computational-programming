class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def heappeak(self, heap):
        temp = heappop(heap)
        heappush(heap, temp)
        
        return temp

    def addNum(self, num: int) -> None:
        
        if not self.maxheap:
            heappush(self.maxheap, -num)
            return
        
        val1= -self.heappeak(self.maxheap)        
        if num >= val1 and len(self.minheap) <= len(self.maxheap):
            heappush(self.minheap, num)
            
        elif num > val1 and  len(self.minheap) > len(self.maxheap):
            
            val2  = self.heappeak(self.minheap)
            if val2 < num:
                minim = heappop(self.minheap)
                heappush(self.maxheap, -minim)
                heappush(self.minheap, num)
            else:
                heappush(self.maxheap, -num )
            
        elif num < val1 and len(self.maxheap) > len(self.minheap):
            val2 = -self.heappeak(self.maxheap)
            if val2 < num:
                heappush(self.minheap, num)
            else:
                maxim = heappop(self.maxheap)
                heappush(self.minheap, -maxim)
                heappush(self.maxheap, -num)
        else:
            heappush(self.maxheap, - num)
                
    def findMedian(self) -> float:
        sizemax = len(self.maxheap)
        sizemin = len(self.minheap)
        
        if sizemax == sizemin:
            minim = self.heappeak(self.minheap)
            maxim = self.heappeak(self.maxheap)
            
            return (minim + (-maxim)) / 2
        
        elif len(self.minheap) > len(self.maxheap):
            
            minim = self.heappeak(self.minheap)
            return minim 
        else:
            maxim = self.heappeak(self.maxheap)
            return -maxim     
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()