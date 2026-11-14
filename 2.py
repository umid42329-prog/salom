# 2 masala


def search_by_genre(cinema: list, genre: str) -> list:
    result = []

    for film in cinema:
        if film["genre"].lower() == genre.lower():
            result.append(film)

    return result


cinema = []

n = int(input("Nechta film kiritasiz? "))

for i in range(n):
    print(f"\n{i + 1}-film:")

    title = input("Film nomi: ")
    film_genre = input("Film janri: ")
    price = int(input("Film narxi: "))

    cinema.append({
        "title": title,
        "genre": film_genre,
        "price": price
    })

genre = input("\nQaysi janrdagi filmlarni qidirasiz? ")

print("\nNatija:")
print(search_by_genre(cinema, genre))
