from AED.questões.question9.classes import *
l = ListaLigada()
for x in range(6):
    l.append(x+1)
print('Lista simples encadeada:', l, '\n' + '-' * 43)

a = ListaDupl()
a.dup_cirulcar(l)
print("Lista duplamente encadeada circular:")
ponteiro = a.inicio
i = 1
for w in range(len(l)-1):
    print('{}°\nDado: {}'.format(i, ponteiro.data))
    print('Anterior: {}'.format(ponteiro.ant.data))
    print('Sucessor: {}\n'.format(ponteiro.next.data))
    ponteiro = ponteiro.next
    i += 1
print('Fim\nDado: {}\nAnterior: {}\nSucessor: {}'.format(a.fim.data, a.fim.ant.data, a.fim.next.data))