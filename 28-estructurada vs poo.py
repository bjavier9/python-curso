cliente = [{'nombre':'javier', 'apellido':'batista'},
           {'nombre':'antonio', 'apellido':'ramiro'} ]

def mostrar_cliente(cliente,ape):
    for c in cliente:
        if(ape == c['apellido']):
            print('{} {}'.format(c['nombre'], c['apellido']))
            return
    print('cliente no encontrado')

mostrar_cliente(cliente, 'batista')

def borrar_cliente(cliente,ape):
    for i, c in enumerate(cliente):
        if(ape == c['apellido']):
            del(cliente[i])
            print(str(c),"> Borrado")
            return
    print('cliente no encontrado')

borrar_cliente(cliente,'batista')

print(cliente)

### No intentes entender este código, sólo fíjate en cómo se utiliza abajo  

# Creo una estructura para los clientes
class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaré ambas estructuras 

# Creo un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)