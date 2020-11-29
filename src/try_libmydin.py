import ctypes as C
math = C.CDLL('./libmydyn.so')

# ----------------

# add_two.o

print('Archivo: add_two.o')

print('')
print(' - add_int(int: a, int: b)')

# Casteo correcto
math.add_int.argtypes = [C.c_int, C.c_int]
math.add_int.restype = C.c_int

a = int(input("a: "))
b = int(input("b: "))
print(8*'-')
print(math.add_int(a, b))

del a, b

# --------

print('')
print(' - add_float(float: a, float: b)')

# Casteo correcto
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]

a = float(input("a: "))
b = float(input("b: "))
print(8*'-')
print(math.add_float(a, b))

del a, b

# --------

print()
print(' - add_int_ref(int: a, int: b)')
a_ref = C.byref(C.c_int(int(input("a: "))))
b_ref = C.byref(C.c_int(int(input("b: "))))
res = C.c_int()
res_ref = C.byref(res)

# Cuenta 
math.add_int_ref(a_ref, b_ref, res_ref)

print(8*'-')
print(res.value)

del a_ref, b_ref, res, res_ref

# --------

print()
print(' - add_float_ref(float: a, float: b)')
a_ref = C.byref(C.c_float(float(input("a: "))))
b_ref = C.byref(C.c_float(float(input("b: "))))
res = C.c_float()
res_ref = C.byref(res)

# Cuenta 
math.add_float_ref(a_ref, b_ref, res_ref)

print(8*'-')
print(res.value)

del a_ref, b_ref, res, res_ref

# ----------------

# arrays.o

print('\n')
print('Archivo: arrays.o')

print('')
print(' - add_int_array(array: a, array: b)')

a = input("a: ")
b = input("b: ")

# Casteo como vectores int
def as_vect(x):
    x = x[1:-1]
    x = x.split(',')
    x = tuple(map(int, x))
    return x

a = as_vect(a)
b = as_vect(b)
# print(a[0], a[1], a[2])


a = (C.c_int * len(a))(*a)
b = (C.c_int * len(b))(*b)
res = C.c_float()
res_ref = C.byref(res)

# Cuenta 
math.add_int_array(C.byref(a), C.byref(b), res_ref, 3)

print(8*'-')
print(res.value)

del a, b, res, res_ref


# --------

print('')
print(' - dot_product(array: a, array: b)')



