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
'''
print("\n\tSepare os elementos com espaço!\n")
while True:
    elem = str(input("Insira os elementos da lista encadeada simples: "))
    elem.split()

    for i in elem:
        if i != ' ':
            l.append(i)

    print("\nLista encadeada simples: ", l)
    print("Lista invertida: ", reverse_lst(l))

    loop = input("\n\nDeseja continuar? 's' ou 'n'>>>")
    if loop == 'n':
        break
'''
#2






