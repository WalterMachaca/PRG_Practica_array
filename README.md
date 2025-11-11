# ARRAYS

## 1.-CONCEPTO
### En programación, un array (o arreglo en español) es una estructura de datos que almacena una colección de elementos, los cuales son del mismo tipo, en una secuencia contigua. Es una de las estructuras más utilizadas debido a su eficiencia en el acceso a datos y su simplicidad para representar colecciones de valores relacionados. Los arrays permiten almacenar múltiples valores en una sola variable, lo que facilita el trabajo con grandes volúmenes de datos. Cada elemento dentro del array está asociado con un índice, que es una posición numérica que permite acceder a un valor específico.
[link de referencia](https://msmk.university/array-en-programacion-concepto-tipos-y-ejemplos/)
![](Carpetas/Array.PNG)
[link de referencia](https://codigosdeprogramacion.com/cursos/?lesson=5-arreglos-y-matrices-arrays)
## 2.-CARACTERÍSTICAS
### Tamaño Fijo: En la mayoría de los lenguajes de programación, una vez que se declara un array, su tamaño no puede cambiar durante la ejecución del programa. Sin embargo, algunos lenguajes como Python permiten trabajar con listas, que son más flexibles.
### Elementos Homogéneos: Todos los elementos del array deben ser del mismo tipo de datos, como enteros, cadenas de texto o números flotantes. Algunos lenguajes de programación permiten arrays de tipos mixtos, pero esto no es común.
### Acceso Rápido: El acceso a un elemento del array es muy rápido, ya que se utiliza el índice para calcular la dirección de memoria del elemento.

## 3.-TIPOS DE ARRAYS
### Array unidimensional: El array unidimensional es simplemente una lista de elementos que están dispuestos en una única fila. Es el tipo mas básico de array.
   ```bash
   numeros = [10,20,30,40,50]
   print(numeros[2]) # Acceso al tercer elemento, salida: 30 
   ```
### Array multidimensional: Es un array que contiene otros arrays como elementos. Los arrays multidimensionales más comunes son los arrays bidimensionales (matrices), pero también existen de más dimensiones
   ```bash
   matriz = [[1,2,3],[4,5,6],[7,8,9]]
   print(matriz[1][2]) # Acceso al tercer elemento de la segunda fila, salida: 6
   ```

