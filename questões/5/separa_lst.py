from AED.classes.listaligada import ListaLigada

l = ListaLigada()
for x in range(6):
    l.append(x)

def separa_listas(lst):
    impares = ListaLigada()
    pares = ListaLigada()
    ponteiro_pares = lst.pares
    if ponteiro_pares:
        while ponteiro_pares:
            pares.append(ponteiro_pares.data)
            ponteiro_pares = ponteiro_pares.next

    ponteiro_impares = lst.impares
    if ponteiro_impares:
        while ponteiro_impares:
            impares.append(ponteiro_impares.data)
            ponteiro_impares = ponteiro_impares.next
    print('\nLista: ', lst)
    print('Impares: ', impares)
    print('Pares: ', pares)

separa_listas(l)