#3 oportunidades para elegir la opcion correcta
#adivinar la pregunta
from random import randrange


palabras = [{'palabra':'MANZANA','pregunta':['¿Viene de un arbol y es roja?','¿Es el logo de las MacBook?']},
            {'palabra':'ARBOL','pregunta':['¿Tiene hojas y es verde y grande?','¿Tiene muchos frutos y aveces sirve para hacer muebles?']},
            {'palabra':'MUSICA','pregunta':['¿Se puede escuchar por unos audifonos?','¿Las personas bailan cuando la escuchan?']}]
# for palabra in palabras:

def inicial():
    print("Bienvenido a este juego pendejo elije una opcion:")
    print("{:>30}".format("1-adivina la palabra"))
    print("{:>30}".format("2-salir"))
    mando = input( 'Escriba el numero de la opcion: ')
    dime(mando)

def dime(m):
    if m == "2":
        print('C salio joven')
    elif m == "1":
        adiviname()

def adiviname():
    malas = 0
    p=randrange(len(palabras))   
    for i in range(3): 
        n=randrange(2)
        print('oportunidad :',i+1,'/3')
        print(palabras[p]['pregunta'][n])
        q=input()
        q=q.upper()
        
        if q==palabras[p]['palabra']:
            print('correcto')
            inicial()
        else:
            print('incorrecto')
            malas +=1 
    print('malas',malas)

inicial() 



    