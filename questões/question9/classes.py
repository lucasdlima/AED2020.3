from AED.classes.listaligada import *


class NoDupl:
    def __init__(self, data, ant, next):
        self.data = data
        self.ant = ant
        self.next = next


class ListaDupl:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tam = 0

    def dup_cirulcar(self, lst):
        duponteiro = self.inicio = NoDupl(lst.inicio.data, None, lst.inicio.next)
        ponteiro = lst.inicio.next
        while ponteiro.next:
            duponteiro.next = NoDupl(ponteiro.data, duponteiro, ponteiro.next)
            duponteiro = duponteiro.next
            ponteiro = ponteiro.next
            if not ponteiro.next:
                self.fim = NoDupl(ponteiro.data, duponteiro, self.inicio)
        self.inicio.ant = self.fim
        self.tam = len(lst)

    def __len__(self):
        return self.tam

    def __str__(self):  # print(lista)
        ponteiro = self.inicio
        ret = ""
        while ponteiro:
            ret = ret + str(ponteiro.data) + ", "
            ponteiro = ponteiro.next
        return "[" + ret[0:-2] + "]"

    def __getitem__(self, index):  # lista[0]
        ponteiro = self._getnode(index)
        if index == -1:
            return self.fim.data
        elif index < 0:
            raise IndexError("List index out of range __getitem__")
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError("List index out of range __getitem__")

    def _getnode(self, index):  # percorre a lista até o index desejado
        ponteiro = self.inicio
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("List index out of range")
        return ponteiro

    def insert(self, index, valor):
        node = NoDupl(valor, None, None)
        if index == 0:
            node.next = self.inicio
            self.inicio = node
            self.inicio.ant = self.fim
        else:
            anterior = self._getnode(index - 2)
            ponteiro = self._getnode(index - 1)
            node.next = ponteiro.next
            node.ant = anterior
            ponteiro.next = node



