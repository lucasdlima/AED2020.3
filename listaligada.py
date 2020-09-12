from node import Node
class ListaLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tam = 0

    def append(self, valor):
        novo = Node(valor)
        if self.inicio:
            self.fim.next = novo
            self.fim = novo

        else:
            self.inicio = self.fim = novo
        self._tam += 1

    def __len__(self):
        return self._tam

    def __str__(self):
        ponteiro = self.inicio
        ret = ""
        while ponteiro:
            ret = ret + str(ponteiro.data) + ", "
            ponteiro = ponteiro.next
        return "[" + ret[0:-2] + "]"

    def __getitem__(self, index):
        ponteiro = self.inicio
        if index == -1:
            return self.fim.data
        elif index < 0:
            raise IndexError("Azedou aqui na __getitem__")
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("Azedou aqui na __getitem__")
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError("Azedou aqui na __getitem__")

    def __setitem__(self, index, value):
        ponteiro = self.inicio
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("Azedou aqui na __setitem__")
        if ponteiro:
            ponteiro.data = value
        else:
            raise IndexError("Azedou aqui na __setitem__")


'''def reverse_lst(lst):          #A Lista deve ter a função __setitem__ troca de elementos
    tam = int(lst._tam)        #tamanho da lista
    aux = tam - 1              #ultimo indice da lista
    meio = tam//2              #meio da lista
    for i in range(meio):      #usando o meio da lista, pois é igual ao n° de trocas necessarias
        derradeiro = lst[aux]
        lst[aux] = lst[i]      #ultimo indice da lista recebe o primeiro
        lst[i] = derradeiro    #e o primeiro recebe o ultimo, assim a troca é feita.
        aux -= 1               #agora com o penultimo até chegar ao meio.
    return lst                 #lista invetida, sogra desce!!
'''