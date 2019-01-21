def indeterminado_p(*args):
    # print(args)
    for arg in args:
        print(arg)

indeterminado_p(5,"holA",'q mas','jajaja',14)

def indeterminado_nombre(**kwargs):
    # print(kwargs)
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])

indeterminado_nombre(n=4, c="hola",l=[1,2,3,4,5,6,7,8])

def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("sumatoria indeterminado es", t)
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])

super_funcion(10,50,-1,1,56,nombre="hector",edad=28)