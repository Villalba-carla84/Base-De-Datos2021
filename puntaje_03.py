#! /usr/bin/env python
# encoding: utf8

import pickle

def guardar_puntajes(nombre_archivo, puntajes):
    """ Guarda la lista de puntajes en el archivo.
    Pre: nombre_archivo corresponde a un archivo válido,
         puntajes corresponde a los valores a guardar
    Post: se guardaron los valores en el archivo en formato pickle.
    """

    archivo = open(nombre_archivo, "wb") #Agrego w (write) b (binary) para poder escribir en binario
    pickle.dump(puntajes, archivo)
    archivo.close()

def recuperar_puntajes(nombre_archivo):
    """ Recupera los puntajes a partir del archivo provisto.
        Devuelve una lista con los valores de los puntajes.
    Pre: el archivo contiene los puntajes en formato pickle
    Post: la lista devuelta contiene los puntajes en el
          mismo formato que se los almacenó.
    """

    archivo = open(nombre_archivo, "rb") #Agrego r (write) b (binary) para poder leer el binario
    puntajes = pickle.load(archivo)
    archivo.close()
    return puntajes

valores = [("lola", 89, "4:15"), ("Ramon", 23, "5:02")]
guardar_puntajes("puntajes_pickle_01.dat", valores)
print (recuperar_puntajes("puntajes_pickle_01.dat"))