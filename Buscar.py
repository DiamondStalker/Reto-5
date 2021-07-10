import json
import os
# Libreria colorama para mostrar por color el estado del promedio
import colorama 
from colorama import Fore
colorama.init()


def borrarPantalla(): # Funcion para saber el sistema operativo, y dependiendo de ella aplicamos un borrado de pantalla
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")

def Buscar_estudiante():
  borrarPantalla()
  # Leemos el archivo Usuarios.json
  with open('Usuarios.json') as f:
    Usuarios = json.load(f)

  print (Fore.BLUE +"\n┏━━━━━━━━━━━━━━━━━━━━ BUSCAR ESTUDIANTE ESTUDIANTES ━━━━━━━━━━━━━━━━━━━━┓")
  Id = input ("          Ingresa el id a buscar  ")

  if Id in Usuarios:

      print (Fore.BLUE + f"\n           NIT  : {Id}")
      print (Fore.BLUE +"               Nombre  :  " + Usuarios[Id]["Nombre"])

      Aprobo_Reprobo(Usuarios[Id]["Matematicas"]["Promedio"],"Matematicas")
      Aprobo_Reprobo(Usuarios[Id]["Ingles"]["Promedio"],"Ingles")
      Aprobo_Reprobo(Usuarios[Id]["Programacion"]["Promedio"],"Programacion")
      Aprobo_Reprobo(Usuarios[Id]["Promedio_semestre"],"Promedio semestre")
  else: print(Fore.RED+"          El usuario no existe  ")
    
  print (Fore.BLUE +"\n┗━━━━━━━━━━━━━━━━━━━━ BUSCAR ESTUDIANTE ESTUDIANTES ━━━━━━━━━━━━━━━━━━━━┛")
  input(Fore.BLUE+"          Presiona ENTER para continiar...  ")

def Aprobo_Reprobo(valor,materia):
  if valor >= 3.5: print (Fore.GREEN + f"                 {materia} se aprobo con : {valor}")
  else: print (Fore.RED + f"                 {materia} se reprobo con : {valor}")