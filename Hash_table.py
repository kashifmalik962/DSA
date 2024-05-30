class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.max
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        print(self.arr)


ob = Hashtable()
print(ob.get_hash('march 6'))
print(ob.get_hash('march 17'))
# ob.add('march 6',310)
# ob.delete('march 6')
