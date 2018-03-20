# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 30/11/2017
# Compiladores - Ciência Da Computação
# PyGraph.py
# -----------------------------------------------------------------------------
import sys

class PyVertice:
    def __init__(self, name, valor=0.0):
        self.name = name
        self.valor = valor

    def __str__(self):
        return str(self.name)

class PyGraph:
    def __init__(self, digrafo=0):
        self.digrafo = digrafo
        self.grafo = []
        self.adj = []

    def inserirNo(self, vertice, vertice2 = None):
        #caso venha somente um nó (ele não se liga a nenhum outro)
        if(vertice not in self.grafo):
            if(vertice2 == None):
                self.grafo.append(vertice)
                self.adj.append([vertice,[]])
            else:
                self.grafo.append(vertice)
                self.adj.append([vertice,[]])
                self.grafo.append(vertice2)
                self.adj.append([vertice2,[]])

                #insere a aresta entre os nós
                #self.adj[0][1].append(vertice)
                self.inserirAdj(vertice,vertice2)


    def inserirAdj(self, vertice, vertice2):
        index = self.grafo.index(vertice)
        self.adj[index][1].append(vertice2)

        if self.digrafo == 0:
            index2 = self.grafo.index(vertice2)
            self.adj[index2][1].append(vertice)


if __name__ == '__main__':
    PyGraph = PyGraph()

    vertice = PyVertice("vertice", 4)
    vertice2 = PyVertice("vertice2")
    PyGraph.inserirNo(vertice, vertice2)

    vertice3 = PyVertice("vertice3")
    PyGraph.inserirNo(vertice3)
    PyGraph.inserirAdj(vertice, vertice3)

    ##print de debugs
    print("Grafo: "+str(len(PyGraph.grafo))+":")
    for vertice in PyGraph.grafo:
        print(PyGraph.grafo.index(vertice))
        print(vertice)

    print("\nAdjacencia "+str(len(PyGraph.adj))+":")
    for vertice in PyGraph.adj:
        print(PyGraph.adj.index(vertice))
        #print(vertice)
        print(vertice[0])
        for vertice2 in vertice[1]:
            print(vertice2)
