class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_at_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def insert_at_first(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node



    def print_f(self):
        temp = self.head
        if self.head is None:
            print('List is empty')
        else:
            llstr = ''
            while temp:
                if temp.next is not None:
                    llstr+=str(temp.data)+'-->'
                    temp = temp.next
                else:
                    llstr+=str(temp.data)
                    temp = temp.next
            print(llstr)
    

    def print_b(self):
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
                
    def check_palindrome(self):
        a_list = []
        b_list = []
        temp3 = self.head
        temp4 = self.tail

        if temp3 is None:
            print('List is empty')
        else:
            while temp3:
                a_list.append(temp3.data)
                temp3 = temp3.next
        if temp4 is None:
            print('List is empty')
        else:
            while temp4:
                b_list.append(temp4.data)
                temp4 = temp4.prev
        if a_list == b_list:
            print(True)
        else:
            print(False)

    
    def get_len(self):
        temp5 = self.head
        count = 0
        while temp5 is not None:
            count+=1
            temp5 = temp5.next
        print(count)


    def find_middle_node(self):
        temp5 = self.head
        count = 0
        while temp5 is not None:
            count+=1
            temp5 = temp5.next

        Mdl_Nde_Ind = (count//2)+1
        temp5 = self.head
        count2 = 1
        while temp5:
            if count2 == Mdl_Nde_Ind:
                print(temp5.data)
            temp5 = temp5.next
            count2+=1

    

    def split_into_halves(self):
        temp5 = self.head
        count = 0
        a_list = []
        b_list = []
        while temp5 is not None:
            count+=1
            temp5 = temp5.next

        Mdl_Nde_Ind = (count//2)
        temp5 = self.head
        count2 = 1
        while temp5:
            if count2 <= Mdl_Nde_Ind:
                a_list.append(temp5.data)
                temp5 = temp5.next
                count2+=1
            elif count2 >= Mdl_Nde_Ind:
                b_list.append(temp5.data)
                temp5 = temp5.next
                count2+=1
        print(a_list)
        print(b_list)

    
    def remove_all_dup(self):
        temp6 = self.head
        a_list = []
        while temp6:
            if temp6.data in a_list:
                temp6 = temp6.next
            else:
                a_list.append(temp6.data)
                temp6 = temp6.next
        print(a_list)

    
    def kth_node_at_end(self,value):
        temp7 = self.tail
        val = value
        count = 1
        while temp7 is not None:
            if val >= count: 
                count+=1
                print(temp7.data)
                temp7 = temp7.prev
            else:
                break

    def insert_node_specific_posi(self,position,node):
        temp7 = self.head
        count = 1
        
        llstr = ''
        while temp7:
            if temp7.next is not None:
                if count == position:
                    count+=1
                    llstr+=str(node)+'-->'
                llstr+=str(temp7.data)+'-->'
                temp7 = temp7.next
                count+=1

            else:
                llstr+=str(temp7.data)
                temp7 = temp7.next
                count+=1
        
        print(llstr)

    
    def delete_node_at_speci_posi(self,position):
        temp7 = self.head
        count = 1
        
        llstr = ''
        while temp7:
            if temp7.next is not None:
                if count == position:
                    count+=1
                    # llstr+=str(node)+'-->'
                    temp7 = temp7.next
                llstr+=str(temp7.data)+'-->'
                temp7 = temp7.next
                count+=1

            else:
                llstr+=str(temp7.data)
                temp7 = temp7.next
                count+=1
        
        print(llstr)
        
ob = Doublelinkedlist()
ob.insert_at_end(10)
ob.insert_at_end(20)
ob.insert_at_end(30)


# ob.insert_at_first(40)
# ob.insert_at_first(50)
# ob.insert_at_first(60)
# ob.print_b()
# ob.check_palindrome()
# ob.get_len()
# ob.find_middle_node()
# ob.split_into_halves()
# ob.remove_all_dup()
# ob.kth_node_at_end(3)
# ob.delete_node_at_speci_posi(3)
ob.print_f()
