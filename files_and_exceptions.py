def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas = {}
    with open(filename, 'r') as f:
        contenido = f.read().strip()
        if contenido:
            ventas_list = contenido.split(';')
            for venta in ventas_list:
                if venta:
                    try:
                        producto, valor = venta.split(':')
                        valor = float(valor)
                        if producto in ventas:
                            ventas[producto].append(valor)
                        else:
                            ventas[producto] = [valor]
                    except ValueError:
                        continue  # Ignora entradas mal formateadas
    return ventas


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto in data:
        ventas = data[producto]
        ventas_totales = sum(ventas)
        promedio = ventas_totales / len(ventas) if ventas else 0
        print(f"{producto}: ventas totales ${ventas_totales:.2f}, promedio ${promedio:.2f}")

