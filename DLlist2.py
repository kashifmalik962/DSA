class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            
            temp.next = new_node
        
    def print(self):
        temp2 = self.head

        llstr = ''
        while temp2:
            if temp2 is not None:
                if temp2.next is not None:
                    llstr+=str(temp2.data)+'-->'
                    temp2 = temp2.next
                else:
                    llstr+=str(temp2.data)
                    temp2 = temp2.next

            else:
                print(False)
                temp2 = temp2.next
        print(llstr)


    def insert_at_first(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        

    def get_length(self):
        temp3 = self.head
        count = 0
        while temp3 is not None:
            count+=1
            temp3 = temp3.next
        print(count)

    
class Doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end_d(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            print(self.tail.data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def delete_at_first(self):
        if self.head==None:
            print('Linklist is empty')
        else:
            self.head = self.head.next


    
    def delete_at_end(self):
        if self.head==None:
            print('Linklist is empty')
        else:
            previous_node = self.tail.prev
            previous_node.next = None
            self.tail = previous_node
    
    
    def print_forword(self):
        temp2 = self.head

        llstr = ''
        while temp2:
            if temp2 is not None:
                if temp2.next is not None:
                    llstr+=str(temp2.data)+'-->'
                    temp2 = temp2.next
                else:
                    llstr+=str(temp2.data)
                    temp2 = temp2.next

            else:
                print(False)
                temp2 = temp2.next
        print(llstr)

    
    def print_backword(self):
        temp5 = self.tail

        llstr2 = ''
        while temp5 is not None:
            if temp5.prev is not None:
                llstr2+=str(temp5.data)+'<--'
                temp5 = temp5.prev
            else:
                llstr2+=str(temp5.data)
                temp5 = temp5.prev
        print(llstr2)


# obj = Linkedlist()
# obj.insert_at_end(10)
# obj.insert_at_end(20)
# obj.insert_at_end(30)
# obj.insert_at_end(40)
# obj.insert_at_first(5)
# obj.get_length()
# obj.print()


ob = Doublelinkedlist()
ob.insert_at_end_d(10)
ob.insert_at_end_d(20)
ob.insert_at_end_d(30)
ob.delete_at_end()
ob.print_forword()
# ob.print_backword()