import json
import math


class nodos:
    def __init__(self, nomb, lat, lon, num, tipo, numt, nombt):
        self.nombre = nomb
        self.lat = lat
        self.lon = lon
        self.num = num
        self.tipo = tipo
        self.numt = numt
        self.nombt = nombt
        self.ant = None
        self.sig = None


class lista_de:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def agregar(self, nomb, lat, lon, num, tipo, numt, nombt):
        nuevo = nodos(nomb, lat, lon, num, tipo, numt, nombt)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            self.cola.sig = nuevo
            nuevo.ant = self.cola
            self.cola = nuevo
        self.size += 1

    def eliminar(self):
        if self.size < 1:
            pass
        else:
            aux = self.cabeza
            aux2 = self.size - 2
            for i in range(aux2):
                aux = aux.sig
            aux.sig = None
            self.size -= 1

    def eliminarE(self, x):
        i = 0
        while i <= (x-1):
            self.eliminar()
            i +=1

    def lista_ListasS(self, orig, dest):  # agrega listas a otra lista
        item = orig.cabeza
        for i in range(orig.size):
            dest.agregar(item.nombre, item.lat, item.lon, item.num, item.tipo, item.numt, item.nombt)
            item = item.sig

    def lista_ListasA(self, x1, x2):  # agregar una lista a otra lista en manera invertida
        item = x1.cola
        for i in range(x1.size):
            x2.agregar(item.nombre, item.lat, item.lon, item.num, item.tipo, item.numt, item.nombt)
            item = item.ant

    def lista_ListasE(self, orig, dest, x):  # agrega un elemento de una lista a otra lista
        item = orig.cabeza
        for i in range(orig.size):
            if item.num == x:
                dest.agregar(item.nombre, item.lat, item.lon, item.num, item.tipo, item.numt, item.nombt)
            item = item.sig

    def mostrarE(self):
        item = self.cabeza
        for i in range(self.size):
            print(item.nombre, "#", item.num)
            item = item.sig

    def mostrarT(self, x):  # MOSTRAR las troncales
        for troncales1 in x['troncales']:
            print(troncales1['nombreT'], " # ", troncales1['n_t'])

    def m_estacion(self, x):  # retorna el nombre de la estacion
        item = self.cabeza
        for i in range(self.size):
            if item.num == x:
                a = item.nombre
            item = item.sig
        return a

    def reasignacion(self):  # le pone nuevos numeros a todas las estaciones en la lista
        item = self.cabeza
        for i in range(self.size):
            item.num = (i + 1)
            item = item.sig

    def ret_numE(self, x):  # retorna el numero de la estacion
        item = self.cabeza
        for i in range(self.size):
            if item.nombre == x:
                a = item.num
            item = item.sig
        return a

    def calcular_d(self, x1, x2):
        pp = 0
        j = (int(x2))
        k = (int(x1))
        if k < j:
            item = self.cabeza
            i = 1
            while i < (j):
                if int(item.num) >= k:
                    lat1 = float(item.lat)
                    lat2 = float(item.sig.lat)
                    lon1 = float(item.lon)
                    lon2 = float(item.sig.lon)

                    # pp = pp + (lat1+lat2)
                    rad = math.pi / 180
                    distancia1 = (lat2 - lat1)
                    distancia2 = (lon2 - lon1)
                    R = 6372.795477598
                    a = (math.sin(rad * distancia1 / 2)) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (
                        math.sin(rad * distancia2 / 2)) ** 2
                    pp = 2 * R * math.asin(math.sqrt(a)) + pp

                i += 1
                item = item.sig
        if k > j:
            item = self.cola
            i = self.size
            while i > (j):
                if int(item.num) <= k:
                    lat1 = float(item.lat)
                    lat2 = float(item.ant.lat)
                    lon1 = float(item.lon)
                    lon2 = float(item.ant.lon)

                    # pp = pp + (lat1+lat2)
                    rad = math.pi / 180
                    distancia1 = (lat2 - lat1)
                    distancia2 = (lon2 - lon1)
                    R = 6372.795477598
                    a = (math.sin(rad * distancia1 / 2)) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (
                        math.sin(rad * distancia2 / 2)) ** 2
                    pp = 2 * R * math.asin(math.sqrt(a)) + pp

                i -= 1
                item = item.ant
        print("La distancia entre las estaciones es: ", "{0:.2f}".format(pp), " km")


# crea una lista para cada troncal y un array con todas las troncales
lista = lista_de()
T_H = lista_de()
T_A = lista_de()
T_B = lista_de()
T_C = lista_de()
T_D = lista_de()
T_E = lista_de()
T_F = lista_de()
T_G = lista_de()
T_J = lista_de()
T_K = lista_de()
T_L = lista_de()
T_M = lista_de()
T_T = lista_de()
T_I = lista_de()
result = lista_de()

T = [T_H, T_A, T_B, T_C, T_D, T_E, T_F, T_G, T_T, T_J, T_K, T_L, T_M, T_I]

