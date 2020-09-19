from node import Node

class ListaLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tam = 0
        self.pares = None
        self.impares = None

    def append(self, valor):
        novo = Node(valor)
        par_e_impar = Node(valor)
        if self.inicio:
            self.fim.next = novo
            self.fim = novo

        else:
            self.inicio = self.fim = novo
        self.app_pi(par_e_impar)
        self._tam += 1

    def __len__(self):
        return self._tam

    def __str__(self):  # print(lista)
        ponteiro = self.inicio
        ret = ""
        while ponteiro:
            ret = ret + str(ponteiro.data) + ", "
            ponteiro = ponteiro.next
        return "[" + ret[0:-2] + "]"

    def _getnode(self, index):  # percorre a lista até o index desejado
        ponteiro = self.inicio
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("List index out of range")
        return ponteiro

    def __getitem__(self, index):  # lista[0]
        ponteiro = self._getnode(index)
        if index == -1:
            return self.fim.data
        elif index < 0:
            raise IndexError("AList index out of range __getitem__")
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError("AList index out of range __getitem__")

    def __setitem__(self, index, value):  # lista[0] = 4
        ponteiro = self._getnode(index)
        if ponteiro:
            ponteiro.data = value
        else:
            raise IndexError("List index out of range __setitem__")

    def index(self, valor):
        ponteiro = self.inicio
        i = 0
        while ponteiro:
            if ponteiro.data == valor:
                return i
            ponteiro = ponteiro.next
            i = i + 1
        raise ValueError("{} is not in list".format(valor))

    def insert(self, index, valor):
        node = Node(valor)  # envolve o valor em um nó
        if index == 0:  # caso queira inserir na cabeça
            node.next = self.inicio  # o proximo desse novo nó será o que era a cabeça
            self.inicio = node  # e a nova cabeça será esse novo nó
        else:
            ponteiro = self._getnode(index - 1)  # percorrer a lista até a prosição anterior da desejada
            node.next = ponteiro.next  # o proximo do novo nó será o que antes era o proximo do elemento que já estava ali
            ponteiro.next = node  # e o proximo do elemento que já estava ali passará a ser o novo nó.
        self._tam += 1

    def busca_insercao(self, valor_pesquisa, valor_inserir, pos):
        if pos not in 'as':
            raise ValueError("Posição invalida.")
        node = valor_inserir
        try:
            valor_pesquisa = self.index(valor_pesquisa)
        except ValueError:
            return False
        if pos == 's':
            self.insert(valor_pesquisa + 1, node)
            return True
        else:
            self.insert(valor_pesquisa, node)
            return True

    def busca_remocao(self, valor):
        try:
            self.index(valor)
        except ValueError:
            return False
        if self.inicio == None:  # Se a lista estiver vazia
            raise ValueError("{} is not in list".format(valor))
        elif valor == self.inicio.data:  # Remover o inicio da lista
            self.inicio = self.inicio.next
            return True
        else:  # Remover qualquer elemento que não seja o inicio.
            anterior = self.inicio  # Começa no inicio.
            ponteiro = self.inicio.next  # Começa no segundo elemento.
            while ponteiro:  # Enquanto o ponteiro não for vazio.
                if ponteiro.data == valor:  # Se o valor passado for igual ao ponteiro.
                    anterior.next = ponteiro.next  # O anterior se liga com o proximo do ponteiro.
                    ponteiro.next = None  # O proximo do Nó que tá sendo removido recebe vazio para cortar qualquer ligação dele com a lista.
                anterior = ponteiro  # Anterior avança para o ponteiro.
                ponteiro = ponteiro.next  # Ponteiro avança para o proximo.
            return True

    def par(self, num):
        if num // 2 == num / 2:
            return True
        else:
            return False

    def app_pi(self, num):
        if self.par(num.data):
            if self.pares:
                ponteiro = self.pares
                while ponteiro.next:
                    ponteiro = ponteiro.next
                ponteiro.next = num
            else:
                self.pares = num
        else:
            if self.impares:
                ponteiro = self.impares
                while ponteiro.next:
                    ponteiro = ponteiro.next
                ponteiro.next = num
            else:
                self.impares = num



