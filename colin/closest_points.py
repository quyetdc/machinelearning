import math

######################################################################
# Bai toan tim 2 điểm gần nhất trong 3 điểm -> có khả năng cùng nhóm #
######################################################################

# Nhan vo huong 2 vector

print("Tìm hai điểm có khoảng cách gần nhau nhất giữa 3 điểm")

print("Vector x: ")
x1 = int(input("     x1: "))
x2 = int(input("     x2: "))

print("Vector y: ")
y1 = int(input("     y1: "))
y2 = int(input("     y2: "))

print("Vector z: ")
z1 = int(input("     z1: "))
z2 = int(input("     z2: "))

print(' \n-----\n')

# k/c x-y
xy = math.sqrt((y1-x1)**2 + (y2-x2)**2)

# k/c x-z
xz = math.sqrt((z1-x1)**2 + (z2-x2)**2)

# k/c y-z
yz = math.sqrt((z1-y1)**2 + (z2-y2)**2)

minDis = xy

for i in [yz, xz]:
    if i < minDis:
        minDis = i

if minDis == xy:
    print('2 điểm gần nhau nhất là: x và y')
elif minDis == yz:
    print('2 điểm gần nhau nhất là: y và z')
else:
    print('2 điểm gần nhau nhất là: x và z')