# 3 masala


def merge_unique_ids(active_users: list, new_users: list) -> list:
    result = []

    for user in active_users + new_users:
        if user not in result:
            result.append(user)

    return result


active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001']

new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']

print(merge_unique_ids(active_users, new_users))
