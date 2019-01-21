def cuenta_atras(num):
    num -=1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print('ya bitch')
    print("fin de la funcion",num)

cuenta_atras(5)

def factorial(num):
    if num > 1:
        num = num * factorial(num -1)
    return num

factorial(5)