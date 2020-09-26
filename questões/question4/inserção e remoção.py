from AED.classes.listaligada import ListaLigada
l = ListaLigada()
for x in range(5):
    l.append(x+1)

print('Lista: ', l)
print(l.busca_insercao(3, 9, 'a'))
print('Inserção do n° na posição anterior ao n° 3: ', l)
print(l.busca_remocao(9))
print('Remoão do valor 9: ', l)