class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.start = None

    def insert_at_end(self,value):
        newnode = node(value)
        if self.start==None:
            self.start = newnode

        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next = newnode

    def print(self):
        temp2 = self.start

        llstr = ''
        while temp2:
            if temp2.next!=None:
                llstr+=str(temp2.data) + '-->'
                temp2 = temp2.next
            
            else:
                llstr+=str(temp2.data)
                temp2 = temp2.next
                
        print(llstr)

    def get_length(self):
        temp3 = self.start
        count = 0
        if temp3!=None:
            while temp3:
                count+=1
                temp3 = temp3.next
            print(count)

    def delete_fnode(self):
        if self.start==None:
            print('Linklist is empty')
        else:
            self.start = self.start.next
            print(self.start)

    def delete_lnode(self):
        temp5 = self.start
        llstr = ''
        while temp5!=None:
            if temp5.next!=None:
                llstr+=str(temp5.data) + '-->'
                
            temp5 = temp5.next
            

        print(llstr)

    

obj = linkedlist()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.insert_at_end(50)
obj.delete_lnode()
obj.print()
obj.get_length()


