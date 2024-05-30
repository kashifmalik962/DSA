class Hashtable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def hash_val(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.Max
    
    def __getitem__(self,key):
        k = self.hash_val(key)
        for kv in self.arr[k]:
            if kv[0] == key:
                return kv[1]
    
    
    def __setitem__(self,key,val):
        h = self.hash_val(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))


    def __delitem__(self,key):
        h = self.hash_val(key)
        for idx,kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h][idx]
                return self.arr 
    
    def print(self):
        print(self.arr)
    
ob = Hashtable()
# ob.hash_val('march 6')
# ob.delete('march 6')
ob['march 6'] = 120
ob['march 6'] = 10
ob['march 8'] = 67
ob['march 9'] = 4
ob['march 17'] = 459
print(ob.arr)
del ob['march 17']
print(ob.arr)
