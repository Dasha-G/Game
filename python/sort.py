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



stone1 = GameSprite("pictures/stone", 186, 272, -10, -10)
stone2 = GameSprite("pictures/sstone", 238, 238, 10, 100)
stone3 = GameSprite("pictures/ssstone", 172, 248, 30, 210)
stone4 = GameSprite("pictures/stone", 196, 250, 170, -30)
stone5 = GameSprite("pictures/sstone", 172, 272, 210, 150)
stone6 = GameSprite("pictures/ssstone", 190, 254, 500, 400)
stone7 = GameSprite("pictures/stone", 168, 238, 600, 450)
stone8 = GameSprite("pictures/sstone", 176, 246, 430, 520)
stone9 = GameSprite("pictures/ssstone", 166, 274, 510, 570)
stone10 = GameSprite("pictures/stone", 180, 270, 600, 620)
stone11 = GameSprite("pictures/sstone", 186, 272, 620, 360)
stone12 = GameSprite("pictures/ssstone", 238, 238, 350, 650)
stone13 = GameSprite("pictures/stone", 172, 248, 750, 350)
stone14 = GameSprite("pictures/sstone", 196, 250, 700, -50)
stone15 = GameSprite("pictures/ssstone", 172, 272, 650, 0)
stone16 = GameSprite("pictures/stone", 190, 254, 750, 50)
stone17 = GameSprite("pictures/sstone", 168, 238, 1350, -100)
stone18 = GameSprite("pictures/ssstone", 176, 246, 1250, -80)
stone19 = GameSprite("pictures/stone", 166, 274, 1320, 50)
stone20 = GameSprite("pictures/sstone", 180, 270, 1350, 230)
stone21 = GameSprite("pictures/ssstone", 186, 272, 850, -80)
