class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        self.head = Node(data,self.head)

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr+=str(itr.data)+suffix
            itr = itr.next
        print(llstr)  

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr =  itr.next
        return count
    

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
                
        itr.next = Node(data)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count+=1

ob = Linkedlist()
ob.insert_at_beginning(5)
ob.insert_at_beginning(10)
ob.insert_at_beginning(15)
ob.insert_at_beginning(20)
ob.insert_at_end(567)
ob.insert_at(5,756)
print(ob.get_length())
ob.print()