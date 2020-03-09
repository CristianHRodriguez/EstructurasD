import math
import xml.etree.ElementTree as ET
doc_xml = ET.parse('direct.xml')
troncales_x = doc_xml.getroot()


class nodos:
    def __init__(self,nomb,lat,lon, num, tipo):
        self.nombre = nomb
        self.lat = lat
        self.lon = lon
        self.num = num
        self.tipo = tipo
        self.ant = None
        self.sig = None

class lista_de:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def agregar(self,nomb,lat,lon, num, tipo):
        nuevo = nodos(nomb,lat,lon, num, tipo)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            self.cola.sig = nuevo
            nuevo.ant = self.cola
            self.cola = nuevo
        self.size += 1

    def mostrar(self):
        item = self.cabeza
        for i in range(self.size):
            print(item.nombre,"#",item.num)
            item = item.sig

    def m_estacion(self,x):
        item = self.cabeza
        for i in range(self.size):
            #print(item.nombre, "#", item.num," x=",x)
            if item.num == x:
                print("Estacion: ",item.nombre)
                print("Tipo: ", item.tipo)
            item = item.sig

    def calcular_d(self,x1,x2):
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

                    #pp = pp + (lat1+lat2)
                    rad = math.pi / 180
                    distancia1 = (lat2 - lat1)
                    distancia2 = (lon2 - lon1)
                    R = 6372.795477598
                    a = (math.sin(rad * distancia1 / 2)) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (math.sin(rad * distancia2 / 2)) ** 2
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

                    #pp = pp + (lat1+lat2)
                    rad = math.pi / 180
                    distancia1 = (lat2 - lat1)
                    distancia2 = (lon2 - lon1)
                    R = 6372.795477598
                    a = (math.sin(rad * distancia1 / 2)) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (math.sin(rad * distancia2 / 2)) ** 2
                    pp = 2 * R * math.asin(math.sqrt(a)) + pp

                i -= 1
                item = item.ant
        print("La distancia entre las estaciones es: ","{0:.2f}".format(pp)," km")

lista = lista_de()

from xml.dom import minidom
doc = minidom.parse('direct.xml')

i = -1
for x in troncales_x:
    for y in x:
        i += 1
        p1 = doc.getElementsByTagName("nombre_e")[i]
        p1 = p1.firstChild.data
        p2 = doc.getElementsByTagName("latitud")[i]
        p2 = p2.firstChild.data
        p3 = doc.getElementsByTagName("longitud")[i]
        p3 = p3.firstChild.data
        p4 = doc.getElementsByTagName("num")[i]
        p4 = p4.firstChild.data
        p5 = doc.getElementsByTagName("tipo")[i]
        p5 = p5.firstChild.data
        lista.agregar(p1,p2,p3,p4,p5)

lista.mostrar()

sol1 = (input("Introdusca el numero de la estacion de origen: "))
lista.m_estacion(sol1)
sol2 = (input("Introdusca el numero de la estacion de destino: "))
lista.m_estacion(sol2)

lista.calcular_d(sol1,sol2)



