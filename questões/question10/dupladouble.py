from AED.questões.question9.classes import ListaDupl
from AED.classes.listaligada import ListaLigada


def double(lst):
    pos = 0
    for i in range(len(lst)):
        lst.insert(pos, lst[pos])
        pos += 2
    return lst


l = ListaLigada()
for x in range(3):
    l.append(x)
print(l, '\n' + '-' * 18)

a = ListaDupl()
a.dup_cirulcar(l)
print(a)
double(a)
print(a)
