# RD DevWeb 03 de Setembro 2021
# Projeto de Agenda de Contatos
# OBJ academico. Praticar banco de dado MySQL junto a linguagem Python
import pymysql as psql
from time import sleep
from datetime import datetime as dt

#Meu pacotes
from BD import bd
from Class import my_class as mc

print('\n ========================== Agenda de Contato v2.0 ========================== \n')
sleep(.5)
bd = bd.conexao_bd()
sleep(.5)

try:
    sleep(1)

    # CRIA UM BANCO CHAMADO BD_AGENDA
    bd.execute('CREATE DATABASE BD_AGENDA')

    # Chamada da Função que cria um tabela usuario
    sql.tabela_user()

    print('\n---- Agenda esta sendo configurada ----\n')
    sleep(2)
    print('\n---- Sua agenda esta configurada para seu uso ----'
          'Reinicia sua agenda\n')


except psql.err.ProgrammingError:
    def principal():
        print(' ------------ Login ------------ ')

        # Execução do banco
        bd.execute('USE BD_AGENDA')

        nome = input('Usuario: ')
        senha = input('Senha: ')

        # Formatação para iterar com o Banco
        formatacao = '\'' + nome + '\'' + 'AND SENHA=' + '\'' + senha + '\''
        checar = """SELECT NOME FROM USUARIO WHERE NOME="""
        concat = checar + formatacao

        # Verifica se o concat é verdadeiro
        if bd.execute(concat):

            def menu():
                """
                Função que tem como objetivo
                acesso aos contatos e configuração
                """

                # Estetica que mostar uma mensagem de boas vindas
                for i in bd:
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
                                pass

                            # Inserir Contatos
                            elif opc_sub == 2:
                                pass

                            # Buscar Contatos
                            elif opc_sub == 3:
                                pass

                            # Alterar Contatos
                            elif opc_sub == 4:
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
            print('Usuario não encontrado.\n')
            print('1 - Criar Usuario | 2 - Login | 3 - Sair')

            while True:
                try:
                    # senha = input('Senha de acesso do BD')
                    opc = int(input('Entre com a opção: '))

                    # Opção Criar Usuario
                    if opc == 1:
                        conn = psql.connect(
                            host='localhost',
                            user='root',
                            password='1234',
                            database='BD_AGENDA'
                        )

                        cursor = conn.cursor()

                        nome = str(input('Nome do(a) usuario(a): '))
                        senha = str(input('Senha do(a) usuario(a): '))
                        tipo = str(input('Tipo de usuario(a): AMD/CSL'))

                        usuario = mc.Usuario(nome, senha, tipo)

                        cursor.execute("INSERT INTO USUARIO (NOME, SENHA, TIPO) VALUES(%s, %s, %s);",
                                       (usuario.nome(), usuario.senha(), usuario.tipo()))

                        conn.commit()
                        print(cursor.rowcount, 'Usuario(s) inserido com sucesso. ')
                        cursor.close()

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

    principal()



