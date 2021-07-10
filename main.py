
"""
██████╗░██╗░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██████╗░░██████╗████████╗░█████╗░██╗░░░░░██╗░░██╗███████╗██████╗░
██╔══██╗██║██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░██╔╝██╔════╝██╔══██╗
██║░░██║██║███████║██╔████╔██║██║░░██║██╔██╗██║██║░░██║╚█████╗░░░░██║░░░███████║██║░░░░░█████═╝░█████╗░░██████╔╝
██║░░██║██║██╔══██║██║╚██╔╝██║██║░░██║██║╚████║██║░░██║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝██║██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║██████╔╝██████╔╝░░░██║░░░██║░░██║███████╗██║░╚██╗███████╗██║░░██║
╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

# Para el siguiente reto, dado que es a aleccion utilizando todo lo visto
# Se va a realizar un diccionario de estudiantes
# Cada estudiante tiene asignado 3 materias
# Cada materia tiene 5 notas y su promedio
# y cada estudiante tiene un promedio
"""
Estructura a utilizar
"1017256539":{
    "Nombre":"Carlos",
    "Materias":{
      "Matematicas":{
        "Notas": [ 5 , 4.5 , 3 , 1 , 3.4],
        "Promedio": "Valor a calcular"
      },
      "Ingles":{
        "Notas": [ 5 , 4.5 , 3 , 1 , 3.4],
        "Promedio": "Valor a calcular"
      },
      "Programacion":{
        "Notas": [ 5 , 4.5 , 3 , 1 , 3.4],
        "Promedio": "Valor a calcular"
      }
    },
    "Promedio_semestre":"Valor a calcular"
  }
"""
# Cada vez que se inserte un nuevo usuario, reescribiremos un archivo json que contiene los datos, dado quetrabajaremos con los json, no crearemos ningun diccionario global

import os
# Libreria colorama para mostrar por color el estado del promedio
import colorama 
from colorama import Fore
colorama.init()

import llenar
import Mostrar as Todos


def borrarPantalla(): # Funcion para saber el sistema operativo, y dependiendo de ella aplicamos un borrado de pantalla
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")

  
# ---------- Menu Principal ----------
# En esta, lo que haremos sera crear nuestro menu principal
# Donde le pediremos que inserte una opcion, y dependiendo de esta opcion llamaremos la funcion correspodiente

Opc = 1
while Opc != 0:
  borrarPantalla()
  print (Fore.CYAN +"\n┏━━━━━━━━━━━━━━━━━━━━ MENU ESTUDIANTES ━━━━━━━━━━━━━━━━━━━━┓")
  print ("\n           1. Insertar nuevo estudiantes")
  print ("\n           2. Mostrar todos los estudiantes")
  print ("\n           3. Buscar un usario y mirar si aprobo")
  print ("\n           4. Mostrar los mejores estudiantes por materia")
  print ("\n           5. Mostrar los mejores promedios del semestre")
  print ("\n┗━━━━━━━━━━━━━━━━━━━━ MENU ESTUDIANTES ━━━━━━━━━━━━━━━━━━━━┛")

  Opc = int (input (" \n          Ingrese el valor numerico segun el menu  "))

  if Opc == 1: llenar.Nuevo_usuario()
  if Opc == 2: Todos.mostrar()
  if Opc == 0: input (" Presiona Enter para finalizar...")