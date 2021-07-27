#!/usr/bin/env python
# encoding: utf8

import csv

ARCHIVO="agenda.csv"
CAMPOS=["Nombre","Apellido","Telefono","Cumpleanios"]

def leer_csv(datos_csv):
    """ Devuelve la siguiente lÃ­nea o None si se terminÃ³ el archivo. """
    try:
        return datos_csv.next()
    except:
        return None

def leer_datos(archivo):
    """ Carga todos los datos del archivo en una lista y la devuelve. """
    abierto = open(archivo)
    datos_csv = csv.reader(abierto)
    campos = leer_csv(datos_csv)
    datos = []
    elemento = leer_csv(datos_csv)
    while elemento:
        datos.append(elemento)
        elemento = leer_csv(datos_csv)
    abierto.close()
    return datos

def guardar_datos(datos, archivo):
    """ Guarda los datos recibidos en el archivo. """
    abierto = open(archivo,"w",newline='')
    datos_csv = csv.writer(abierto)
    datos_csv.writerow(CAMPOS)
    datos_csv.writerows(datos)
    abierto.close()

def leer_busqueda():
    """ Solicita al usuario nombre y apellido y los devuelve. """
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    return (nombre,apellido)

def buscar(nombre, apellido, datos):
    """ Busca el primer elemento que coincida con nombre y con apellido. """
    for elemento in datos:
        if nombre in elemento[0] and apellido in elemento[1]:
            return elemento
    return None

def menu_alta(nombre, apellido, datos):
    """ Pregunta si se desea ingresar un nombre y apellido y
        de ser asÃ­, pide los datos al usuario. """
    print ("No se encuentra %s %s en la agenda." % (nombre, apellido))
    confirmacion = input("¿Desea ingresarlo? (s/n) ")
    if confirmacion.lower() != "s":
        return
    telefono = input("Telefono: ")
    cumple = input("Cumpleanios: ")
    datos.append([nombre,apellido,telefono,cumple])

def mostrar_elemento(elemento):
    """ Muestra por pantalla un elemento en particular. """
    print ()
    print (" %s %s" % (elemento[0],elemento[1]))
    print ("Telefono: %s" % elemento[2])
    print ("Cumpleanios: %s" % elemento[3])
    print ()

def menu_elemento():
    """ Muestra por pantalla las opciones disponibles para un elemento
    existente. """
    o = input("b: borrar, m: modificar, ENTER para continuar (b/m): ")
    return o.lower()

def modificar(viejo, nuevo, datos):
    """ Reemplaza el elemento viejo con el nuevo, en la lista datos."""
    indice = datos.index(viejo)
    datos[indice] = nuevo

def menu_modificacion(elemento, datos):
    """ Solicita al usuario los datos para modificar una entrada. """
    nombre = input("Nuevo nombre: ")
    apellido = input("Nuevo apellido: ")
    telefono = input("Nuevo telefono: ")
    cumple = input("Nuevo cumpleanios: ")
    modificar(elemento, [nombre, apellido, telefono, cumple], datos)

def baja(elemento, datos):
    """ Elimina un elemento de la lista. """
    datos.remove(elemento)

def confirmar_salida():
    """ Solicita confirmaciÃ³n para salir """
    confirmacion = input("¿Desea salir? (s/n) ")
    return confirmacion.lower() == "s"

def agenda():
    """ FunciÃ³n principal de la agenda.
        Carga los datos del archivo, permite hacer bÃºsquedas, modificar
        borrar, y al salir guarda. """
    datos = leer_datos(ARCHIVO)
    fin = False
    while not fin:
        (nombre, apellido) = leer_busqueda()
        if nombre == "" and apellido == "":
            fin = confirmar_salida()
            continue
        elemento = buscar(nombre, apellido, datos)
        if not elemento:
            menu_alta(nombre, apellido, datos)
            continue
        mostrar_elemento(elemento)
        opcion = menu_elemento()
        if opcion == "m":
            menu_modificacion(elemento, datos)
        elif opcion == "b":
            baja(elemento, datos)
            
        guardar_datos(datos, ARCHIVO)

agenda()