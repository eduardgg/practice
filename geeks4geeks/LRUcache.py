
class BLLNode(object):
    
    def __init__(self, key=None, val=None, pre=None, nex=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nex = nex

class LRUcache():

    def __init__(self, cap):
        self.cap = cap # Nombre d'elements màxim
        self.dic = {} # Valors key -> BLL(value, pre, nex)
        self.head = None # Valor key
        self.last = None # Valor key
        self.len = 0 # Nombre d'elements
    
    def GET(self, key):
        if key not in self.dic.keys():
            return -1
        return self.dic[key].val
    
    def SET(self, key, value):
        
        print()
        print("DEBUG BEFORE")
        print("last key:", self.last)
        print("dic", self.dic)
        if self.last:
            print("last value:", self.dic[self.last].val)
        print("prev head:", self.head)
        if self.head:
            print("dic[head]: ", self.dic[self.head].val)
        print("len and cap:", self.len, self.cap)
        print()

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
            # TODO:
            # Segur que s'està esborrant l'últim bé?
            # A C++ es pot eliminar explícitament un objecte
            # A python cal eliminar totes les referències
            # Segur que ho estic eliminant tot???
            newLast = self.dic[self.last].pre
            newLast.nex = None
            del self.dic[self.last]
            self.last = newLast.key
            self.dic[key] = BLLNode(key, value)
            self.dic[key].nex = self.dic[self.head]
            self.dic[self.head].pre = self.dic[key]
            self.head = key

        print("DEBUG AFTER")
        print("last key:", self.last)
        print("dic", self.dic)
        print("new head: ", self.head)
        print("dic[head]: ", self.dic[self.head].val)
        print("len and cap:", self.len, self.cap)
        print()


        

t = int(input())
for _ in range(t):
    capacity = int(input())
    cache = LRUcache(capacity)
    queries = int(input())
    for _ in range(queries):
        q = input()
        if q == "SET":
            key = int(input())
            value = int(input())
            cache.SET(key, value)
        elif q == "GET":
            key = int(input())
            print(cache.GET(key))