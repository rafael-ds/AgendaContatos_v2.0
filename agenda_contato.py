# RD DevWeb 03 de Setembro 2021
# Projeto de Agenda de Contatos
# OBJ academico. Praticar banco de dado MySQL junto a linguagem Python
import pymysql as psql
from time import sleep
from datetime import datetime as dt

# Meu pacotes
from BD import bd
from Class import my_class as mc
from Queries import queries

print('\n ========================== Agenda de Contato v2.0 ========================== \n')
sleep(.5)
conn = bd.conexao_bd()
sleep(.5)

try:
    # Executado no primeiro usu do programa
    # Criação do Banco
    # Criação das tabelas Usuario e Contatos
    sleep(1)

    # CRIA UM BANCO CHAMADO BD_AGENDA
    conn.execute('CREATE DATABASE BD_AGENDA')
    sleep(.5)

    # Chamada da criação da tabela Usuario
    bd.tabela_user()
    sleep(.5)

    # Chamada da criação da tabela Contatos
    bd.tabela_contatos()

    # Chamada da Função que cria um tabela usuario

    print('\n---- Agenda esta sendo configurada ----\n')
    sleep(2)
    print('\n---- Sua agenda esta configurada para seu uso ----'
          'Reinicia sua agenda\n')


except psql.err.ProgrammingError:
    def principal():
        print(' ------------ Login ------------ ')

        # Execução do banco
        conn.execute('USE BD_AGENDA')

        try:
            acessar = int(input('1 - Entrar | 2 - Criar Usuario: '))

            if acessar == 1:
                nome = input('Usuario: ')
                senha = input('Senha: ')

                # Formatação para iterar com o Banco
                formatacao = '\'' + nome + '\'' + 'AND SENHA=' + '\'' + senha + '\''
                checar = """SELECT NOME FROM USUARIO WHERE NOME="""
                concat = checar + formatacao

                # Verifica se o concat é verdadeiro
                if conn.execute(concat):

                    def menu():
                        """
                        Função que tem como objetivo
                        acesso aos contatos e configuração
                        """

                        # Estetica que mostar uma mensagem de boas vindas
                        for i in conn:
                            print(f'Seja bem vindo(a) {i[0]}! ')

                        print('\n----------- Menu -------------\n')
                        print('1 - Meus contatos | 2 - Configurações | 3 - Sair')

                        try:
                            opc_menu = int(input('Entre com a opção: '))

                            # Opção Meus Contatos
                            if opc_menu == 1:
                                print('\n--------------------------------------\n')
                                print('1 - Mostrar Contatos.\n'
                                      '2 - Inserir Contatos.\n'
                                      '3 - Buscar por Contato.\n'
                                      '4 - Alterar Contato.\n'
                                      '5 - Excluir Contato.\n'
                                      '6 - Limpar Agenda.\n'
                                      '7 - Sair\n')
                                print('--------------------------------------\n')

                                try:
                                    opc_sub = int(input('Entre com a opção: '))

                                    # Mostar Contatos
                                    if opc_sub == 1:
                                        con = bd.conexao_bd()
                                        con.execute('USE BD_AGENDA')

                                        # OBS contatos acessivel a todos
                                        nome_user = nome
                                        con.execute("SELECT IDUSUARIO FROM USUARIO WHERE NOME =%s;", nome_user)

                                        for i in con:
                                            # Comando de projeção dos dados
                                            con.execute(
                                                "SELECT NOME_CONT, EMAIL, TELEFONE FROM CONTATOS WHERE ID_USUARIO =%s;",
                                                i[0])

                                            # Loop que projeta uma Queris com os contatos
                                            # do usuario.
                                            print('-------- Meus Contatos -----------\n')
                                            print(' Nome |-| Email |-| Telefone ')
                                            sleep(.5)
                                            for c in con:
                                                print(f' {c[0]} -- {c[1]} -- {c[2]} ')

                                        menu()

                                    # Inserir Contatos
                                    elif opc_sub == 2:

                                        print('------- Inserir Contatos --------')

                                        nome_cont = str(input('Nome: ')).title()
                                        email_cont = str(input('email: '))
                                        tel_cont = str(input('Telefone: '))
                                        print(f'\n----------- Confirmar -----------\n'
                                              f'Nome: {nome_cont}\n'
                                              f'Email: {email_cont}\n'
                                              f'Telefone: {tel_cont}\n'
                                              f'------------------------------------')

                                        inserir = str(input(f'Inserir? S/N: '))

                                        if inserir == 's' or inserir == 'S':
                                            # tab_cont -> tabela contatos
                                            con = bd.conexao_bd()

                                            # ACESSANDO BD_AGENDA
                                            con.execute('USE BD_AGENDA')

                                            # variavel que recebe como valor
                                            # o nome do usuario
                                            nome_user = nome

                                            # Queri que busca o id do usuario conparando com o nome do mesmo
                                            # guardado na variavel 'nome_user'
                                            con.execute("SELECT IDUSUARIO FROM USUARIO WHERE NOME =%s;", nome_user)

                                            # Inserindo contatos
                                            for i in con:
                                                # print(i)
                                                bd.inserir_contato(nome_cont, email_cont, tel_cont, i[0])

                                            sleep(.5)
                                            menu()

                                        elif inserir == 'n' or inserir == 'N':
                                            print('Inserção cancelada.\n')
                                            sleep(.5)
                                            menu()

                                    # Buscar Contatos
                                    elif opc_sub == 3:

                                        # Função que busca um contatos expecifico
                                        def contatos():
                                            id_u = queries.id_user(nome)
                                            conn.execute("SELECT NOME_CONT, EMAIL, TELEFONE FROM CONTATOS WHERE "
                                                         "ID_USUARIO =%s;", id_u)

                                            return conn

                                        nome_cont = input('Nome Contato: ').title()

                                        for i in contatos():
                                            if i[0] == nome_cont:
                                                print('-------- Contato -----------\n')
                                                print(' Nome |---| Email |---| Telefone ')
                                                sleep(.5)
                                                print(f' {i[0]} -- {i[1]} -- {i[2]} ')

                                        menu()

                                    # Alterar Contatos
                                    elif opc_sub == 4:
                                        print('----------- Alterar Contatos ---------\n')
                                        # alterar = input('1 - Alterar N')
                                        pass
                                    # Excuir Contatos
                                    elif opc_sub == 5:
                                        pass

                                    # Limpar Agenda
                                    elif opc_sub == 6:
                                        pass

                                    # Sair
                                    elif opc_sub == 7:
                                        sleep(1)
                                        principal()

                                except ValueError:
                                    print('Por favor insira um valor numérico:\n')

                            # Opção Cnfiguração
                            elif opc_menu == 2:
                                pass

                            # Opção Sair
                            elif opc_menu == 3:
                                sleep(.5)
                                principal()

                        except ValueError:
                            print('Por favor insira um valor numérico:\n')

                    menu()

                else:
                    print('* Usuario ou senha incorreta.')
                    sleep(.5)
                    principal()

            elif acessar == 2:
                print('1 - Criar Usuario | 2 - Login | 3 - Sair')

                while True:
                    try:
                        # senha = input('Senha de acesso do BD')
                        opc = int(input('Entre com a opção: '))

                        # Opção Criar Usuario
                        if opc == 1:
                            nome = str(input('Nome do(a) usuario(a): '))
                            senha = str(input('Senha do(a) usuario(a): '))
                            tipo = str(input('Tipo de usuario(a): AMD/CSL'))

                            # Objeto usuario
                            user = mc.Usuario(nome, senha, tipo)

                            # inserção do objeto no banco
                            bd.inserir_usuario(user.nome(), user.senha(), user.tipo())

                            sleep(1)
                            principal()

                        # Opção Login
                        elif opc == 2:
                            sleep(.5)
                            principal()

                        # Opção Sair
                        elif opc == 3:
                            sleep(.7)
                            exit(0)

                    except ValueError:
                        print('Por favor insira um valor numérico:\n ')

        except ValueError:
            print('Por favor insira um valor numérico:\n')

    principal()
