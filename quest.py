from listaligada import ListaLigada
#1
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


