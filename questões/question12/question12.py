from AED.questões.question9.classes import *


class Aluno:
    def __init__(self, matricula, nome, media):
        self.matricula = matricula
        self.nome = nome
        self.media = media


lista = ListaDupl()


def cadastar_aluno(lista, matricula, nome, media):
    if not lista.inicio:
        lista.inicio = NoDupl(Aluno(matricula, nome, media), None, None)
        lista.inicio.ant = NoDupl(lista.fim, None, lista.inicio)
    i = 0
    ponteiro = lista.inicio
    while ponteiro:
        if ponteiro.data.matricula < matricula:
            break
        i += 1
        ponteiro = ponteiro.next
    lista.insert(i - 2, Aluno(matricula, nome, media))


class CadastroAluno:
    def __init__(self):
        self.alunos = ListaDupl()

    def cadastrar_novo(self):
        matricula = int(input("N° de matricúla: "))
        nome = str(input("Nome do aluno: "))
        media = float(input("Média do aluno: "))
        if isinstance(matricula, int) and isinstance(nome, str) and len(nome) <= 80 and isinstance(media, float):
            i = 0
            ponteiro = self.alunos.inicio
            for x in self.alunos:
                if ponteiro.data.matricula > matricula:
                    break
                i += 1
                ponteiro = ponteiro.next
            self.alunos.insert(i, Aluno(matricula, nome, media))
        else:
            if not isinstance(matricula, int):
                return print('"{}" não é um número de matricula válido, insira um número inteiro!'.format(matricula))
            if not isinstance(nome, str):
                return print('"{}" não é um nome válido, insira um texto'.format(nome))
            elif not len(nome) <= 80:
                return print('Inserção inválida, insira um nome com menos de 80 caracteres')
            if not isinstance(media, float):
                return print('"{}" não é uma média válida, insira um número de ponto flutuante.'.format(media))

    def __str__(self):
        rt = ''
        ponteiro = self.alunos.inicio
        for a in self.alunos:
            rt = rt + '-\nMatrícula: {} ->\tAluno: {} ->\tMédia: {}\n'.format(ponteiro.data.matricula,
                                                                              ponteiro.data.nome, ponteiro.data.media)
            ponteiro = ponteiro.next
        return rt + '-'

    def menu(self):
        print('-' * 25)
        print('1 - Cadastrar aluno\n2 - Ver alunos cadastrados\n3 - Sair')
        print('-' * 25)
        while True:
            opc = int(input('>>>'))
            if opc == 3:
                break
            elif opc == 1:
                print("Insira os seguintes dados para cadastrar um novo aluno:")
                self.cadastrar_novo()
            elif opc == 2:
                if not self.alunos.inicio:
                    print('Não existe alunos cadastrados.')
                print(self.__str__())
            else:
                print('Opção inválida.')


a = CadastroAluno()
a.menu()
