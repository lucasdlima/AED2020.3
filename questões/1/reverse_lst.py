from AED.classes.listaligada import ListaLigada

lst = ListaLigada()
for x in range(5):
    lst.append(x)

print("Lista: ", lst)
# Lista pronta para testar a função.

def reverse_lst(lst):
    tam = int(lst._tam)
    aux = tam - 1
    meio = tam // 2
    for i in range(meio):
        derradeiro = lst[aux]
        lst[aux] = lst[i]
        lst[i] = derradeiro
        aux -= 1
    return lst

print("Lista invertida: ", reverse_lst(lst))

'''
l = ListaLigada()
print("\tInsira os elementos da Lista simples encadeada pressionando enter para confimar a inserção de cada elemnto.\n")
print("---Insira 'n' para concluir!---\n")
aux = 1
while True:
    elem = str(input("Insira o {}° elemento: ".format(aux)))
    if elem == 'n':
        break
    l.append(elem)
    aux += 1

print("\nLista simples encadeada: ", l)
print("Lista invertida: ", reverse_lst(l))

x = input("\nx>>>")
'''
# Interface para escolher os elementos da lista.
