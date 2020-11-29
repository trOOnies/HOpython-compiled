import ctypes as C
math = C.CDLL('./libmydyn.so')

# ----------------

print('Iniciando libmydyn.so...')
print('Autor: Facundo M. Scasso')
print()

print('¿Quiere probar alguna funcion en especifico?')
print('(Tambien puede utilizar las iniciales en minuscula. Por ejemplo: \'ai\'.)')
print()
print('0: Probar todas las funciones')
print('1: add_int')
print('2: add_float')
print('3: add_int_ref')
print('4: add_float_ref')
print('5: add_int_array')
print('6: dot_product')
mode = input('# ')
print()
print()

if mode == '0':
    mode = 0
else:
    try:
        mode = int(mode)
    except:
        dict_int_mode = {'ai': 1, 'af': 2, 'air': 3, 'afr': 4, 'aia': 5, 'dp': 6}
        mode = dict_int_mode[mode]


# ----------------

# add_two.o

print('Archivo: add_two.o')
if mode > 4:
    print('La funcion seleccionada no esta en este archivo.')

if mode == 0 or mode == 1:
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

if mode == 0 or mode == 2:
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

if mode == 0 or mode == 3:
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

if mode == 0 or mode == 4:
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
if mode != 0 and mode < 5:
    print('La funcion seleccionada no esta en este archivo.')


if mode == 0 or mode == 5:
    print('')
    print(' - add_int_array(array: a, array: b)')

    a = input("a: ")
    b = input("b: ")

    # Casteo como vectores int
    def as_vect_int(x):
        x = x[1:-1]
        x = x.split(',')
        x = tuple(map(int, x))
        return x

    a = as_vect_int(a)
    b = as_vect_int(b)
    # print(a[0], a[1], a[2])


    a = (C.c_int * len(a)) (*a)
    b = (C.c_int * len(b)) (*b)
    res = (C.c_int * len(a)) ()
    res_ref = C.byref(res)

    if len(a) != len(b):
        raise TypeError('Los vectores no son del mismo tamaño')

    # Cuenta 
    math.add_int_array(C.byref(a), C.byref(b), res_ref, len(a))

    print(8*'-')
    print(list(res))

    del a, b, res, res_ref


# --------

if mode == 0 or mode == 6:
    print('')
    print(' - dot_product(array: a, array: b)')

    # Casteo correcto
    math.dot_product.restype = C.c_float

    a = input("a: ")
    b = input("b: ")

    # Casteo como vectores float
    def as_vect_float(x):
        x = x[1:-1]
        x = x.split(',')
        x = tuple(map(float, x))
        return x

    a = as_vect_float(a)
    b = as_vect_float(b)

    a = (C.c_float * len(a)) (*a)
    b = (C.c_float * len(b)) (*b)

    if len(a) != len(b):
        raise TypeError('Los vectores no son del mismo tamaño')

    print(8*'-')
    print(math.dot_product(a, b, len(a)))

    del a, b
