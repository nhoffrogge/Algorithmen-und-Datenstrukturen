import sys

n = 10

data = []

for i in range(n):
    
    a = len(data)
    
    b = sys.getsizeof(data)
    
    print('Laenge: ', a, 'Groesse in Bytes: ', b)
    
    data.append(i)
    
class M(object):
    
    def public(self):
        print('Use Tab to see me!')
        
    def _private(self):
        print('You wont be able to Tab to see me!')
        
m = M()
m.public()

m._private()

import ctypes

class DynamicArray():
    
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        #len(object)
        return self.n
    
    def __getitem__(self,k):
        # arr[6]
        
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        
        return