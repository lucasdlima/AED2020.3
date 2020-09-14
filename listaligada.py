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

    def __str__(self): #print(lista)
        ponteiro = self.inicio
        ret = ""
        while ponteiro:
            ret = ret + str(ponteiro.data) + ", "
            ponteiro = ponteiro.next
        return "[" + ret[0:-2] + "]"

    def _getnode(self, index): #percorre a lista até o index desejado
        ponteiro = self.inicio
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("List index out of range")
        return ponteiro

    def __getitem__(self, index): #lista[0]
        ponteiro = self._getnode(index)
        if index == -1:
            return self.fim.data
        elif index < 0:
            raise IndexError("AList index out of range __getitem__")
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError("AList index out of range __getitem__")

    def __setitem__(self, index, value): #lista[0] = 4
        ponteiro = self._getnode(index)
        if ponteiro:
            ponteiro.data = value
        else:
            raise IndexError("List index out of range __setitem__")

    def insert(self, index, valor):
        node = Node(valor)                          #envolve o valor em um nó
        if index == 0:                              #caso queira inserir na cabeça
            node.next = self.inicio                 #o proximo desse novo nó será o que era a cabeça
            self.inicio = node                      #e a nova cabeça será esse novo nó
        else:
            ponteiro = self._getnode(index-1)       #percorrer a lista até a prosição anterior da desejada
            node.next = ponteiro.next               #o proximo do novo nó será o que antes era o proximo do elemento que já estava ali
            ponteiro.next = node                    #e o proximo do elemento que já estava ali passará a ser o novo nó.
        self._tam += 1


