from AED.questões.question9.classes import *


def encad_circular(list):
    if list:
        ponteiro = list.inicio
        while ponteiro:
            if not ponteiro.next:
                list.fim = Node(ponteiro.data)
                list.fim.next = list.inicio
            ponteiro = ponteiro.next
    return list


l = ListaLigada()
for x in range(3):
    l.append(x + 1)

print('Lista simples encadeada: {}'.format(l))
b = encad_circular(l)
print("\nLista simpes encadeada circular:\nProximo do fim: {}".format(b.fim.next.data))


a = ListaDupl()
a.dup_cirulcar(l)
print("\nLista duplo encadeada circular:\nAnterior do primeiro elemento: {}\nSucessor do fim: {}".format(a.inicio.ant.data, a.fim.next.data))