print("Lista de troncales y numero asignado\n")
with open('transmi.json') as file:
    data = json.load(file)

    # almacenamiento en una lista gigante todas y cada una de las troncales y sus estaciones
    for troncales in data['troncales']:
        p1 = troncales['nombreT']
        p2 = troncales['n_t']
        for propiedades in troncales['estaciones']:
            p3 = propiedades['nombreE']
            p4 = propiedades['latitud']
            p5 = propiedades['longitud']
            p6 = propiedades['numero']
            p7 = propiedades['tipo']
            lista.agregar(p3, p4, p5, p6, p7, p2, p1)
            pp2 = int(p2) - 1
            T[pp2].agregar(p3, p4, p5, p6, p7, p2, p1)

lista.reasignacion()

#tablas hash
#Creemos una tabla hash vacia con capacidad para almacenar 10 elementos


def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

#Buscar datos en la tabla
def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        #print(i,k,v,kv)
        if key == k:
            return v

cont_upz = 0
with open('upz local.json') as file:
    upz = json.load(file)

    for upz_b in upz['localidades']:
        for upz_z in upz_b['NUPZ']:
            cont_upz += 1

    hash_table = [[] for _ in range(cont_upz)]
    for upz_c in upz['localidades']:
        for upz_zo in upz_c['NUPZ']:
            upz_n = upz_zo['UPZ']
            upz_l = upz_zo['NUPZ']
            insert(hash_table, upz_n, upz_l)

#print(hash_table)
#zz = search(hash_table,116)
#print(zz)
#fin del hash

# determinar desde donde y hasta donde
T[0].mostrarT(data)
print("\n")
T1 = (input("Introdusca el numero de la Troncal de ORIGEN: "))
T11 = (int(T1) - 1)
print("\n")
T[(T11)].mostrarE()
print("\n")
E1 = (input("Introdusca el numero de la estacion de ORIGEN: "))
print("\nLa estacion de origen es ")
A1 = T[T11].m_estacion(int(E1))
print(A1, "\n")
T[0].mostrarT(data)
print("\n")
T2 = (input("Introdusca el numero de la Troncal de DESTINO: "))
T12 = (int(T2) - 1)
print("\n")
T[(T12)].mostrarE()
print("\n")
E2 = (input("Introdusca el numero de la estacion de DESTINO: "))
print("\nLa estacion de destino es ")
A2 = T[T12].m_estacion(int(E2))
print(A2)

# todas las opciones posibles para llenar la nueva lista
O = T11
D = T12
R = 0

if (O == D):
    result.lista_ListasS(T[T11], result)
    R = 2
