products = {}
howMuch = int(input('How Much Products Do You Want To Add: '))
i = 0
while i < howMuch:
    productKey = input('Product Name: ')
    productValue = input('Product Price: ')
    products.update({
        productKey : productValue
    })
    howMuch-=1
for Keys,Values in products.items():
    print('Product: {} and Price: {}'.format(Keys,Values))