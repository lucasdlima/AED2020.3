from AED.classes.listaligada import ListaLigada


class Garcon:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.mesas_atendidas = 0
        self.salario = 1045.00

    def __str__(self):
        p = "Id: {}\nNome: {}\nSalario: R${}".format(self.id, self.nome, self.salario)
        return p


class Mesa:
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
        self.ten = valor * 0.1

    def __str__(self):  # print(lista)
        p = "id: {}; Ganhos: {} ".format(self.id, self.ten)
        return p


class Bonna_massa:
    def __init__(self):
        self.garcons = ListaLigada()
        self.mesas = ListaLigada()

    def cadastrar_garcon(self, nome):
        id = len(self.garcons) + 1
        self.garcons.append(Garcon(id, nome))

    def __str__(self):
        ponteiro = self.garcons.inicio
        repr = "-\n"
        while ponteiro:
            repr = repr + str(ponteiro.data) + '\n' + '-' + '\n'
            ponteiro = ponteiro.next
        return repr

    def registar_mesa(self, id, valor):
        self.mesas.append(Mesa(id, valor))
        self.garcons[id - 1].mesas_atendidas += 1

    def calcular_salario(self, id):
        ponteirom = self.mesas.inicio
        idex = self.garcons[self.index(id)].id
        while ponteirom:
            if idex == ponteirom.data.id:
                self.garcons[self.index(id)].salario = self.garcons[self.index(id)].salario + ponteirom.data.ten
            ponteirom = ponteirom.next
        return print('Salário + ganhos do Garçon {}: R$ {}'.format(self.garcons[self.index(id)].nome,
                                                                   self.garcons[self.index(id)].salario))

    def index(self, id):
        i = 0
        ponteiro = self.garcons.inicio
        while ponteiro:
            if id == ponteiro.data.id or id == ponteiro.data.nome:
                return i
            else:
                ponteiro = ponteiro.next
                i += 1

    def relatorio(self):
        pprint = self.garcons.inicio
        p = '-' * 21 + '\nRelatório de ganhos:\n' + '-' * 21 + '\n'
        while pprint:
            p = p + 'Nome: ' + str(pprint.data.nome) + '\n' + 'Ganhos: R$ ' + str(
                pprint.data.salario - 1045) + '\n' + '-' + '\n'
            pprint = pprint.next
        return print(p)


testar = Bonna_massa()
testar.cadastrar_garcon('Lucas')  # Função cadastrar Garçon, recebe o Nome do garçom, o Id é dado pela ordem
testar.cadastrar_garcon('Bruno')
testar.cadastrar_garcon('Rodolfo')

testar.registar_mesa(1, 900) # Função registar mesa, recebe o Id do garçom e o valor pago pela comanda
testar.registar_mesa(1, 1500)
testar.registar_mesa(1, 350)
testar.registar_mesa(2, 750)
testar.registar_mesa(2, 3000)
testar.registar_mesa(3, 1750)
testar.registar_mesa(3, 2350)

testar.calcular_salario(1)  # Função calcular salário, recebe o Id (int) ou o nome do garçom ('str')
testar.calcular_salario('Bruno') # e retorna o salário + os ganhos
testar.calcular_salario(3)

testar.relatorio() # Função relatório, recebe apenas o proprio objeto e imprime nome e ganhos de todos os garçons
