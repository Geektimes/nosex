n = 116111
storage = n % 10
while n > 0:
    digit = n % 10
    if digit != storage:
        print("NO")
    else:
        print("YES")
    n = n // 10

print(1161 // 10)