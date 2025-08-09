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

myHouse = House(2,"pink","True")
print(myHouse.get_num())
print(myHouse.get_color())
print(myHouse.get_availability())
