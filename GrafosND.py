
import math

class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = []
    
    def esta_en_vertices(self,v):
        if self.vertices.count(v) == 0:
            return False
        else:
            return True
    
    def agregar_vertices(self,v):
        if self.esta_en_vertices(v):
            return False
        else:
            self.vertices.append(v)

        filas = columnas = len(self.matriz)
        matriz_aux = [[None]*(filas+1) for i in range(columnas+1)]

        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]
        self.matriz = matriz_aux
        return True
    
    def agregar_arista(self, inicio, fin, valor, dirigida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor

        if not dirigida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        return True

    def imprimir_matriz(self, n):
        cadena = "\n"
        for c in range(len(n)):
            cadena += "\t" + str(self.vertices[c])
        
        cadena += "\n" + ("       " * len(n))

        for f in range(len(n)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(n)):
                if f == c:
                    cadena += "\t" + "X"
                else:
                    if n[f][c] is None:
                        cadena += "\t" + "0"    
                    else:
                        cadena += "\t" + str(n[f][c])
        cadena += "\n"
        print(cadena)
if __name__ == "__main__":
    g = Grafo()

    g.agregar_vertices("FLOR")
    g.agregar_vertices("MONT")
    g.agregar_vertices("MOR")
    g.agregar_vertices("PAU")
    g.agregar_vertices("CART")
    g.agregar_vertices("BEL")
    g.agregar_vertices("SAJ")
    
    g.agregar_arista("FLOR", "MONT", 38.6, True)
    g.agregar_arista("FLOR", "MOR", 25.4, True)
    g.agregar_arista("MOR", "FLOR", 25.4, True)
    g.agregar_arista("MONT", "PAU", 19.5, True)
    g.agregar_arista("CART", "PAU", 60.4, True)
    g.agregar_arista("MONT", "FLOR", 38.6, True)
    g.agregar_arista("PAU", "MONT", 19.5, True)
    g.agregar_arista("PAU", "CART", 60.4, True)
    g.agregar_arista("BEL", "MOR", 20.4, True)
    g.agregar_arista("MOR", "BEL", 20.4, True)
    g.agregar_arista("SAJ", "BEL", 17.6, True)
    #g.agregar_arista("BEL", "SAJ", 17.6, True)

    g.imprimir_matriz(g.matriz)
