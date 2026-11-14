# 5 masala


def are_numbers_ascending(text: str) -> bool:
    numbers = []

    for word in text.split():
        word = word.strip(",.!?:;")
        if word.isdigit():
            numbers.append(int(word))

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False

    return True


text = input("Matn kiriting: ")

print(are_numbers_ascending(text))
