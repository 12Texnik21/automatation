def mount_to_season(mount):
    if mount in (12, 1, 2):
        return "Зима"
    elif mount in (3, 4, 5):
        return "Весна"
    elif mount in (6, 7, 8):
        return "Лето"
    elif mount in (9, 10, 11):
        return "Осень"
    else:
        return "Неверный номер месяца"
    

print(mount_to_season(1))
print(mount_to_season(5))
print(mount_to_season(6))
print(mount_to_season(10))
print(mount_to_season(15))