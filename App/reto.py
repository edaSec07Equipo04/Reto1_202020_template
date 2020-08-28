"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it

from Sorting import quicksort as qu

from time import process_time 

ar = "ARRAY_LIST"

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1



def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def lessAverageMovie(elemento1,elemento2):
    """Método que devuelve True si el elemento 1 es menor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_AVERAGE)"""

    return elemento1["vote_average"]<elemento2["vote_average"]

def greaterAverageMovie(elemento1,elemento2):

    """Método que devuelve True si el elemento 1 es mayor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_AVERAGE)"""

    return elemento1["vote_average"]>elemento2["vote_average"]

def lessCountMovie(elemento1,elemento2):
    """Método que devuelve True si el elemento 1 es menor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_COUNT)"""

    return elemento1["vote_count"]<elemento2["vote_count"]

def greaterCountMovie(elemento1,elemento2):
    """Método que devuelve True si el elemento 1 es mayor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_COUNT)"""

    return elemento1["vote_count"]>elemento2["vote_count"]


def requerimiento_b(lst,count, sortingPreference, sortingOrder):
    if sortingPreference == "votos" and sortingOrder == "menor":
        lt.ordenamiento_shell(lst,lessCountMovie)
    elif sortingPreference == "votos" and sortingOrder == "mayor":
        lt.ordenamiento_shell(lst,greaterCountMovie)
    elif sortingPreference == "calificación" or sortingPreference == "calificacion" and sortingOrder == "menor":
        lt.ordenamiento_shell(lst,lessAverageMovie)
    elif sortingPreference == "calificación" or sortingPreference == "calificacion" and sortingOrder == "mayor":
        lt.ordenamiento_shell(lst,lessAverageMovie)

    resultado = lt.newList("ARRAY_LIST") 

    for i in range(1,count+1):

        pelicula = lt.getElement(lst,i)
        lt.addLast(resultado,pelicula)
 
    return resultado





def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMovies()

            elif int(inputs[0])==2: #opcion 2
                if lstmovies==None or lt.size(lstmovies)==0: #Comprobar que la lista no esté vacía
                    print('La lista está vacía.')
                else:
                    asking = True
                    moviesNumber = input("Ingrese el número de películas que quiere tener en su ranking: ")
                    problem = "El número de películas debe ser mayor o igual a diez (10)"
                    while asking:
                        if int(moviesNumber) < 10:
                            print(problem)
                            moviesNumber = input("Ingrese el número de películas que quiere tener en su ranking: ")      
                        else:
                            asking = False
                            sortingPreference = input("- Digite 'votos' si desea ordenar su ranking por cantidad de votos.\n- Digite 'calificacion' si desea ordenar su rankin por calificación promedio.\n")
                            sortingOrder = input("- Digite 'menor' si desea ordenar su ranking de menor a mayor.\n- Digite 'mayor' si desea ordenar su ranking de mayor a menor.\n")
                            nuevo = requerimiento_b(lstmovies,int(moviesNumber), sortingPreference.lower(), sortingOrder.lower())
                    print(lt.size(nuevo))

            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()