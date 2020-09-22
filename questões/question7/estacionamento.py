from AED.classes.listaligada import ListaLigada
from AED.questões.question1.reverse_lst import reverse_lst


class Carro:
    def __init__(self, placa, cliente, modelo):
        self.placa_carro = placa
        self.nome_cliente = cliente
        self.marca_modelo = modelo

    def __str__(self):
        p = 'Um {} de placa {} pertecente ao Sr(a) {}.'.format(self.marca_modelo, self.placa_carro, self.nome_cliente)
        return p


class EstacionamentoUAST:
    def __init__(self):
        self.parking1 = ListaLigada()
        self.parking2 = ListaLigada()

    def estacionar(self):
        if len(self.parking1) < 10:
            placa = input("Placa: ")
            cliente = input("Nome cliente: ")
            modelo = input("Modelo do veículo: ")
            self.parking1.append(Carro(placa, cliente, modelo))
            return print("Ok!")
        else:
            return print("Não há vagas.")

    def devolver(self):
        placa = input("Placa: ")
        if self.getplaca(placa):
            temp = len(self.parking1) - self.getindex(placa)
            for i in range(temp-1):
                movidos = self.parking1.pop()
                self.parking2.append(movidos)
            self.parking1.pop()
            if self.parking2.inicio:
                ponteiro = reverse_lst(self.parking2).inicio
                for x in range(len(self.parking2)):
                    self.parking1.append(ponteiro.data)
                    ponteiro = ponteiro.next
            if self.parking2.inicio:
                self.parking2.next = self.parking2.inicio = None
        else:
            print("Placa não econtrada.")

    def getplaca(self, placa):
        ponteiro = self.parking1.inicio
        while ponteiro:
            if ponteiro.data.placa_carro == placa:
                return True
            ponteiro = ponteiro.next
        return False

    def getindex(self, placa):
        index = 0
        ponteiroplaca = self.parking1.inicio
        while ponteiroplaca:
            if ponteiroplaca.data.placa_carro == placa:
                break
            else:
                ponteiroplaca = ponteiroplaca.next
                index += 1
        return index

    def exibir(self):
        if not self.parking1:
            print("Estacionamento vazio.")
        pos = 1
        for i in self.parking1:
            print('{}° vaga: {}'.format(pos, str(i)))
            pos += 1



    def menu(self):
        print('-'*25)
        print('1 - Estacionar\n2 - Exibir estacionados\n3 - Devolver\n4 - Sair')
        print('-' * 25)
        while True:
            opc = int(input('>>>'))
            if opc == 4:
                break
            elif opc == 1:
                print("Insira os seguintes dados para estacionar:")
                self.estacionar()
            elif opc == 2:
                self.exibir()
            elif opc == 3:
                self.devolver()
            else:
                print('Opção inválida.')


a = EstacionamentoUAST()
a.menu()