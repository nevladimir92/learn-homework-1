phone1 = {'name': 'iPhone Xs Plus','stock':24,'price':65432.1,'discount':25}
phone2 = {'name': 'Samsung Galaxy S10','stock':8,'price':50000,'discount':10}
phone3 = {'name': '','stock':10,'price':10000,'discount':22}

def discounted(price,discount,max_discount =20,name = ""):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discaunt = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        return price
    else:
        return price - (price*discount /100)


apple_desc = discounted(phone1['price'],phone1['discount'],name = phone1['name'])
print(apple_desc)

android_desc = discounted(phone2['price'],phone2['discount'],name = phone2['name'])
print(android_desc)

a_desc = discounted(phone3['price'],phone3['discount'],name = phone3['name'])
print(a_desc)