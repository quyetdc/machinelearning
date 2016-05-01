import math

# Nhan vo huong 2 vector

print("Chuong trinh nha 2 vector vo huong 3 - 3")
print("Vector x: ")
x1 = int(input("     x1: "))
x2 = int(input("     x2: "))
x3 = int(input("     x3: "))

print("Vector y: ")
y1 = int(input("     y1: "))
y2 = int(input("     y2: "))
y3 = int(input("     y3: "))

print(' \n-----\n')

tichVoHuong = x1*y1 + x2*y2 + x3*y3

print('|' + str(x1) + '' + '      |' + str(y1) )

print('|' + str(x2) + '' + '  x'
      + '   |' + str(y2) + '' + '   =   ' +
      '' + str(tichVoHuong)+'')


print('|' + str(x3) + '' + '      |' + str(y3))


print(' \n-----\n')

abs_x = math.sqrt(x1**2 + x2**2 + x3**2)
abs_y = math.sqrt(y1**2 + y2**2 + y3**2)

print('||x|| = ' + str(abs_x))
print('||y|| = ' + str(abs_y))
print('cos(x, y) = ' + str(tichVoHuong / (abs_x * abs_y)))

