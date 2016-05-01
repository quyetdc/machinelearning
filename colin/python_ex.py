# tinh tong 1-> 10000

sum = 0

for i in range(1, 1001):
    sum += i

print(sum)

# Tinh tong so chan 1-> 1000

even_sum = 0
for i in range(1,1001):
    if (i % 2) == 0:
        even_sum += i

print(even_sum)

# string & list

name = 'I am Quyet!'

name_list = name.split( )

name_list.append('Hello Python')

print(name_list)

new_name = ' '.join(name_list)

print(new_name)


# Function declaration

def sumToNumber(number):
    sum = 0
    for i in range(1,number+1):
        sum += i
    return sum

print(sumToNumber(10))


#################
# IMPORT MODULE #
#################

import sum_module

print(sum_module.sumFunction(10, 31))


