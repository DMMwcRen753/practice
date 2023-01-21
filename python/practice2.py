#7以上7777777以下の7の倍数を全て書き出したとき、数字「7」は何回現れるか。
count = 0

for num in range(7,7777778,7):
    count += str(num).count('7')

print(count)
