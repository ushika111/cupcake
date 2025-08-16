class House:
    def __init__(self,num,color,availability):
        self.set_num (num)
        self.set_color (color)
        self.set_availability (availability)
    def set_num(self, num):
        if num>= 1 and num<= 10:
            self.__num = num
        elif num<1:
            self.__num = 1
        elif num>10:
            self.__num=10

    def set_color(self,color):
        if color not in ["pink","amber","olive"]:
            self.__color = ("blue")
        else:
            self.__color = color

    def set_availability(self,availability):
        if isinstance(availability, bool):
            self.__availability = availability
        else:
            self.__availability = False

    def get_num(self):
        return self.__num
    def get_color(self):
        return self.__color
    def get_availability(self):
        return self.__availability
    def paint(self, new_color):
        if self.get_color(new_color):
            print("You have chosen the same color, you must like it")
        else:
            if new_color in self.__color:
                print("A new color I see")
                self.set_color(new_color)
            else:
                print("The color you've chosen is not in the options")
    def extend(self):
        if self.get_num() <10:
            self.__num += 1
        else:
            print("that is the maximum number of rooms you could extend to")
    def redesign(self,new_num):
        self.new_num(new_num)
    def sell_house(self):
        if self.get_availability():
            print("The house is available")
        else:
            if self.get_availability() == True:
                print("Congrats the house is now made available")
    def __str__(self):
        print()


myHouse = House(2,"pink","True")
print(myHouse.get_num())
print(myHouse.get_color())
print(myHouse.get_availability())
print(myHouse.paint())
print(myHouse.extend())
print(myHouse.redesign())
print(myHouse.sell_house())