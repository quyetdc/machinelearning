f = open('hello_world.txt', 'w+')
f.write('Hi every body!')
f.close()

f_cont = open('hello_world.txt').read()
print(f_cont)
