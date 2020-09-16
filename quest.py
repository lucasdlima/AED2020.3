from listaligada import ListaLigada
#1 Construa uma função que recebe uma lista encadeada simples e retorne a mesma lista com a sequência de
# encadeamento invertida.

l = ListaLigada()

def reverse_lst(lst):          #A Lista deve ter a função __setitem__ troca de elementos
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
print("\tInsira os elementos da Lista simples encadeada pressionando enter para confimar a inserção de cada elemnto.\n")
print("---Insira 'n' para concluir!---\n")
aux = 1
while True:
    elem = str(input("Insira o {}° elemento: ".format(aux)))
    if elem == 'n':
        break
    l.append(elem)
    aux +=1

print("\nLista simples encadeada: ", l)
print("Lista invertida: ", reverse_lst(l))

x = input("\nx>>>")
'''
#2 Escreva uma função que receba uma lista encadeada de números inteiros e verifique se os intens da lista estão em
# ordem crescente, decrescente ou fora de ordem, imprimindo o resultado da verificação.

def ordem(lst):
    crescente = True
    decrescente = True
    pos1 = 0
    pos2 = 1
    meio = len(lst) - 1
    for x in range(meio):
        if lst[pos1] < lst[pos2]:
            pos1 += 1
            pos2 += 1
        else:
            crescente = False
            break
    pos1 = 0
    pos2 = 1
    for x in range(meio):
        if lst[pos1] > lst[pos2]:
            pos1 += 1
            pos2 += 1
        else:
            decrescente = False
            break
    if crescente:
        return "ordem crescente!"
    if decrescente:
        return "ordem decrescente!"
    if crescente == decrescente:
        return "fora de ordem!"


#3 Implemente uma função que duplica uma lista simplesmente encadeada, criando novos nós smpre ao lado dos já
# existentes. Se a lista era 1,7 vai se tonar 1,1,7,7.

def double(lst):
    pos = 0
    for i in range(len(lst)):
        lst.insert(pos, lst[pos])
        pos += 2
    return lst

#4
''' def busca_insercao(self, valor_pesquisa, valor_inserir, pos):
        if pos not in 'as':
            raise ValueError("Posição invalida.")
        node = valor_inserir
        try:
            valor_pesquisa = self.index(valor_pesquisa)
        except ValueError:
            return False
        if pos == 's':
            self.insert(valor_pesquisa+1, node)
            return True
        else:
            self.insert(valor_pesquisa, node)
            return True

    def busca_remocao(self, valor):
        try:
            self.index(valor)
        except ValueError:
            return False
        if self.inicio == None:                             #Se a lista estiver vazia
            raise ValueError("{} is not in list".format(valor))
        elif valor == self.inicio.data:             #Remover o inicio da lista
            self.inicio = self.inicio.next
            return True
        else:                                       #Remover qualquer elemento que não seja o inicio.
            anterior = self.inicio                  #Começa no inicio.
            ponteiro = self.inicio.next             #Começa no segundo elemento.
            while ponteiro:                         #Enquanto o ponteiro não for vazio.
                if ponteiro.data == valor:          #Se o valor passado for igual ao ponteiro.
                    anterior.next = ponteiro.next   #O anterior se liga com o proximo do ponteiro.
                    ponteiro.next = None            #O proximo do Nó que tá sendo removido recebe vazio para cortar qualquer ligação dele com a lista.
                anterior = ponteiro                 #Anterior avança para o ponteiro.
                ponteiro = ponteiro.next            #Ponteiro avança para o proximo.
            return True'''

#5

