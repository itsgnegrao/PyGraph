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
        self.cor = "branco"
        self.predecessor = None
        self.tempDescoberta = -1
        self.tempFinalizado = -1

    def __str__(self):
        return str(self.name)

class PyGraph:
    def __init__(self, digrafo=0):
        self.digrafo = digrafo
        self.grafo = []
        self.vetorDistancia = []
        self.adj = []

    #função para inserir dois nos e suas arestas ou uma aresta somente
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

    #função para inserir uma nova aresta
    def inserirAdj(self, vertice, vertice2):
        index = self.grafo.index(vertice)
        self.adj[index][1].append(vertice2)

        if self.digrafo == 0:
            index2 = self.grafo.index(vertice2)
            self.adj[index2][1].append(vertice)

    #função para remover um no e suas arestas
    def removerNo(self,vertice):
        if(vertice in self.grafo):
            index = self.grafo.index(vertice)
            self.grafo.remove(vertice)
            self.adj.pop(index)

            for vert in self.adj:
                for vert2 in vert[1]:
                    if(vert2 == vertice):
                        vert[1].remove(vertice)

    #retorna o grau do Grafo
    def getOrdem(self):
        return str(len(self.grafo))

    #função errada????
    #ou retornar o numero de arestas
    def getVertices(self):
        return self.grafo

    #retorna os nos de um Grafo
    def getNos(self):
        return self.grafo

    #retorna o grau de um no do Grafo bidirecional
    def getGrau(self, no):
        cont = 0
        if(self.digrafo == 0):
            for nos in PyGraph.adj:
                for vertice2 in nos[1]:
                    if(vertice2 == no):
                        cont+=1
        return cont

    #retorna a lista de adjascencia de um nó bidirecional
    def getAdjacentes(self, no):
        return self.adj[self.grafo.index(no)][1]


    #verifica se o grafo é completo bidirecional
    def isCompleto(self):
        cont = 0
        n = len(self.grafo)
        visitados = []

        for nos in self.adj:
            visitados.append(nos[0])
            for no in nos[1]:
                if no not in visitados:
                    cont+=1
                    visitados.append(no)

        return 1 if (n*(n-1))/2 == cont else 0

    #verifica se um grafo é conexo

    def isConexo(self):
        return 1 if (-1 not in self.vetorDistancia) else 0

        ##ARRUMAR

    def buscaLargura(self, vertInicial):
        tempo = 0

        #coloca os tempos como infinitos
        for i in self.grafo:
            self.vetorDistancia.append(-1)

        for vertice in self.grafo:
            if(vertice != vertInicial):
                vertice.cor = "branco"
                vertice.predecessor = -1
        index = self.grafo.index(vertInicial)
        self.grafo[index].cor = "cinza"
        self.grafo[index].tempDescoberta = tempo
        self.grafo[index].predecessor = -1
        self.vetorDistancia[index] = tempo

        filaVisitacao = []
        filaVisitacao.append(vertInicial)

        while(len(filaVisitacao) != 0):
            vertFila = filaVisitacao.pop()
            index = self.grafo.index(vertFila)
            vertFilaAdj = self.adj[index][1]

            tempo = vertFila.tempDescoberta+1
            for vertAdj in vertFilaAdj:
                if(vertAdj.cor == "branco"):
                    vertAdj.cor = "cinza"
                    vertAdj.tempDescoberta = tempo
                    index = self.grafo.index(vertAdj)
                    self.vetorDistancia[index] = tempo
                    vertAdj.predecessor = vertFila
                    filaVisitacao.append(vertAdj)
            vertFila.cor = "preto"


if __name__ == '__main__':
    PyGraph = PyGraph()

    #inserção
    vertice = PyVertice("vertice", 4)
    vertice2 = PyVertice("vertice2")
    PyGraph.inserirNo(vertice, vertice2)

    vertice3 = PyVertice("vertice3")
    PyGraph.inserirNo(vertice3)
    PyGraph.inserirAdj(vertice, PyGraph.grafo[2])


    #remoção
    #PyGraph.removerNo(vertice3)

    #recebe o Ordem
    print("\nOrdem: "+PyGraph.getOrdem())

    #recebe os vertices do Grafo
    print("\nVertices:")
    lists = PyGraph.getVertices()
    for i in lists:
        print(i)

    #recebe os nos do Grafo
    print("\nNos:")
    nos = PyGraph.getNos()
    for i in nos:
        print(i)

    #recebe o grau de um Grafo bidirecional
    print("\nGrau de "+str(PyGraph.grafo[1])+":"+str(PyGraph.getGrau(PyGraph.grafo[1])))

    #recebe a lista de adj de um Grafo
    print("\nADJ de "+str(PyGraph.grafo[1])+":")
    nos = PyGraph.getAdjacentes(PyGraph.grafo[1])
    for i in nos:
        print(i)

    #grafo é completo ou nao
    print("\nCompleto?:"+str(PyGraph.isCompleto()))

    #grafo é completo ou nao
    vertice4 = PyVertice("vertice4")
    PyGraph.inserirNo(vertice4)
    PyGraph.inserirAdj(vertice, vertice4)
    vertice5 = PyVertice("vertice5")
    PyGraph.inserirNo(vertice5)
    PyGraph.inserirAdj(vertice4,vertice5)
    vertice6 = PyVertice("vertice6")
    PyGraph.inserirNo(vertice6)
    #PyGraph.inserirAdj(vertice5,vertice6)
    #PyGraph.inserirAdj(vertice3,vertice6)
    print("\nConexo?:"+str(PyGraph.isConexo()))

    #buscaLargura
    PyGraph.buscaLargura(PyGraph.grafo[0])
    print("\nVetor Distancia:")
    sys.stdout.write("[")
    for i in PyGraph.vetorDistancia:
        sys.stdout.write(str(i))
        sys.stdout.write(" ")
    sys.stdout.write("]\n\n")

    ##print de debugs
    print("\nGrafo: "+PyGraph.getOrdem()+":")
    for vertice in PyGraph.grafo:
        print(PyGraph.grafo.index(vertice))
        print(vertice)

    print("\nAdjacencia "+PyGraph.getOrdem()+":")
    for vertice in PyGraph.adj:
        print(PyGraph.adj.index(vertice))
        #print(vertice)
        print(vertice[0])
        for vertice2 in vertice[1]:
            print(vertice2)
