import json
import os
# Libreria colorama para mostrar por color el estado del promedio
import colorama 
from colorama import Fore
colorama.init()


# Con esta funcion lo que vamos hacer es un materia
# Luego vamos a ordenarlos de mayor a menor para mostrar los mejores estudiantes de esa materia


def borrarPantalla(): # Funcion para saber el sistema operativo, y dependiendo de ella aplicamos un borrado de pantalla
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")


def Ordenar():
  borrarPantalla()
  # Leemos el archivo Usuarios.json
  with open('Usuarios.json') as f:
    Usuarios = json.load(f)
  print (Fore.CYAN +"\n┏━━━━━━━━━━━━━━━━━━━━ ORDENAR Y MOSTRAR ━━━━━━━━━━━━━━━━━━━━┓")
  print ("\n           1. Ordenar y mostrar por Matematicas")
  print ("\n           2. Ordenar y mostrar por Ingles")
  print ("\n           3. Ordenar y mostrar por Programacion")
  print ("\n           4. Ordenar y mostrar por Semestre")
  print ("\n┗━━━━━━━━━━━━━━━━━━━━ ORDENAR Y MOSTRAR ━━━━━━━━━━━━━━━━━━━━┛")

  Materia = int ( input ("\n           Ingresa el valor numerico de la opcion de la materia  :  "))

  z = list(Usuarios.items())
  if Materia == 1 :
    z.sort(reverse=True,key=lambda x: (x[1]["Matematicas"]["Promedio"]))
    y = dict(z)
    # Crear arhivo con la informacion del json
    with open('PromedioMatematicas.json', 'w') as json_file:
      json.dump(y, json_file)
  if Materia == 2:
    z.sort(reverse=True,key=lambda x: (x[1]["Ingles"]["Promedio"]))
    y = dict(z)
    # Crear arhivo con la informacion del json
    with open('PromedioIngles.json', 'w') as json_file:
      json.dump(y, json_file)
  if Materia == 3 :
    z.sort(reverse=True,key=lambda x: (x[1]["Programacion"]["Promedio"]))
    y = dict(z)
    # Crear arhivo con la informacion del json
    with open('PromedioProgramacion.json', 'w') as json_file:
      json.dump(y, json_file)
  if Materia == 4 :
    z.sort(reverse=True, key=lambda x: (x[1]["Promedio_semestre"]))
    y = dict(z)
    # Crear arhivo con la informacion del json
    with open('Promediosemestre.json', 'w') as json_file:
      json.dump(y, json_file)