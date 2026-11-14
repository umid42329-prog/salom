# 4 masala


def sorted_by_price(products: list) -> list:
    return sorted(products, key=lambda product: int(product[1]), reverse=True)


products = []

n = int(input("Nechta mahsulot kiritasiz? "))

for i in range(n):
    print(f"{i + 1}-mahsulot:")
    name = input("Mahsulot nomi: ")
    price = input("Mahsulot narxi: ")
    count = input("Mahsulot soni: ")

    products.append((name, price, count))

result = sorted_by_price(products)

print("\nNarx bo'yicha kamayish tartibida:")
for product in result:
    print(product)


