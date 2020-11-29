import ctypes as C
math = C.CDLL('./libmydyn.so')

# Casteo correcto de los inputs
math.add_int.argtypes = [C.c_int, C.c_int]
math.add_float.argtypes = [C.c_float, C.c_float]

# Casteo correcto de los outputs
math.add_int.restype = C.c_int
math.add_float.restype = C.c_float


print('Archivo: add_two.o')
print('')
print(' - add_int(int: a, int: b)')

a = int(input("a: "))
b = int(input("b: "))
print(8*'-')
print(math.add_int(a, b))

print('')
print(' - add_float(float: a, float: b)')
a = float(input("a: "))
b = float(input("b: "))
print(8*'-')
print(math.add_float(a, b))

#print(' - add_int(int: a, int: b)')

#print(' - add_int(int: a, int: b)')



#print('Archivo: arrays.o')

#print(' - add_int(int: a, int: b)')

#print(' - add_int(int: a, int: b)')



