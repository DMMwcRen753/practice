num = 0

for xp in range(1,513):
    for y in range(1,513):
        if (xp/y) < 0:
            break
        else:
            num += xp % y
print(num)