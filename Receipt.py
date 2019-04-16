import datetime


class Receipt:
    def __init__(self, purchases):
        self.__purchases = purchases

    def __str__(self):
        subTotal = 0
        totalTax = 0
        finalTotal = 0
        for x in range(len(self.__purchases)):
            name = self.__purchases[x].getName()
            price = self.__purchases[x].getPrice()
            tax = self.__purchases[x].getTax(self.__purchases[x].getTaxRate())
            if price != tax:
                totalTax += tax
            subTotal += price
            formattedPrice = '{:.2f}'.format(price)
            newString = '{:_<25}'.format(name)
            finalString = newString + formattedPrice
            self.__purchases[x] = finalString
        finalTotal = subTotal + totalTax
        return '----- Receipt ' + str(datetime.datetime.now()) + ' -----' + '\n' + '\n'.join(self.__purchases) + '\n' + \
               '\n' + '{:_<25}'.format('Sub Total') + '{:.2f}'.format(subTotal) + '\n' + \
               '{:_<25}'.format('Tax') + '{:.2f}'.format(totalTax) + '\n' + \
               '{:_<25}'.format('Total') + '{:.2f}'.format(finalTotal)

    def addItem(self, newItem):
        return self.__purchases.append(newItem)

