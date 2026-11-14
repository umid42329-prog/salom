# 3 masala


def merge_unique_ids(active_users: list, new_users: list) -> list:
    result = []

    for user in active_users + new_users:
        if user not in result:
            result.append(user)

    return result


active_users = input("Faol foydalanuvchilar IDlarini kiriting: ").split()

new_users = input("Yangi foydalanuvchilar IDlarini kiriting: ").split()

print("Noyob IDlar:")
print(merge_unique_ids(active_users, new_users))
