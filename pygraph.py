# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 30/11/2017
# Compiladores - Ciência Da Computação
# PyGraph.py
# -----------------------------------------------------------------------------

import sys

class PyVertice:
    def __init__(self, name="vertice", valor=0.0):
        self.name = name
        self.valor = valor

    def __str__(self):
        return str(self.name)

class PyGraph:
    def __init__(self, digrafo=0):
        self.digrafo = digrafo
        self.grafo = []
        self.adj = []
        vertice = PyVertice()
        self.grafo.append(vertice)
        self.adj.append(vertice)

    def inserirNo(self, vertice):
        self.grafo.append(vertice)
        self.adj.append(vertice)

    def inserirAdj(self,vertice, vertice2):
        pass



if __name__ == '__main__':
    PyGraph = PyGraph()
    #PyGraph.inserir(-1,PyVertice(name="batata"))
    #PyGraph.inserir(-1,PyVertice(name="batata2"))
    PyGraph.inserirNo(PyVertice("vertice2", 4))
    #   PyGraph.inserirNo(PyVertice("vertice3", 5))

    print("Grafo: "+str(len(PyGraph.grafo))+":")
    for vertice in PyGraph.grafo:
        print(PyGraph.grafo.index(vertice))
        print(vertice)

    print("\nAdjacencia "+str(len(PyGraph.adj))+":")
    for vertice in PyGraph.adj:
        index = PyGraph.adj.index(vertice)
        print(index)
        print(PyGraph.adj[index])

    #for vertice in PyGraph.adj:
    #    print(PyGraph.adj.index(vertice))
    #    for vertice2 in vertice:
    #        print(vertice2)
