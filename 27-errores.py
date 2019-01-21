# l = [1,2,3,4,5]

# if len(l)>0:
#     l.pop()
# else:
#     print(vacio)
# Exception
while(True):
    try:
        n = float(input("introduce un numero: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except TypeError:
        print('No se puede dividir el numero por una letra.')
    except ValueError:
        print('Debes introducir un numero.')
    except ZeroDivisionError:
        print('no se puede dividir por cero.')
    except Exception as e:
        print("ha ocurrido un error ", type(e).__name__)
    else:
        print('todo funciono correctamente')
        break
    finally:
        print('Fin de iteración')