class Hashtable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.Max
        
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx,kv in enumerate(self.arr[h]):
            if kv[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def find_avg_temrpture_of_given_day(self,days):
        list = []
        if days <= len(self.arr):
            for i in range(days):
                for idx,element in enumerate(self.arr):
                    if len(element) == 1 and element[0][0] == f"Jan-{i}":
                        list.append(ob[f"Jan-{i}"][0][1])
                        
                    else:
                        for j in range(len(element)):
                            if len(element) > 1 and element[0][0] == f"Jan-{i}":
                                v = (element[j][1])
                                list.append(v)
        else:
            print('extra length')
        print(sum(list)/len(list))

    def find_max_temrpture_of_given_day(self):
        list = []
        for i in range(10):
            for idx,element in enumerate(self.arr):
                        if len(element) == 1 and element[0][0] == f"Jan-{i}":
                            list.append(ob[f"Jan-{i}"][0][1])
                        
                        else:
                            for j in range(len(element)):
                                if len(element) > 1 and element[0][0] == f"Jan-{i}":
                                    v = (element[j][1])
                                    list.append(v)
        print(max(list))
                

ob = Hashtable()
# print(ob.get_hash('Jan-06'))
ob['Jan-1'] = 27
ob['Jan-2'] = 31
ob['Jan-3'] = 23
ob['Jan-4'] = 34
ob['Jan-5'] = 37
ob['Jan-6'] = 38
ob['Jan-7'] = 29
ob['Jan-8'] = 30
ob['Jan-9'] = 35
ob['Jan-10'] = 30
# ob.find_avg_temrpture_of_given_day(10)
# print(ob.arr)
ob.find_max_temrpture_of_given_day()