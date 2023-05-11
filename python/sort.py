from random import randint
a= [randint(1,100) for i in range(5)]
print(a)
n = len(a)
for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
print("Sorted")
for i in range(n):
    print(a[i], end=" . ")




