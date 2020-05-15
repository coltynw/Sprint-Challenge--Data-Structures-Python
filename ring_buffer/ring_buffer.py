class RingBuffer:
    def __init__(self, capacity):
        #where it the iterating position is
        self.current = 0 
        #the array
        self.store = [] 
        #the max number of things in the array
        self.capacity = capacity 

    def append(self, item):
        #check if the length of the array is smaller than the capacity
        if len(self.store) < self.capacity:
        #if it is then add on next item
            self.store.append(item)
        #if it isn't then
        else:
            #get the oldest item
            self.store[self.current] = item 
        #add 1
        self.current += 1 
        #if the position is at capacity
        if self.current == self.capacity: 
            #then go back to the first one, zero index.
            self.current = 0

    def get(self): 
        return self.store