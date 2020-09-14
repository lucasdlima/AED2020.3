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
