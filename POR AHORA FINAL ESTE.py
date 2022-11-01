

import mysql.connector
import pygame

from solver import solve, valid
pygame.font.init()
from GUI import main



from preguntas import pregunta1, pregunta2, pregunta3, pregunta4, pregunta5



mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin",
        database="sudoku")
print("Me conecte")
mycursor = mydb.cursor(buffered = True)



def ponerNivelUNO(nivel_1, usuario):
    cero="UPDATE usuarios SET puntos= %s WHERE usuario =%s"
    mycursor.execute(cero,(nivel_1,usuario))
    mydb.commit()




def actualizar(nivel,usuario): 
    consulta=''' UPDATE usuarios SET puntos= puntos + %s WHERE usuario =%s'''
    mycursor.execute(consulta,(nivel,usuario))
    mydb.commit()








def comprobar_usuario(user):
    sql = "SELECT usuario, puntos FROM usuarios WHERE usuario = '%s'" % user
    mycursor.execute(sql)         
    registro = mycursor.fetchone()
    if registro != None:
        print ("Usuario Registrado",registro)
        print("PUNTAJE: ", registro[1])
        return registro[1]
                
    else:                    #Si no existe nada
        print("no hay registro")
        mycursor.reset()
        return False







def Inicio_Sesion(user,contra):
    
    sql = "SELECT usuario, puntos, password FROM usuarios WHERE usuario = '%s'" % user 
    mycursor.execute(sql) 
    registro = mycursor.fetchone()

    if registro != None:
        print("Te encuentras en el NIVEL: ", registro[1])
    
        if contra==registro[2]: 
            return True,registro[1]
    
        else: print("contraseña incorrecta")
        return False
       
                
    else:                    #Si no existe nada
        print("no hay registro")
        mycursor.reset()
        return False







while True:
    
    print(
        """
        0. Salir
        1.Agregar un usuario
        2.Consultar tu puntuacion
        3.----JUGAR------
        4.Bajar puntuacion a cero
        5.Prueba de inicio de sesion
    
        """

    )
    opcion=int(input("seleccione la opcion: "))
    if opcion==0:
        break
    elif opcion==1:
        user=input("Digite el usuario: ")
        contra=str(input("Digite la contraseña: "))
        level=0
        sql='INSERT INTO usuarios (usuario,password,puntos) VALUES (%s,%s,%s)'
        mycursor.execute(sql, (user,contra,level))
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)

    #Comprobar que el usuario exista
    elif opcion==2:
        user = input("Ingrese usurio: ") 
        comprobar_usuario(user)

    #JUGAR con usuario

    elif opcion==3:
        print("selecciono 3")
        user=input("escriba su usuario: ")
        password=input("escriba la contraseña: " )
        
        resultado=Inicio_Sesion(user,password)
        
        if resultado != False:
        
            print("\n----iniciaste sesion de manera correcta----\n")
            puntitos=(main()[1])
            
            pygame.quit()
            print("--- FElicidades completaste el sudoku")
            print("Has ganado 1000 puntos por completar el sudoku")
            print("tuviste",puntitos,"errores")
            puntuacion=1000-(puntitos*5)
            print("\nTu puntuacion final es de",puntuacion)
            ponerNivelUNO(puntuacion,user)

          
        






        
                
        
        

        
    elif opcion==4:
        print("Selecciono 4")
        nivelBajar=0
        user=input("eliga usuario: ")
        ponerNivelUNO(nivelBajar,user)
        print("La puntuacion del ",user,"ha sido bajado a 0.")
    
    elif opcion==5:
        user=input("escriba usuario: ")
        password=input("escriba su contraseña: ")
        Inicio_Sesion(user,password)
        if Inicio_Sesion != False:
            print("iniciaste sesion de manera correcta")
        

        

mydb.close()
print("cerre la base de datos")





#sql = "SELECT usuario, nivel FROM usuarios WHERE usuario = '%s'" % user
 #       mycursor.execute(sql)         
  #      registro = mycursor.fetchone()
   #     if registro != None:
    #        print ("Usuario Registrado",registro)
            
     #       nuevo_nivel=1
      #      actualizar(nuevo_nivel,user)
       #    

        #else:                    #Si no existe nada
         #   print("no hay registro")
       # mycursor.reset()
    

