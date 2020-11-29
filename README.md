# Compiled languages into Python

*Autor: Facundo M. Scasso*

En este hands-on practicamos cómo llamar a una librería
nuestra desde Python. En la carpeta `src/` tenemos dos archivos de C: add_two.c y arrays.c

Para completar este ejercicio tuve que efectuar los siguientes pasos:


### 1. Compilar ambos archivos como objetos separados

Compilo los 2 archivos de C con el flag -fPIC para que la compilación no asuma que los voy a correr/utilizar con un cierto orden.
```
> gcc -c -fPIC arrays.c add_two.c
```


### 2. Construir una librería dinámica que tenga ambos objetos

Creo la librería dinámica **libmydyn<span>.so<span>** con la siguiente sintaxis:
```
> gcc -shared arrays.o add_two.o -o libmydyn.so
```

Y verifico con 'nm' qué hay dentro del shared object que creé:

```
> nm -n libmydyn.so
(...)
00000000000010f9 T add_int_array
0000000000001170 T dot_product
00000000000011ea T add_float
0000000000001208 T add_int
0000000000001220 T add_float_ref
0000000000001257 T add_int_ref
(...)
```

Estos renglones son aquellos que nos confirman que el shared object no sólo contiene las funciones incluidas en los archivos de C, sino que se encuentran definidas llegadas a este paso, y son ejecutables (T).


### 3. Escribir un script en Python que pruebe **todas** las funciones de la librería

Creo el script en la misma carpeta de trabajo, y lo abro con Visual Studio Code:
```
> touch try_libmydyn.py
> code try_libmydyn.py
```

Pueden ver el detalle del archivo entrando al código y leyendo los comentarios, pero a grandes rasgos:

1. Utilicé Ctypes como vimos en clase para correr funciones de C previamente compiladas en una librería dinámica llamada 'libmydym.so'.
2. Generé una calculadora interactiva a partir de la implementación del punto 1, donde el usuario puede imputar los valores a operar.
3. Para facilitar la operación de la herramienta, generé una pequeña estructura lógica en que uno puede elegir mediante un input inicial si quiere probar todas las funciones de corrido, o si quiere probar una única función. Pueden encontrar este parámetro en el código con el nombre **mode**.

El ejecutable es relativamente simple, pero vale la siguiente aclaración:

Para las funciones 5 y 6 -en las que uno opera con vectores- la sintaxis esperada en el input deberá verse de la siguiente forma:
```
a: [1,2,3]
b: [10,32,-3]
```
Es decir, se espera que el usuario escriba el vector como si fuese una objeto lista de Python. La conversión a tipos con los que puede trabajar C se realiza de forma automática por detrás.
