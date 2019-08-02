for i in range(1, 101):
    g = i % 10
    s = i // 10
    if i % 7 != 0 and g != 7 and s != 7:
        print(i)

