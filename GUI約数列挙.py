# -*- coding: utf-8 -*-

#GUIを書いてみる





def divisor(n): #n以下の約数列挙
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table

n = int(input())
for i in divisor(n):
    print(i)