while(R < 1):
    if (D < O):
        O, D = D, O
    elif (O == 0):
        if (D == 1): # H -> A
            result.lista_ListasS(T[D], result)
            result.lista_ListasS(T[O], result)
            break;
        elif (D == 2): #H -> B
            result.lista_ListasS(T[D], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[O], result)
            break;
        elif (D == 3): #H -> C
            result.lista_ListasS(T[D], result)
            result.lista_ListasE(lista, result, 71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[O], result)
            break;
        elif (D == 4): #H -> D
            result.lista_ListasS(T[D], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[O], result)
            break;
        elif (D == 5): #H -> E
            result.lista_ListasS(T[D], result)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 6:  #H -> F
            result.lista_ListasA(T[D], result)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasE(lista, result, 27)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 7:  #H -> G
            result.lista_ListasA(T[D], result)
            result.lista_ListasE(lista, result, 82)
            result.lista_ListasE(lista, result, 83)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 8:  # H -> T
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 9:  # H -> J
            result.lista_ListasA(T[D], result)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasE(lista, result, 27)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 10:  # H -> K
            result.lista_ListasA(T[D], result)
            result.lista_ListasE(lista, result, 24)
            result.lista_ListasE(lista, result, 25)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasE(lista, result, 27)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 11:  # H -> L
            result.lista_ListasA(T[D], result)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 12:  # H -> M
            result.lista_ListasS(T[D], result)
            result.lista_ListasS(T[11], result)
            #result.eliminarE(1)
            result.lista_ListasS(T[O], result)
            break;
    elif(O == 1):
        if D == 2:   # A -> B
            result.lista_ListasS(T[D], result)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 3:  # A -> C
            result.lista_ListasS(T[D], result)
            result.lista_ListasE(lista, result, 71)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 4:  # A -> D
            result.lista_ListasS(T[D], result)
            result.lista_ListasS(T[O], result)
            break;
        elif D == 5:  # A -> E
            result.lista_ListasS(T[D], result)
            result.lista_ListasA(T[O], result)
            break;
        elif D == 6:  # A -> F
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 7:  # A -> G
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result, 83)
            result.lista_ListasE(lista, result, 82)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 8:  # A -> T
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[0], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 9:  # A -> J
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==10:
            result.lista_ListasS(T[1],result)
            result.lista_ListasS(T[10], result)
            break;
        elif D==11:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;


    elif (O == 2):
        if D == 3:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,71)
            result.lista_ListasA(T[D], result)
            break;
        elif D==4:
            result.lista_ListasS(T[O], result)
            result.lista_ListasA(T[D], result)
            break;
        elif D == 5:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==6:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==7:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[5], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 8:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[1],result)
            result.lista_ListasS(T[0], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==9:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasE(lista, result,136)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 10:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 11:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 12:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;


    elif (O == 3):
        if D==4:
             result.lista_ListasS(T[O], result)
             result.lista_ListasA(T[D], result)
             break;
        elif D==5:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 6:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[5], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==7:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[5], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 8:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[0], result)
            result.lista_ListasS(T[D], result)
            break;

        elif D==9:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==10:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[5], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==11:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==12:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasE(lista, result,135)
            result.lista_ListasE(lista, result,134)
            result.lista_ListasS(T[D], result)
            break;


    elif (O == 4):
        if D == 5:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D== 6:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[5], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==7:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[5], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 8:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(result, result,71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[0], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 9:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(result, result,71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==10:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[5], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 11:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,71)
            result.lista_ListasS(T[1], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 12:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[1], result)
            result.lista_ListasE(lista, result,135)
            result.lista_ListasE(lista, result,134)
            result.lista_ListasS(T[D], result)
            break;

    elif (O == 5):
        if D==6:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==7:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 8:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[0], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==9:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,137)
            result.lista_ListasE(lista,result,136)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 10:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 11:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 12:
            result.lista_ListasS(T[O], result)
            result.lista_ListasE(lista, result,137)
            result.lista_ListasE(lista, result,136)
            result.lista_ListasE(lista, result,135)
            result.lista_ListasE(lista, result,134)
            result.lista_ListasS(T[D], result)
            break;
    elif (O == 6):
        if D==7:
            result.lista_ListasA(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==8:
            result.lista_ListasA(T[O], result)
            result.lista_ListasS(T[0], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==9:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasS(T[D], result)
            break;
        elif D==10:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasE(lista, result, 25)
            result.lista_ListasE(lista, result, 24)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 11:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 12:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result,26)
            result.lista_ListasE(lista, result,137)
            result.lista_ListasE(lista, result,135)
            result.lista_ListasE(lista, result,134)
            result.lista_ListasS(T[D], result)
            break;
    elif (O == 7):
        if D==8:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result,82)
            result.lista_ListasE(lista, result,83)
            result.lista_ListasS(T[0], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==9:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result, 86)
            result.lista_ListasE(lista,result,85)
            result.lista_ListasE(lista, result,84)
            result.lista_ListasE(lista, result,26)
            result.lista_ListasE(lista, result,136)
            result.lista_ListasS(T[D], result)
            break;
        elif D==10:
            result.lista_ListasS(lista, result)
            result.lista_ListasE(lista, result,86)
            result.lista_ListasE(lista, result,81)
            result.lista_ListasE(lista, result,80)
            result.lista_ListasS(T[D], result)
            break;
        elif D==11:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result, 86)
            result.lista_ListasE(lista, result, 85)
            result.lista_ListasE(lista, result, 84)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasS(T[D], result)
            break;
        elif D==12:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result, 86)
            result.lista_ListasE(lista, result, 85)
            result.lista_ListasE(lista, result, 84)
            result.lista_ListasE(lista, result, 26)
            result.lista_ListasE(lista, result, 135)
            result.lista_ListasE(lista, result, 134)
            result.lista_ListasS(T[D], result)
            break;
    elif (O == 8):
        if D==9:
            result.lista_ListasA(T[O], result)
            result.lista_ListasA(T[0], result)
            result.lista_ListasE(lista, result,26)
            result.lista_ListasE(lista, result,136)
            result.lista_ListasS(T[D], result)
            break;
        elif D==10:
            result.lista_ListasA(T[O], result)
            result.lista_ListasE(lista, result,27)
            result.lista_ListasE(lista, result,26)
            result.lista_ListasE(lista, result,25)
            result.lista_ListasE(lista,result,24)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 11:
            result.lista_ListasA(T[O], result)
            result.lista_ListasA(T[0], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 12:
            result.lista_ListasA(T[O], result)
            result.lista_ListasA(T[0], result)
            result.lista_ListasE(lista, result,137)
            result.lista_ListasE(lista, result,136)
            result.lista_ListasE(lista, result,135)
            result.lista_ListasE(lista, result,134)
            result.lista_ListasS(T[D], result)
            break;

    elif (O == 9):
        if D==10:
            result.lista_ListasS(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D==11:
            result.lista_ListasA(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        elif D == 12:
             result.lista_ListasS(T[O], result)
             result.lista_ListasE(lista, result,120)
             result.lista_ListasS(T[D], result)
             break;

    elif (O == 10):
        if D == 11:
            result.lista_ListasA(T[O], result)
            result.lista_ListasS(T[D], result)
            break;
        if D == 12:
             result.lista_ListasA(T[O], result)
             result.lista_ListasS(T[D], result)
             break;

    elif (O == 11):
        if D == 12:
            result.lista_ListasA(T[O], result)
            result.lista_ListasS(T[D], result)
            break;


    elif (O == 12):
        print("h")


result.reasignacion()
sol1 = result.ret_numE(A1)
sol2 = result.ret_numE(A2)
result.calcular_d(sol1, sol2)


