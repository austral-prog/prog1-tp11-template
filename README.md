# Trabajo Práctico 11

## Files y Exceptions

En este ejercicio, trabajarás con archivos y manejo de excepciones en Python.

El objetivo es leer un archivo de texto donde cada venta está en el formato `producto:valor_de_venta;producto:valor_de_venta;...`. Deberas cargar los datos en un diccionario donde la clave es el producto y el valor es una lista con todos los montos de ventas para ese producto.

Luego, deberás procesar ese diccionario para imprimir, para cada producto, el total vendido y el promedio de ventas, en el siguiente formato:

```
producto: ventas totales $X.XX, promedio $Y.YY
```

Además, deberás manejar las excepciones que puedan surgir al trabajar con archivos, como el caso en que el archivo no exista.

### 1. Leer un archivo y agrupar ventas por producto

Implementa la función `read_file_to_dict` que reciba el nombre de un archivo, lea la línea de ventas y agrupe los montos en una lista por producto. Cada venta tiene el formato `producto:valor` y las ventas están separadas por punto y coma `;`.

Ejemplo de archivo:

```
producto1:100;producto2:200;producto1:150;producto3:50;producto2:100;
```

La función debe devolver:

```python
{
    'producto1': [100.0, 150.0],
    'producto2': [200.0, 100.0],
    'producto3': [50.0]
}
```

### 2. Procesar el diccionario

Implementa la función `process_dict` que reciba el diccionario y, para cada producto, imprima:

```
producto: ventas totales $X.XX, promedio $Y.YY
```

Por ejemplo, para el diccionario anterior:

```
producto1: ventas totales $250.00, promedio $125.00
producto2: ventas totales $300.00, promedio $150.00
producto3: ventas totales $50.00, promedio $50.00
```