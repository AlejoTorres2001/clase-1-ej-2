# Ejercicio 1

Usted es un cientifico de datos junior, recientemente contratado por la empresa [MSubs](https://www.msubs.com/) lider en la fabricacion de submarinos. Se encuentra tomando un cafe cuando de repente suena la alarma de emergencias!

Las llaves de su jefe se cayeron al fondo del oceano y es su tarea encontrarlas.

Para esto se le ha preparado un submarino especial el cual puede adentrarse en altas profundidades.Una vez dentro usted se dirige al fondo del ocenao donde su submarino realiza un **barrido por sonar** de todo el fondo del oceano.

En una pequeña pantalla, el submarino reporta los datos del **barrido** (datos.txt)

*cada linea es una medida de la profunidad a la que se encuentra el fondo del oceano*.

Por ejemplo suponga que tiene el siguiente reporte:

```python
199
200
208
210
200
207
240
269
260
263
```

Esto indica que el sonar ha detectado profunidad de 199,200,208,210,200,207,240,269,260 y 263 metros.

---

**Su primer tarea es descubrir que tan rapido la profundidad aumenta**

Para hace esto, *cuente el numero de veces que una medicion de profunidad aumenta, con respecto a la medicion anterior*
consideracion: No hay medicion anterior a la primer medicion de su reporte.
retomando el ejemplo anterior: los cambios son los siguientes:

```python
199 (N/A - no hay medicion anterior)
200 (aumento)
208 (aumento)
210 (aumento)
200 (decremento)
207 (aumento)
240 (aumento)
269 (aumento)
260 (decremento)
263 (aumento)
```
En este ejemplo hay **7** mediciones que son mayores a las mediciones anteriores

**Cuantas medicione son mayores que su medicion anterior?**

## Elabore un programa que:

1. **lea el reporte de profundidad**
2. **cuente el numero de mediciones que son mayores a la medicion anterior**


# Ejercicio 2 (Opcional):

Considerar cada una de las mediciones no es tan eficiente como usted creia,existe mucho ruido en esos datos!

Entonce se le ocurre considerar **sumas de 3 mediciones consecuticas**.

Nuevamente, considerando el ejemplo anterior:
```python
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

```
Comienze por comparar las primeras y las segundas 3 mediciones consecutivas

las primeras mediciones 
estan marcadas con A (199, 200, 208) y su suma es 199 + 200 + 208 = 607

las segundas mediciones estan marcadas con B (200, 208, 210) y su suma es 200 + 208 + 210 = 618

la suma de las segunda mediciones (B) es *MAYOR* a la suma de las primeras mediciones (A) **por lo que en esta comparacion la profunidad aumenta**

Usted debe contar el numero de veces que la suma de estas mediciones consecutivas es mayor a la anterior suma de las mediciones consecutivas

```python
A: 607 (no hay suma previa)
B: 618 (aumento)
C: 618 (no hay cambio)
D: 617 (decremento)
E: 647 (aumento)
F: 716 (aumento)
G: 769 (aumento)
H: 792 (aumento)
```
En este ejemplo hay **5** sumas que son mayores a las sumas anteriores

**Cuantas sumas son mayores que la suma anterior?**

## Elabore un programa que:

1. **Lea el reporte de profundidad**
2. **Cuente el numero de sumas que son mayores a la suma anterior**

**Puede realizar un fork del repositorio y trabajar sobre una nueva rama *nom_alumno/solucion* para luego realizar una Pull Request a este repositorio con su trabajo**
