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


# ---------- Nuevo usuario ----------
def Nuevo_usuario():
  borrarPantalla()
  # Leemos el archivo Usuarios.json
  with open('Usuarios.json') as f:
    Usuarios = json.load(f)
    
  print (Fore.RESET +"\n┏━━━━━━━━━━━━━━━━━━━━ DATOS NUEVO ESTUDIANTE ━━━━━━━━━━━━━━━━━━━━┓")
  Idu = input ("\n          Id del estudiante  ")

  if Idu in Usuarios: 
    print (Fore.RED+"\n          El usuario ya exite  ")
    input("\n          Presiona ENTER para continuar...")
  else:
    Nombreu = input (Fore.RESET+"\n          Nombre del estudiante  ")
    print ("\n┗━━━━━━━━━━━━━━━━━━━━ DATOS NUEVO ESTUDIANTE ━━━━━━━━━━━━━━━━━━━━┛")

    Matematicasu = []
    Inglesu = []
    Programacionu = []

    PromedioM = float(0)
    PromedioI = float(0)
    PromedioP = float(0)
    PromedioS = float(0)

    for i in range (0,3):
      borrarPantalla()
      if i == 0:
        print (Fore.RESET +"\n┏━━━━━━━━━━━━━━━━━━━━ INSERTE NOTAS DE MATEMATICAS ━━━━━━━━━━━━━━━━━━━━┓")
        Llenar_notas(Matematicasu,0)
        print ("\n┗━━━━━━━━━━━━━━━━━━━━ INSERTE NOTAS DE MATEMATICAS ━━━━━━━━━━━━━━━━━━━━┛")
      if i == 1: 
        print (Fore.RESET +"\n┏━━━━━━━━━━━━━━━━━━━━ INSERTE NOTAS DE INGLES ━━━━━━━━━━━━━━━━━━━━┓")
        Llenar_notas(Inglesu,0)
        print ("\n┗━━━━━━━━━━━━━━━━━━━━ INSERTE NOTAS DE INGLES ━━━━━━━━━━━━━━━━━━━━┛")
      if i == 2: 
        print (Fore.RESET +"\n┏━━━━━━━━━━━━━━━━━━━━ INSERTE NOTAS DE PROGRAMACION ━━━━━━━━━━━━━━━━━━━━┓")
        Llenar_notas(Programacionu,0)
        print ("\n┗━━━━━━━━━━━━━━━━━━━━ INSERTE NOTAS DE PROGRAMACION ━━━━━━━━━━━━━━━━━━━━┛")
        
        

    for i in range (0,3):
      if i == 0: PromedioM = Promedio(Matematicasu)
      if i == 1: PromedioI = Promedio(Inglesu)
      if i == 2: PromedioP = Promedio(Programacionu)

    PromedioS = ((PromedioM+PromedioI+PromedioP)/3)
    Datos = {}
    Datos=dict(
      Nombre = Nombreu,
      Matematicas = dict(Notas=Matematicasu,Promedio=PromedioM),
      Ingles = dict(Notas=Inglesu,Promedio=PromedioI),
      Programacion = dict(Notas=Programacionu,Promedio=PromedioP),
      Promedio_semestre = PromedioS
      )

    Usuarios[Idu]=Datos
    # Crear arhivo con la informacion del json
    with open('Usuarios.json', 'w') as json_file:
      json.dump(Usuarios, json_file)


    borrarPantalla()
    print (Fore.RESET +"\n┏━━━━━━━━━━━━━━━━━━━━ SE INSERTO━━━━━━━━━━━━━━━━━━━━┓")
    print( Fore.RESET + f"\n          El usuario con el id {Idu} y de nombre {Nombreu} fue insertado correctamente")

    Promedio_msg(PromedioM,"Matematicas")
    Promedio_msg(PromedioI,"Ingles")
    Promedio_msg(PromedioP,"Programacion")
    Promedio_msg(PromedioS,"Semestre")

    print (Fore.RESET + "\n┗━━━━━━━━━━━━━━━━━━━━ SE INSERTO ━━━━━━━━━━━━━━━━━━━━┛")
    input(Fore.RESET + "\n          Presiona ENTER para continuar...")


# ---------- imprime por color si gano con el promedio dado ----------

def Promedio_msg(Promedio,Nombre):
  if Promedio >= 3.5: print (Fore.GREEN + f"\n          El promedio de {Nombre} fue de {Promedio} y esta se aprobo")
  else: print (Fore.RED + f"\n          El promedio de {Nombre} fue de {Promedio} y esta se reaprobo")

# ---------- Calcular promedio asignatura ----------
def Promedio(lista):
  promedio = float(0)
  for i in lista:
    promedio = promedio + i
  return promedio / 5

  
# ---------- Insertar nota Matematicas ----------
def Llenar_notas(lista,i):
  if i < 5:
    valor = float ( input (f"\n          Ingrese la nota #{i+1} entre los  0 - 5 : "))

    if valor >=0 and valor <= 5:
      lista.append(valor)
      Llenar_notas(lista,i+1)
    else:Llenar_notas(lista,i)
  return lista
  