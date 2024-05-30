                                    # HOTEL MANAGEMENT PROGRAMM
class person:
    def __init__(self,name,hotel,rm_card):
        self.name = name
        self.hotel = hotel
        self.rm_card = rm_card
        
        self.food = ['breakfast','lunch','dinner']
        self.food = [i.capitalize() for i in self.food]
        
        self.food_b = ['tea','coffee','green tea','bread','egg','sandwich','butter','juice','fruits','dry-fruits']
        self.food_b = [i.capitalize() for i in self.food_b]
        
        self.food_l = ['rice','chappati','biryani','veg-biryani','chicken-burger','cold-drinks','sweet','etc']
        self.food_l = [i.capitalize() for i in self.food_l]
        
        self.food_d = ['shahi Paneer','dal-makhni','rice','chappati','cold-drinks','sweet']
        self.food_d = [i.capitalize() for i in self.food_d]

    def greet(self):
        print('Welcome Mr. {0} enjoy with your family in my hotel {1}'.format(self.name,self.hotel))

    def rm_card(self):
        print(f'Hello Sir your room card is {self.rm_card} Thankyou need you more information')

    def hungry(self):
        inp = input('you are hungy you want to food y/n :')
        if inp == 'y':
            inp2 = input(f'select a category you need {(1,self.food[0]),(2,self.food[1]),(3,self.food[2])} : ')
            
            if inp2 == '1':
                count = 1
                for i in self.food_b:
                    print(count,' = ',i)
                    count+=1

                clint_food_need = []
                while True:
                    inp_food_b = input('What you need :')
                    
                    if inp_food_b == "" or int(inp_food_b) < 0 or int(inp_food_b) > 10:
                        break
                    
                    elif int(inp_food_b) > 0 and int(inp_food_b) <=10:
                        clint_food_need.append(inp_food_b)
                    else:
                        break

                def order(food_list):
                    print('Order List')
                    c = 0
                    for i in food_list:
                        c+=1
                        print(c,'.',self.food_b[int(i)-1])
                    print('Order is Successfully please wait a 10 min ')

                order(clint_food_need)

            elif inp2 == '2':
                count = 1
                for i in self.food_l:
                    print(count,' = ',i)
                    count+=1

                clint_food_need = []
                while True:
                    inp_food_l = input('What you need :')
                    
                    if inp_food_l == "" or int(inp_food_l) < 0 or int(inp_food_l) > 10:
                        break
                    
                    elif int(inp_food_l) > 0 and int(inp_food_l) <=8:
                        clint_food_need.append(inp_food_l)
                    else:
                        break

                def order(food_list):
                    print('Order List')
                    c = 0
                    for i in food_list:
                        c+=1
                        print(c,'.',self.food_l[int(i)-1])
                    print('Order is Successfully please wait a 10 min ')

                order(clint_food_need)
            
            elif inp2 == '3':
                count = 1
                for i in self.food_d:
                    print(count,' = ',i)
                    count+=1

                clint_food_need = []
                while True:
                    inp_food_d = input('What you need :')
                    
                    if inp_food_d == "" or int(inp_food_d) < 0 or int(inp_food_d) > 10:
                        break
                    
                    elif int(inp_food_d) > 0 and int(inp_food_d) <=6:
                        clint_food_need.append(inp_food_d)
                    else:
                        break

                def order(food_list):
                    print('Order List')
                    c = 0
                    for i in food_list:
                        c+=1
                        print(c,'.',self.food_d[int(i)-1])
                    print('Order is Successfully please wait a 10 min ')

                order(clint_food_need)
            
            else:
                print('Soory! there is no food variery here')
        else:
            print('If you are hungry to inform our staff')

person = person('Kashif','Abu tabu',123)
person.greet()
person.hungry()

