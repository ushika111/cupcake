class Property:
    """
    this is the Parent property
    """

    def __init__(self, type,location):
       self.set_type(type)
       self.set_location(location)
    def set_type(self,type):
        """
        This is to define the type of property, which should only be LAND, APARTMENT, or HOUSE.
        :param type: string
        :return: none
        """
        if type not in ["apartment","house","land"]:
            self.__type = ("undefined property")
        else:
            self.__type = type
    def set_location(self, location):
        """
        This is to define a location of the property which should be only Australia
        :param location: string
        :return: none
        """
        if location not in ("Australia"):
            self.__location = ("outside the territory ")
        else:
            self.__location = location
    def get_type(self):
        return(self.__type)
    def get_location(self):
        return(self.__location)
    def __str__(self):
        print("The property is:",{self.__type},"and it is proven its located in :",{self.__location})

        p1 = property("apartment","Australia")
        p2 = property("house","USA")
        properties = list(p1,p2)
        for item in properties:
            properties.append(property)

        print(properties)
