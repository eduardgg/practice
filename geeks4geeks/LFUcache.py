
# Inefficient implementation of SortedList:

'''
import bisect

class SortedList:
    
    def __init__(self):
        self.data = []

    def add(self, item):
        bisect.insort_left(self.data, item)

    def discard(self, item):
        index = bisect.bisect_left(self.data, item)
        if index < len(self.data) and self.data[index] == item:
            self.data.pop(index)

    def pop(self, index=0):
        return self.data.pop(index)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)
'''



from sortedcontainers import SortedList
class LFUCache:

    def __init__(self, cap: int):
        self.cap = cap
        self.dic = {}
        self.freqs = {}
        self.order = {}
        self.els = SortedList()
        self.cnt = 0

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.els.discard((self.freqs[key], self.order[key], key))
        self.freqs[key] += 1
        self.cnt += 1
        self.order[key] = self.cnt
        self.els.add((self.freqs[key], self.order[key], key))
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.dic:
            self.els.discard((self.freqs[key], self.order[key], key))
            self.freqs[key] += 1
        else:
            if len(self.dic) >= self.cap:
                freq, _, old_key = self.els.pop(0)
                del self.dic[old_key]
                del self.freqs[old_key]
                del self.order[old_key]
            self.freqs[key] = 1
        self.cnt += 1
        self.order[key] = self.cnt
        self.dic[key] = value
        self.els.add((self.freqs[key], self.order[key], key))




obj = LFUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))
obj.put(5, 5)
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))