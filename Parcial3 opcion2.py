# se implementan librerias 

import sqlite3
from math import e

#se nombra contadores y variables de cadena 
conexion = 0
nuevonombre=""
# esn esta funcion se implementa la creacion y conexion a la base datos 
def crear_conexion(base_datos): #el parametro recibido es el nombre  de la base de datos 
    global conexion 
    try:
        conexion = sqlite3.connect(base_datos) # se utiliza sqlite para crear una base de datos 

        return conexion # se retorna la conexion 
    except sqlite3.Error as error: # se implementa una excepcion por si el bloque try lanza un error 
        print('Se ha producido un error al crear la conexión:', error)
# en las siguiente 3 funciones se crean las tablas contenidas en la bases de datos   
def crear_tabla(conexion, definicion):# en esta parte se recibe la conexion y la definicion que es el parametro del lenguaje sql creando la tabla 
    cursor = conexion.cursor()#se conecta a la base de datos y crea un cursor  
    cursor.execute(definicion)# se ejecuta el lenguaje de sql antes decrito 
    conexion.commit() # se confirman cambios 
    # en las dos siguientes funciones se ejecuta lo mismo, cambiando de el parametro del sql 
def crear_tabla2(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()   
def crear_tabla3(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()        

def mostrar_tablas(conexion):# esta funcion presenta las tres tablas creadas 
    sql = "SELECT name FROM sqlite_master WHERE type='table';"#lenguaje que llama a las tablas 

    cursor = conexion.cursor()##se conecta a la base de datos y crea un cursor
    cursor.execute(sql)## se ejecuta el lenguaje de sql
    tablas = cursor.fetchall()# devuelve un array que contiene tadas las filas restantes del conjunto de resultados

    for t in tablas:    #se imprimen todas las tablas
        print(t[0])

def crear_usuario(conexion, usuario):# en esta funcion se da el nombre de la primer tabla
    sql = 'INSERT INTO usuario VALUES (?, ?);'#se inserta la tabla 

    cursor = conexion.cursor()#se conecta a la base de datos y crea un cursor
    cursor.execute(sql, usuario) #se ejecuta el lenguaje y el nombre de la tabla 

    conexion.commit() # se confirman cambios 
    # en la  siguientes funciones se ejecuta lo mismo, cambiando de el parametro del nombre de la tabla 
def crear_usuario2(conexion, usuario2):
    sql = 'INSERT INTO usuario2 VALUES (?, ?);'

    cursor = conexion.cursor()
    cursor.execute(sql, usuario2)

    conexion.commit()

def mostrar_usuarios(conexion):# esta funcion se utiliza para visualizar los datos de cada tabla
    sql = 'SELECT * FROM usuario;'#se ejecuta el codigo que llama a la tabla

    cursor = conexion.cursor()#se conecta a la base de datos y crea un cursor  
    cursor.execute(sql)# se ejecuta el lenguaje sql en la DB

    usuarios = cursor.fetchall()# devuelve un array que contiene tadas las filas restantes del conjunto de resultados
    return usuarios #retorna los datos 
# en la  siguientes funciones se ejecuta lo mismo, cambiando de el parametro del nombre de la tabla 
def mostrar_usuarios2(conexion):
    sql = 'SELECT * FROM usuario2;'

    cursor = conexion.cursor()
    cursor.execute(sql)

    usuarios = cursor.fetchall()
    
    return usuarios
def mostrar_many(conexion):
    sql = 'SELECT * FROM many;'

    cursor = conexion.cursor()
    cursor.execute(sql)

    usuarios = cursor.fetchall()

    return usuarios


#en las siguientes solicitudes se utilizan condicionales para solicitar del usuario los datos requeridos en las tablas
#se tiene en cuenta la relacion many too many que tiene la tercer tabla al no ser llenada por valores dictador del usuario directamente
#se tiene una relacion de atributos al tener diversas variables de almacenado monovaluado, derivado y atomico
def solicitar_datos_usuario():
    nmoscas = 0
    nplanta = 0


    while True:
        
        try:
            nmoscas = int(input('Ingrese la cantidad de moscas: '))

            if nmoscas > 0:
                break
            else:
                print('MENSAJE: Debe ingresar un valor entero positivo.')
        except ValueError:
            print('MENSAJE: Debe ingreser un valor entero.')

        print()
      
    while True:
        nplanta = input('Ingrese el nombre de la planta: ').strip()

        if len(nplanta):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para el nombre.')
        
        print()

    
    
    return nmoscas, nplanta
def solicitar_datos_usuario2(pos):

    nuplantas = 0
    nplanta = 0
    dato1 = mostrar_usuarios(conexion)


    while True:
        
        try:
            nuplantas = int(input('Ingrese la cantidad de plantas de {}: '.format(dato1[pos][1])))

            if nuplantas > 0:
                break
            else:
                print('MENSAJE: Debe ingresar un valor entero positivo.')
        except ValueError:
            print('MENSAJE: Debe ingreser un valor entero.')

        print()
      
    
    
    
    return nuplantas, dato1[pos][1]

def llenartabla3(conexion):
    sql = 'INSERT INTO many VALUES (?, ?, ?);'
    datos1= mostrar_usuarios(conexion)
    datos2= mostrar_usuarios2(conexion)
    resultado = []

    for i in range(0,len(datos1)):
        resultado.append((datos2[i][1],datos2[i][0],datos1[i][0]))

   
    
    for i in range(0,len(resultado)):
        cursor = conexion.cursor()
        cursor.execute(sql, (resultado[i][0],resultado[i][1],resultado[i][2]))
        conexion.commit()

def llenartabla3BDE(conexion,desde): #Metodo para llenar la tabla 3 cuando se ingrese a una base de datos existente.
    sql = 'INSERT INTO many VALUES (?, ?, ?);'
    datos1= mostrar_usuarios(conexion)[desde:]
    datos2= mostrar_usuarios2(conexion)[desde:]
    resultado = []

    for i in range(0,len(datos1)):
        resultado.append((datos2[i][1],datos2[i][0],datos1[i][0]))

   
    
    for i in range(0,len(resultado)):
        cursor = conexion.cursor()
        cursor.execute(sql, (resultado[i][0],resultado[i][1],resultado[i][2]))
        conexion.commit() 

#en esta funcion se encuentra el promedio de moscas entre cada arbol, y se determina la cantidad inicial de moscas        
def promedio(conexion):
    dato1= mostrar_usuarios(conexion)
    dato2 = mostrar_usuarios2(conexion)
    totalmoscas = 0
    totalplantas = 0

    for i in range(0,len(dato1)):
        totalmoscas += dato1[i][0]

    for i in range(0,len(dato2)):
        totalplantas += dato2[i][0] 

    resultado = totalmoscas/totalplantas
    print(totalmoscas)
    print(totalplantas)
    print(resultado)
    print(e)


    return resultado


    

   

#en las dos siguientes funciones sirven para cambiar datos que estan en las tablas usuario y usuario 2

def actualizar_usuario(conexion, usuario):
    global nuevonombre
    nuevonombre = ""
    #se utiliza el metodo where para filtrar datos 

    sql = 'UPDATE usuario SET nmoscas = ? WHERE nplanta = ?;' 
    bandera = True
    
    nuevovalor2=0
    while bandera:
        try:
            #se pide el nombre de la planta para cambiar el numero de moscas 
         entrada =  input("ingrese el nombre de la planta que quiere modificar el numero de moscas: ")
         nuevonombre = entrada

         entrada2 =  int(input("ingrese el nuevo numero de moscas: "))
         nuevovalor2 = entrada2
         bandera = False
         break

        except:
            print("dato no valido")

    
    cursor = conexion.cursor()
    cursor.execute(sql, (nuevovalor2, nuevonombre))
    conexion.commit()
def actualizar_usuario2(conexion, usuario2):

    sql = 'UPDATE usuario2 SET nuplantas = ? WHERE nplanta = ?;'
    bandera = True
    global nuevonombre
    nuevonombre=""
    nuevovalor2=0
    while bandera:
        try:
         entrada =  input("ingrese el nombre de la planta que quiere modificar el numero de plantas: ")
         nuevonombre = entrada

         entrada2 =  int(input("ingrese el nuevo numero de plantas: "))
         nuevovalor2 = entrada2
         bandera = False
         break

        except:
            print("dato no valido")

    
    cursor = conexion.cursor()
    cursor.execute(sql, (nuevovalor2, nuevonombre))
    conexion.commit()
#en esta funcion se utilizan condicionales, ciclos y listar para acuatulizar la relacion many too many
def actualizartabla3():


    dato1=mostrar_usuarios(conexion)
    dato2=mostrar_usuarios2(conexion)
    nuevasplantas = 0
    nuevasmoscas = 0
    sql = 'UPDATE many SET nuplantas = ?,nmoscas1 = ? WHERE nplanta = ?;'
    for i in range(0, len(dato1)):
        if nuevonombre in dato1[i]:
            nuevasmoscas = dato1[i][0]
        else: continue
    for i in range ( 0, len(dato2)):
        if nuevonombre in dato2[i]:
            nuevasplantas = dato2[i][0]
        else: continue

    
    cursor = conexion.cursor()
    cursor.execute(sql, (nuevasplantas,nuevasmoscas, nuevonombre))
    conexion.commit()
# en las dos siguientes funciones se utiliza el modelo obtenido en la explicacion y se multiplica por la cantidad de dias deseadas, para obtener la cantidad de moscas en totales en el cultivo 
def moscas5t ():
    valorinicial =promedio(conexion)
    a = valorinicial*e**3.40119738166
    return a
def moscas10t ():
    a = promedio(conexion)*e**6.80239476332
    return a

#la siguiente funcion es el proceso central de algoritmo al definir la creacion de tablas 
def main():
    a= input("digite el nombre de la base de datos: ")#se da el nombre de la base de datos 
    conexion = crear_conexion(a) #se crea la conexion a la base de datos 
   


   # se crean las tres tablas necesarias, con las variables requeridas para el modelaje a a partir del lenguaje sql 
    sql = """
    CREATE TABLE usuario(
          nmoscas INTEGER NOT NULL,
          nplanta TEXT NOT NULL
    );
    """
    sql2 = """
    CREATE TABLE usuario2(
          nuplantas INTEGER NOT NULL,
          nplanta TEXT NOT NULL
    );
    """
    sql3 = """
    CREATE TABLE many(
          nplanta TEXT NOT NULL,
          nuplantas INTEGER NOT NULL,
          nmoscas1 INTEGER NOT NULL
    );
    """

    nuevabd = True
    try:
        crear_tabla(conexion, sql)#se define el parametro del lenguaje sql donde esta la creacion de la tabla
        crear_tabla2(conexion, sql2)#se llama la funcion y se ejecuta el codigo que genera la tabla
        crear_tabla3(conexion, sql3) #se llama la funcion que crea la tabla 3
        print("SE HA CREADO UNA BASE DE DATOS NUEVA".center(50,"*"))
    except: #Como trabajamos con una estructura de base de datos fija, para saber si una base de datos existe podemos preguntar si las tablas ya están creadas
        #aprovechando la exepción que lanza cuando las tablas ya están creadas.
        print("LA BASE DE DATOS YA EXISTE, TENGA ENCUENTA QUE SE TRABAJARA CON LOS DATOS QUE INGRESES MAS LOS EXISTENTES EN LA BASE DE DATOS".center(50,"*"))
        nuevabd =False
        dato1Verificacion = mostrar_usuarios(conexion)
    # aqui se hace la primer tabla que tendra los datos usados por el usuario 
   
    print("TABLA #1".center(60,"+"))#metodo estetico
    entrada = int(input("ingrese la cantidad de datos que desee: "))#se ingre la cantidad de elementos que tendra la tabla
    for i in range(0,entrada):#se piden la cantidad de elementos requeridos 
        print("dato numero {}\n".format(i+1))#se muestra la posicion del dato
        usuario = solicitar_datos_usuario()#se llama la funcion que tiene los datos escritos por el usuari
        crear_usuario(conexion, usuario) #se crea la conexion a la base de datos

    print("TABLA #2".center(60,"+"))#metodo estetico
    
    for i in range(0,entrada):#segun la cantidad de datos antes requerido se ejecuta
        if nuevabd: #Si es una nueva base de datos que llene la tabla desde el inicio
            print("dato numero {}\n".format(i+1))#se muestra la posicion del dato
        
            usuario2 = solicitar_datos_usuario2(i)#se llama la funcion que tiene los datos escritos por el usuario
        
            crear_usuario2(conexion, usuario2)# se llena la tabla2
        elif not nuevabd: #Si la base de datos ya existe, llene la tabla desde el ultimo dato de la anterior tabla

            print("dato numero {}\n".format(i+1))#se muestra la posicion del dato
        
            usuario2 = solicitar_datos_usuario2(len(dato1Verificacion)+i)#se llama la funcion que tiene los datos escritos por el usuario
        
            crear_usuario2(conexion, usuario2)# se llena la tabla2


    if nuevabd:#Si es una nueva base de datos
        llenartabla3(conexion)#se llena la tabla 3
    elif not nuevabd:#Si es una base de datos existente
        llenartabla3BDE(conexion,len(dato1Verificacion))



    
    menu(usuario)
    if conexion:
     conexion.close()# se cierra la conexion 
# en esta funcion se utilizan ciclos y metodos del lenguaje sql para eliminar datos segun el parametro del nombre de la planta
def eliminar_usuario(conexion):
    sql = 'DELETE FROM usuario WHERE nplanta = ?;'
    sql2 = 'DELETE FROM usuario2 WHERE nplanta = ?;'
    sql3 = 'DELETE FROM many WHERE nplanta = ?;'
    
    bandera = True
    nuevovalor3=0
    
    while bandera:
        try:
         entrada5 =  input("ingrese el nombre de la planta que quiere borrar: ")
         nuevonombre = entrada5

         
         bandera = False
         break

        except:
            print("dato no valido")

    
    cursor = conexion.cursor()
    cursor.execute(sql,(nuevonombre,))
    conexion.commit()


    cursor = conexion.cursor()
    cursor.execute(sql2,(nuevonombre,))
    conexion.commit()


    cursor = conexion.cursor()
    cursor.execute(sql3,(nuevonombre,))
    conexion.commit()
#funcion que muestra las opciones al usuario 
def menu (us):
    bandera = True
    while bandera:
        print("menu".center(60,"+"))
        # esta es el menu principal que se muestra el usuario para que utilize todas las funciones antes explicadas,a partir de condicionales se filtran y ejecutan las funciones
        menu = "1. modificar datos de la tabla1\n 2. modificar datos de la tabla2\n 3. ver datos de la tabla\n 4.ver datos de la tabla2\n"\
            "5.ver datos de la tabla3 \n 6.ver cantidad de moscas a los 5 dias\n 7.ver cantidad de moscas a los 10 dias\n 8.eliminar datos de la tabla1 \n 9. mostar tablas\n 10. salir\n opcion = "
        entrada = input(menu)
        if entrada == "1":
            actualizar_usuario(conexion, us)
            actualizartabla3()
        elif entrada == "2":
            actualizar_usuario2(conexion, us)
            actualizartabla3()
        elif entrada == "3":
            print(mostrar_usuarios(conexion))
        elif entrada == "4":
             print(mostrar_usuarios2(conexion))
        elif entrada == "5":
            print(mostrar_many(conexion))
        elif entrada == "6":
           print("la cantidad de moscas totales en el cultivo de todas las plantas pasado los 5 dias es: {0:.4f}".format(moscas5t()))
        elif entrada == "7":
            print("la cantidad de moscas totales en el cultivo de todas las plantas pasado los 10 dias es: {0:.4f}".format(moscas10t()))
        elif entrada == "8":
            eliminar_usuario(conexion)
        elif entrada == "9":
            mostrar_tablas(conexion)
        elif entrada == "10":
            bandera = False
            break 
        else:
            print("opcion no valida")
        



main()