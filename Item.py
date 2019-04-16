class Item:

    def __init__(self, name, price, taxable, taxRate = 0):
        self.__name = name
        self.__price = float(price)
        self.__taxable = taxable
        self.__taxRate = taxRate

    def __str__(self):
        return self.__name

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getTax(self, tax):
        if (self.__taxable == True) and (tax != 0):
            return float(self.__price) * tax
        else:
            return self.__price

    def getTaxRate(self):
        return self.__taxRate
