import math

# 扇形の面積
def area_sector(r, theta):
    return r**2 * theta / 2


# 半径r
r = 10
# 角度theta
theta = math.pi / 3
# 面積S
S = area_sector(r, theta)

# 0 < x < rの点を通る直線で切る
for x in range(1, r):
    phi = math.asin(x * math.sin(theta) / r)
    area_1 = (r**2 * (theta - phi) - (r * math.cos(phi) - x * math.cos(theta)) * x * math.sin(theta)) / 2
    area_2 = S - area_1
    dif = abs(area_1 - area_2)
    print('x =', x)
    # print('area 1 = ', area_1)
    # print('area 2 = ', area_2)
    print('dif = ', dif)
    