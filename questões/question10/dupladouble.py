from AED.questões.question9.classes import ListaDupl
from AED.classes.listaligada import ListaLigada
from AED.questões.question3.double_lst import double

l = ListaLigada()
for x in range(3):
    l.append(x)
print(l, '\n' + '-' * 18)

a = ListaDupl()
a.dup_cirulcar(l)
print(a)
double(a)
print(a)
