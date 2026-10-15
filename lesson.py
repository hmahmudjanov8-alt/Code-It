count = 0

while True:
    product = input("Введите товар (стоп — закончить): ")

    if product == "стоп":
        break

    price = float(input("Введите цену: "))
    count = count + 1

    if count == 1:
        min_price = price
        max_price = price
        min_product = product
        max_product = product
    else:
        if price < min_price:
            min_price = price
            min_product = product

        if price > max_price:
            max_price = price
            max_product = product

if count > 0:
    print("Минимальная цена:", min_price, "Товар:", min_product)
    print("Максимальная цена:", max_price, "Товар:", max_product)
else:
    print("Товары не добавлены")
