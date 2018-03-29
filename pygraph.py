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
        self.tempo = 0
        self.digrafo = digrafo
        self.grafo = []
        self.vetorDistancia = []
        self.adj = []

   #função para inserir dois nos e suas arestas ou uma aresta somente
    def inserirNo(self, vertice):
        #caso venha somente um nó (ele não se liga a nenhum outro)
        if(1 if self.verificaNomeVertice(vertice) == None else 0):
            self.grafo.append(vertice)
            self.adj.append([vertice,[]])


    def achaNomePos(self, vertice):
        aux = -1
        for vert in self.grafo:
            if(vert.name == vertice.name):
                aux = self.grafo.index(vert)
        return aux

    #verifica se existe um vertice com o nome ja no grafo
    def verificaNomeVertice(self, vertice):
        aux = None
        for vert in self.grafo:
            if(vert.name == vertice.name):
                aux = vert
        return aux

    #função para inserir uma nova aresta
    def inserirAdj(self, vertice, vertice2):
        vertice = self.verificaNomeVertice(vertice)
        vertice2 = self.verificaNomeVertice(vertice2)
        index = self.grafo.index(vertice)
        self.adj[index][1].append(vertice2)

        if self.digrafo == 0:
            index2 = self.grafo.index(vertice2)
            self.adj[index2][1].append(vertice)


    def limpaGrafo(self):
        self.grafo = []
        self.vetorDistancia = []
        self.adj = []

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


    def buscaLargura(self, vertInicial):
        self.tempo = 0
        self.vetorDistancia = []

        #coloca os tempos como infinitos
        for i in self.grafo:
            self.vetorDistancia.append(-1)

        for vertice in self.grafo:
            if(vertice != vertInicial):
                vertice.cor = "branco"
                vertice.predecessor = -1

        index = self.grafo.index(vertInicial)
        self.grafo[index].cor = "cinza"
        self.grafo[index].tempDescoberta = self.tempo
        self.grafo[index].predecessor = -1
        self.vetorDistancia[index] = self.tempo

        filaVisitacao = []
        filaVisitacao.append(vertInicial)

        while(len(filaVisitacao) != 0):
            vertFila = filaVisitacao.pop()
            index = self.grafo.index(vertFila)
            vertFilaAdj = self.adj[index][1]

            self.tempo = vertFila.tempDescoberta+1
            for vertAdj in vertFilaAdj:
                if(vertAdj.cor == "branco"):
                    vertAdj.cor = "cinza"
                    vertAdj.tempDescoberta = self.tempo
                    index = self.grafo.index(vertAdj)
                    self.vetorDistancia[index] = self.tempo
                    vertAdj.predecessor = vertFila
                    filaVisitacao.append(vertAdj)
            vertFila.cor = "preto"

    #Busca em profundidade
    def buscaProfundidade(self):
        self.tempo = 0

        for vertice in self.grafo:
                vertice.cor = "branco"
                vertice.predecessor = -1

        for vertice in self.grafo:
                if(vertice.cor == "branco"):
                    print("aqui :"+str(vertice))
                    self.buscaProfundidadeVisita(vertice)

    #Busca em prfundidade visita
    def buscaProfundidadeVisita(self,vertice):
        self.tempo +=1
        vertice.tempDescoberta = self.tempo
        vertice.cor = "cinza"
        print("visitando: "+str(vertice)+", tempo: "+str(self.tempo))

        index = self.achaNomePos(vertice)
        print(vertice)
        print(index)
        for vert in self.adj[index][1]:
            vert = self.verificaNomeVertice(vert)
            if(vert.cor == "branco"):
                vert.predecessor = vertice
                self.buscaProfundidadeVisita(vert)

        vertice.cor = "preto"
        self.tempo+=1
        print("finalizado: "+str(vertice)+", tempo: "+str(self.tempo))
        vertice.tempFinalizado = self.tempo

    def printGrafo(self):
        print("\nGrafo: "+PyGraph.getOrdem()+":")
        sys.stdout.write("[")
        for vertice in PyGraph.grafo:
            sys.stdout.write("- "+str(vertice)+" ")
        print("]")

    def printAdjacencia(self):
        print("\nAdjacencia "+PyGraph.getOrdem()+":")
        for vertice in PyGraph.adj:
            sys.stdout.write(str(vertice[0])+" -> ")
            for vertice2 in vertice[1]:
                sys.stdout.write(str(vertice2))
                if(not vertice[1].index(vertice2) == len(vertice[1])-1):
                    sys.stdout.write(" - ")
            print()

    def printVetorDistancia(self):
        sys.stdout.write("[")
        for i in reversed(PyGraph.vetorDistancia) :
            if(i!=0):
                    sys.stdout.write(str(i))
                    sys.stdout.write(" ")
        sys.stdout.write("]\n\n")

    def printTempoDescoberta(self):
        print("\nTempos De Descoberta: "+PyGraph.getOrdem()+":")
        sys.stdout.write("[")
        for vertice in PyGraph.grafo:
            sys.stdout.write("- ("+str(vertice)+")"+str(vertice.tempDescoberta)+","+str(vertice.tempFinalizado)+" ")
        print("]\n")


if __name__ == '__main__':
    PyGraph = PyGraph()

    #inserção
    a = PyVertice("a")
    PyGraph.inserirNo(a)
    b = PyVertice("b")
    PyGraph.inserirNo(b)
    c = PyVertice("c")
    PyGraph.inserirNo(c)
    d = PyVertice("d")
    PyGraph.inserirNo(d)
    e = PyVertice("e")
    PyGraph.inserirNo(e)
    f = PyVertice("f")
    PyGraph.inserirNo(f)
    g = PyVertice("g")
    PyGraph.inserirNo(g)
    h = PyVertice("h")
    PyGraph.inserirNo(h)

    PyGraph.digrafo=1
    #insere adjascencia
    PyGraph.inserirAdj(a,b)
    PyGraph.inserirAdj(a,f)
    PyGraph.inserirAdj(b,g)
    PyGraph.inserirAdj(b,c)
    PyGraph.inserirAdj(b,d)
    PyGraph.inserirAdj(d,e)
    PyGraph.inserirAdj(g,h)

    #remoção
    #PyGraph.removerNo(vertice3)

    #recebe o Ordem
    print("\nOrdem: "+PyGraph.getOrdem())

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

    #buscaLargura
    PyGraph.buscaLargura(PyGraph.grafo[0])

    #buscaProfundidade
    PyGraph.buscaProfundidade()

    print("\nConexo?:"+str(PyGraph.isConexo()))

    #print debugs
    print("\nVetor Distancia:")
    PyGraph.printVetorDistancia()
    PyGraph.printGrafo()
    PyGraph.printAdjacencia()
    PyGraph.printTempoDescoberta()
