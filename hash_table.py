


class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [None]*self.max
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            c = ord(char)
            hash += c
        return hash % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

h = Hashtable()
h["march 6"] = 302
print(h["march 6"])
print(h.arr)