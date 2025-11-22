import os
import csv


def obtenerRutaArchivoCsv():
    nombreCarpeta = "datos"
    nombreArchivo = "paises.csv"
    rutaCompleta = os.path.join(nombreCarpeta, nombreArchivo)
    return rutaCompleta


def cargarPaisesDesdeCsv(rutaArchivoCsv):
    listaPaises = []
    with open(rutaArchivoCsv, "r", newline="") as archivo:
        read = csv.DictReader(archivo)
        for fila in read:
            nombre = fila.get("nombre", "").strip()
            poblacionTexto = fila.get("poblacion", "").strip()
            superficieTexto = fila.get("superficie", "").strip()
            continente = fila.get("continente", "").strip()

            if (
                nombre == ""
                or continente == ""
                or poblacionTexto == ""
                or superficieTexto == ""
                or not poblacionTexto.isdigit()
                or not superficieTexto.isdigit()
            ):
                print("Se omitio un registro por formato invalido en el CSV")
                continue

            pais = {
                "nombre": nombre,
                "poblacion": int(poblacionTexto),
                "superficie": int(superficieTexto),
                "continente": continente,
            }
            listaPaises.append(pais)
    return listaPaises


def guardarPaisesEnCsv(rutaArchivoCsv, listaPaises):
    with open(rutaArchivoCsv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        write = csv.DictWriter(archivo, fieldnames=campos)
        write.writeheader()
        for pais in listaPaises:
            write.writerow(
                {
                    "nombre": pais["nombre"],
                    "poblacion": pais["poblacion"],
                    "superficie": pais["superficie"],
                    "continente": pais["continente"],
                }
            )


def validacionTextoNoVacio(mensaje):
    texto = input(mensaje).strip()
    while texto == "":
        print("El valor no puede ser vacio")
        texto = input(mensaje).strip()
    return texto


def validacionNumeroPositivo(mensaje):
    texto = input(mensaje).strip()
    while not texto.isdigit() or int(texto) <= 0:
        print("Debe ingresar un numero entero positivo")
        texto = input(mensaje).strip()
    return int(texto)


def mostrarMenuPrincipal():
    print("...::: MENÚ PRINCIPAL :::...")
    print("1 - Agregar pais")
    print("2 - Actualizar población y superficie de un pais")
    print("3 - Buscar pais por nombre")
    print("4 - Filtrar paises por continente")
    print("5 - Filtrar paises por rango de población")
    print("6 - Filtrar paises por rango de superficie")
    print("7 - Ordenar paises por nombre")
    print("8 - Ordenar paises por población")
    print("9 - Ordenar paises por superficie")
    print("10 - Mostrar estadísticas")
    print("0 - Fin del programa")
    print("====================================")


def mostrarListaPaises(listaPaises):
    if len(listaPaises) == 0:
        print("No hay paises para mostrar")
        return

    for pais in listaPaises:
        print(
            pais["nombre"]
            + " - "
            + str(pais["poblacion"])
            + " - "
            + str(pais["superficie"])
            + " km" + "\u00B2"
            + " - "
            + pais["continente"]
        )
    print()


# Opción 1
def agregarPais(listaPaises):
    print("...::: Agregar pais :::...")
    nombre = validacionTextoNoVacio("Nombre: ")
    poblacion = validacionNumeroPositivo("Población: ")
    superficie = validacionNumeroPositivo("Superficie en km²: ")
    continente = validacionTextoNoVacio("Continente: ")

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    listaPaises.append(pais)
    print("Pais agregado correctamente")


def buscarIndicePaisPorNombre(listaPaises, nombreBuscado):
    nombreBuscadoMin = nombreBuscado.lower()
    indiceEncontrado = -1
    indice = 0
    while indice < len(listaPaises) and indiceEncontrado == -1:
        nombrePaisMin = listaPaises[indice]["nombre"].lower()
        if nombrePaisMin == nombreBuscadoMin:
            indiceEncontrado = indice
        indice += 1
    return indiceEncontrado


# Opcion 2
def actualizarPais(listaPaises):
    print("...::: Actualizar pais :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados para actualizar")
        return

    nombreBuscado = validacionTextoNoVacio("Ingrese el nombre EXACTO del pais a actualizar: ")
    indice = buscarIndicePaisPorNombre(listaPaises, nombreBuscado)

    if indice == -1:
        print("No se encontró un pais con ese nombre")
        return

    print("Pais encontrado:")
    mostrarListaPaises([listaPaises[indice]])

    nuevaPoblacion = validacionNumeroPositivo("Nueva población: ")
    nuevaSuperficie = validacionNumeroPositivo("Nueva superficie en km²: ")

    listaPaises[indice]["poblacion"] = nuevaPoblacion
    listaPaises[indice]["superficie"] = nuevaSuperficie
    print("Datos actualizados correctamente")


# Opcion 3
def buscarPaisPorNombre(listaPaises):
    print("...::: Buscar pais por nombre :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return

    textoBusqueda = validacionTextoNoVacio("Ingrese parte o todo el nombre a buscar: ").lower()
    resultados = []
    for pais in listaPaises:
        if textoBusqueda in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises que coincidan con la búsqueda")
    else:
        print("Paises encontrados:")
        mostrarListaPaises(resultados)

# Opcion 4
def filtrarPorContinente(listaPaises):
    print("...::: Filtrar paises por continente :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return

    continenteBuscado = validacionTextoNoVacio("Ingrese el continente a filtrar: ").lower()
    resultados = []
    for pais in listaPaises:
        if pais["continente"].lower() == continenteBuscado:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises para ese continente")
    else:
        print("Paises filtrados por continente:")
        mostrarListaPaises(resultados)

# Opcion 5
def filtrarPorRangoPoblacion(listaPaises):
    print("...::: Filtrar paises por rango de población :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return

    minimo = validacionNumeroPositivo("Población minima: ")
    maximo = validacionNumeroPositivo("Población maxima: ")

    while maximo < minimo:
        print("La población maxima no puede ser menor que la minima")
        maximo = validacionNumeroPositivo("Población maxima: ")

    resultados = []
    for pais in listaPaises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises en ese rango de población")
    else:
        print("Paises filtrados por rango de población:")
        mostrarListaPaises(resultados)


# Opcion 6
def filtrarPorRangoSuperficie(listaPaises):
    print("...::: Filtrar paises por rango de superficie :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return

    minimo = validacionNumeroPositivo("Superficie minima: ")
    maximo = validacionNumeroPositivo("Superficie maxima: ")

    while maximo < minimo:
        print("La superficie maxima no puede ser menor que la mínima.")
        maximo = validacionNumeroPositivo("Superficie maxima: ")

    resultados = []
    for pais in listaPaises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises en ese rango de superficie")
    else:
        print("Paises filtrados por rango de superficie:")
        mostrarListaPaises(resultados)


def obtenerNombrePais(pais):
    return pais["nombre"]


def obtenerPoblacionPais(pais):
    return pais["poblacion"]


def obtenerSuperficiePais(pais):
    return pais["superficie"]

# Opcion 7
def ordenarPorNombre(listaPaises):
    print("...::: Ordenar paises por nombre :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return
    listaPaises.sort(key=obtenerNombrePais)
    print("Paises ordenados por nombre (ascendente):")
    mostrarListaPaises(listaPaises)


# Opcion 8
def ordenarPorPoblacion(listaPaises):
    print("...::: Ordenar paises por población :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return
    listaPaises.sort(key=obtenerPoblacionPais)
    print("Paises ordenados por población (ascendente):")
    mostrarListaPaises(listaPaises)

# Opcion 9
def ordenarPorSuperficie(listaPaises):
    print("...::: Ordenar paises por superficie :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return

    print("1 - Superficie ascendente")
    print("2 - Superficie descendente")
    opcion = input("Elija una opción: ").strip()

    if opcion == "1":
        listaPaises.sort(key=obtenerSuperficiePais)
        print("Paises ordenados por superficie (ascendente):")
    elif opcion == "2":
        listaPaises.sort(key=obtenerSuperficiePais, reverse=True)
        print("Paises ordenados por superficie (descendente):")
    else:
        print("Opción inválida. No se modificó el orden de la lista")
        return

    mostrarListaPaises(listaPaises)

# Opcion 10
def mostrarEstadisticas(listaPaises):
    print("...::: Estadísticas :::...")
    if len(listaPaises) == 0:
        print("No hay paises cargados")
        return

    paisMayorPoblacion = listaPaises[0]
    paisMenorPoblacion = listaPaises[0]
    sumaPoblacion = 0
    sumaSuperficie = 0

    indice = 0
    while indice < len(listaPaises):
        pais = listaPaises[indice]
        if pais["poblacion"] > paisMayorPoblacion["poblacion"]:
            paisMayorPoblacion = pais
        if pais["poblacion"] < paisMenorPoblacion["poblacion"]:
            paisMenorPoblacion = pais

        sumaPoblacion += pais["poblacion"]
        sumaSuperficie += pais["superficie"]
        indice += 1

    promedioPoblacion = sumaPoblacion / len(listaPaises)
    promedioSuperficie = sumaSuperficie / len(listaPaises)

    conteoContinentes = {}
    for pais in listaPaises:
        cont = pais["continente"]
        if cont in conteoContinentes:
            conteoContinentes[cont] += 1
        else:
            conteoContinentes[cont] = 1

    print(f"Pais con mayor población: {paisMayorPoblacion['nombre']} ({paisMayorPoblacion['poblacion']})")
    print(f"Pais con menor población: {paisMenorPoblacion['nombre']} ({paisMenorPoblacion['poblacion']})")
    print(f"Promedio de población: {promedioPoblacion:.2f}")
    print(f"Promedio de superficie: {promedioSuperficie:.2f}")
    print("Cantidad de paises por continente:")
    for continente, cantidad in conteoContinentes.items():
        print(f"  {continente}: {cantidad}")
    print()

# Menú principal
def ejecutarPrograma():
    rutaArchivoCsv = obtenerRutaArchivoCsv()
    listaPaises = cargarPaisesDesdeCsv(rutaArchivoCsv)

    opcion = ""
    while opcion != "0":
        mostrarMenuPrincipal()
        opcion = input("Ingrese una opción: ").strip()
        print()
        match opcion:
            case "1":
                agregarPais(listaPaises)
                guardarPaisesEnCsv(rutaArchivoCsv, listaPaises)
                print("Cambios guardados")
            case "2":
                actualizarPais(listaPaises)
                guardarPaisesEnCsv(rutaArchivoCsv, listaPaises)
                print("Cambios guardados")
            case "3":
                buscarPaisPorNombre(listaPaises)
            case "4":
                filtrarPorContinente(listaPaises)
            case "5":
                filtrarPorRangoPoblacion(listaPaises)
            case "6":
                filtrarPorRangoSuperficie(listaPaises)
            case "7":
                ordenarPorNombre(listaPaises)
            case "8":
                ordenarPorPoblacion(listaPaises)
            case "9":
                ordenarPorSuperficie(listaPaises)
            case "10":
                mostrarEstadisticas(listaPaises)
            case "0":
                print("Fin del programa")
            case _:
                print("Opción inválida, reintente de nuevo")


# Iniciar el programa
ejecutarPrograma()
