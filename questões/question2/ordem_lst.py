from AED.classes.listaligada import ListaLigada

l = ListaLigada()
l2 = ListaLigada()
l3 = ListaLigada()
i = 4
for x in range(5):
    l.append(x)
    l2.append(i)
    l3.append(x)
    l3.append(i)
    i -= 1


# lsitas prontas para testar a função


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
        print("ordem crescente!")
    if decrescente:
        print("ordem decrescente!")
    if crescente == decrescente:
        print("fora de ordem!")


print(l)
ordem(l)
print(l2)
ordem(l2)
print(l3)
ordem(l3)

'''
lst = ListaLigada()
print(
    "\tInsira os elementos (apenas números) da Lista simples encadeada pressionando enter para confimar a "
    "inserção de cada elemnto.\n")
print("---Insira 'n' para concluir!---\n")
aux = 1
while True:
    elem = str(input("Insira o {}° elemento: ".format(aux)))
    if elem == 'n':
        break
    lst.append(elem)
    aux += 1

print("\nLista simples encadeada: ", lst)
ordem(lst)

x = input("\nx>>>")
'''
# interface para escolher os elementos da lista.
