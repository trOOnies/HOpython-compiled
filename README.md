# Compiled languages into Python

En este hands-on vamos a practicar cómo llamar a una librería
nuestra desde python. En la carpeta `src/` tienen dos archivos de C.
Para completar este ejercicio tienen que hacer los siguientes pasos:


### 1. Compilar ambos archivos como objetos separados

Compilo los 2 archivos de C con el flag -fPIC para que la compilación no asuma que los voy a correr/utilizar en cierto orden.
gcc -c -fPIC arrays.c add_two.c



### 2. Construir una librería dinámica que tenga ambos objetos

Creo la librería dinámica 'libmydyn.so' con la siguiente sintaxis:
gcc -shared arrays.o add_two.o -o libmydyn.so

Y verifico con 'nm' qué hay dentro del shared object que creé:
nm -n libmydyn.so

```
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


### 3. Escribir un script en python que pruebe **todas** las funciones de la librería





