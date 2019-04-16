from Item import Item
from Receipt import Receipt

counter = 0
print('Welcome to Receipt Creator')
Receipt = Receipt([])
while counter == 0:
    name = input('Enter Item name: ')
    price = input("Enter Item Price: ")
    priceAsFloat = float(price)
    taxable = input('Is the item taxable (yes/no): ')
    if taxable == 'yes':
        tax = True
        taxRate = float(input('Enter the tax rate as a decimal: '))
        newItem = Item(name, price, tax, taxRate)
    else:
        tax = False
        newItem = Item(name, price, tax)
    nextIteration = input('Add another item (yes/no): ')
    if nextIteration == 'no':
        counter += 1
    Receipt.addItem(newItem)
print(Receipt)
