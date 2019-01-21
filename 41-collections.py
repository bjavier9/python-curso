from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
l = [1,2,3,4,5,5,6,7,8,9]
print(Counter(l))

p = "palabra"
print(Counter(p))

animales = "gato perro perro perro caballo nani canario"
animales2 = animales.split()
animales2=Counter(animales2)
print(Counter(animales2))

print(animales2.most_common(1))
l=[1,2,3,4,5,6,2,4,6,7,3]
c = Counter(l)
print(c.items())
print(c.keys())
print(c.values())
print(sum(c.values()))
print(list(c))
print(dict(c))
print(set(c))

d = defaultdict(float)
d['algo']
print(d)
d = defaultdict(str)
print(d)
d = defaultdict(object)
d['algo']
print(d)
d = defaultdict(int)

d['algo']= 10.5
print(d['algo'])
n = {}
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)
n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'
print(n1==n2)

t = (20,40,60)
persona = namedtuple('Persona','nombre apellido edad')
p = persona(nombre="Hector", apellido="da costa",edad="94")
print(p.nombre)
print(p.apellido)
print(p.edad)
print(p)
print(p[0])
print(p[1])
print(p[2])