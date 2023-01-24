count = 0
t = 0

for i in range(1,1000,4):
    t += 8/(i*(i+2))
    count += 1
    if t > 3.1414:
        break
print(t)
print(count)
