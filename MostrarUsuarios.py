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

def Mostrar_Agenda():
  borrarPantalla()
  # Leemos el archivo Usuarios.json
  with open('Usuarios.json') as f:
    Usuarios = json.load(f)
  
  print (Fore.BLUE +"\n┏━━━━━━━━━━━━━━━━━━━━ TODOS LOS ESTUDIANTES ━━━━━━━━━━━━━━━━━━━━┓")

  for x,y in Usuarios.items():
    
    print (Fore.BLUE + f"\n           NIT  : {x}")
    print (Fore.BLUE +"               Nombre  :  " + Usuarios[x]["Nombre"])

    Aprobo_Reprobo(Usuarios[x]["Matematicas"]["Promedio"],"Matematicas")
    Aprobo_Reprobo(Usuarios[x]["Ingles"]["Promedio"],"Ingles")
    Aprobo_Reprobo(Usuarios[x]["Programacion"]["Promedio"],"Programacion")
    Aprobo_Reprobo(Usuarios[x]["Promedio_semestre"],"Promedio semestre")

   
  print (Fore.BLUE +"\n┗━━━━━━━━━━━━━━━━━━━━ TODOS LOS ESTUDIANTES ━━━━━━━━━━━━━━━━━━━━┛")
  input ("\n           Presiona ENTER para continuar...")

def Aprobo_Reprobo(valor,materia):
  if valor >= 3.5: print (Fore.GREEN + f"                 {materia} se aprobo con : {valor}")
  else: print (Fore.RED + f"                 {materia} se reprobo con : {valor}")