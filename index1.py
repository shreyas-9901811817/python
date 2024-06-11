

a=["apple","banana"]
b=["tea","buiscuits"]
a.extend(b)
print(a)


for i in range(5):
    for j in range(i):
        print(" ", end="")

    for k in range(5 - i, 0, -1):
        print(k, end=" ")

    print()


n = 5  # size of the cross

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()