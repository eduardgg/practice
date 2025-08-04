# User function Template for python3

# design the class in the most optimal way

class BLLNode(object):
    
    def __init__(self, key=None, val=None, pre=None, nex=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nex = nex
        
class LRUCache:
      
    # Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        self.cap = cap # Nombre d'elements màxim
        self.dic = {} # Valors key -> BLL(value, pre, nex)
        self.head = None # Valor key
        self.last = None # Valor key
        self.len = 0 # Nombre d'elements
        
        
    # Function to return value corresponding to the key.
    def get(self, key):
        if key not in self.dic.keys():
            return -1
        return self.dic[key].val
        
        
    # Function for storing key-value pair.   
    def set(self, key, value):
        
        if self.cap == 1:
            self.dic = {key: BLLNode(key, value)}
            self.head = key
            self.last = key
            self.len = 1
            
        if key in self.dic.keys():
            if self.dic[key].nex and self.dic[key].pre:
                self.dic[key].nex.pre = self.dic[key].pre
                self.dic[key].pre.nex = self.dic[key].nex
                self.dic[key].nex = self.dic[self.head]
                self.dic[self.head].pre = self.dic[key]
            elif self.dic[key].pre:
                newLast = self.dic[key].pre
                newLast.nex = None
                self.last = newLast.key
                self.dic[key].pre = None
                self.dic[key].nex = self.dic[self.head]
                self.dic[self.head].pre = self.dic[key]
            self.head = key
            self.dic[key].val = value

        elif self.head == None:
            self.dic[key] = BLLNode(key, value)
            self.head = key
            self.last = key
            self.len += 1

        elif self.len < self.cap:
            self.dic[key] = BLLNode(key, value)
            self.dic[key].nex = self.dic[self.head]
            self.dic[self.head].pre = self.dic[key]
            self.head = key
            self.len += 1
        
        else:
            newLast = self.dic[self.last].pre
            newLast.nex = None
            del self.dic[self.last]
            self.last = newLast.key
            self.dic[key] = BLLNode(key, value)
            self.dic[key].nex = self.dic[self.head]
            self.dic[self.head].pre = self.dic[key]
            self.head = key



# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  # number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru = LRUCache(cap)
        
       
        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]
            if qtyp == 'SET':
                lru.set(int(a[i+1]), int(a[i+2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i+1])), end=' ')
                i += 2
            q += 1
        print()

# Driver Code Ends