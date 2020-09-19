from AED.classes.listaligada import ListaLigada

lst = ListaLigada()
lst.append(1)
lst.append(7)
print(lst)


# Lista pronta para testar a função

def double(lst):
    pos = 0
    for i in range(len(lst)):
        lst.insert(pos, lst[pos])
        pos += 2
    return lst


print(double(lst))

'''
l = ListaLigada()
print(
    "\tInsira os elementos.\n")
print("---Insira 'n' para concluir!---\n")
aux = 1
while True:
    elem = str(input("{}° elemento: ".format(aux)))
    if elem == 'n':
        break
    l.append(elem)
    aux += 1

print("\nLista simples encadeada: ", l)
print("Nova lista: ", double(l))

x = input("\nx>>>")
'''
# Interface para escolher os elementos da lista.
