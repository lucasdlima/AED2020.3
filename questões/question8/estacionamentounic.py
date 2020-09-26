from AED.classes.listaligada import ListaLigada


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
        self.parking = ListaLigada()

    def estacionar(self):
        if len(self.parking) < 10:
            placa = input("Placa: ")
            cliente = input("Nome cliente: ")
            modelo = input("Modelo do veículo: ")
            self.parking.append(Carro(placa, cliente, modelo))
            return print("Ok!")
        else:
            return print("Não há vagas.")

    def devolver(self):
        placa = input("Placa: ")
        if self.getplaca(placa):
            primeiro = self.parking[0]
            while True:
                removido = self.parking[0]
                self.parking.busca_remocao(self.parking[0])
                if removido.placa_carro == placa or self.parking[0] == primeiro:
                    break
                self.parking.append(removido)
            print('Carro encontrado e retirado!')
        else:
            print("Placa não econtrada.")

    def getplaca(self, placa):
        ponteiro = self.parking.inicio
        while ponteiro:
            if ponteiro.data.placa_carro == placa:
                return True
            ponteiro = ponteiro.next
        return False

    def exibir(self):
        if not self.parking:
            print("Estacionamento vazio.")
        pos = 1
        for i in self.parking:
            print('{}° vaga: {}'.format(pos, str(i)))
            pos += 1

    def menu(self):
        print('-' * 25)
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
