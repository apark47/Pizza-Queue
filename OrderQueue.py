# OrderQueue.py
from Pizza import Pizza

class QueueEmptyException(Exception):
    pass

class OrderQueue:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i): 
        while i // 2 > 0: # parent does exist
            if self.heapList[i].getTime() < self.heapList[i // 2].getTime():
                # swap
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp

            i = i // 2
    
    
    def percDown(self, i):
        # we know we have at least a left child to check
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i) # mc is minimal child (lowest value)
            if self.heapList[i].getTime() > self.heapList[mc].getTime():
                # swap
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
            
    def minChild(self, i):
        if (i * 2 + 1) > self.currentSize: # if right child doesn't exist
            return i * 2
        else:
            if self.heapList[i*2].getTime() < self.heapList[i*2+1].getTime():
                return i*2
            else:
                return i*2+1
            
    

    def addOrder(self, pizzaOrder):
        self.heapList.append(pizzaOrder) # append works left to right in a complete tree structure
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def processNextOrder(self):
        if self.currentSize == 0:
            raise QueueEmptyException

        
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval.getOrderDescription()

       
    
