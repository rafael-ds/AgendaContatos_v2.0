# from BD import bd
import pymysql as sql
from time import sleep

# conn = bd.conexao_bd()
# conn.execute('USE BD_AGENDA')

senha = input('Confirme a senha do MySQL: ')
conn = sql.connect(
    host="localhost",
    user="root",
    password=senha,
    database='bd_agenda'
)
cursor = conn.cursor()


def id_user(n):
    """
    Função que busca o usuario conectado e
    retorna o ID do mesmo

    :return: Retorno do ID do tipo INT
    """

    cursor.execute("SELECT IDUSUARIO FROM USUARIO WHERE NOME =%s;", n)
    for i in cursor:
        return i[0]


def update_nome(novo_cont, nome_cont, id_us):
    """
    Função de atualização do nome de um contato

    :param novo_cont: nome para o novo contato
    :param nome_cont: nome atual do contato
    :param id_us: Id do usuario atravez da chamada da fução id_user(n)
                  para identificar a FK na REFERENCIA na tabela contato
    """
    update_user = "UPDATE CONTATOS SET NOME_CONT =%s WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (novo_cont, nome_cont, id_us)

    cursor.execute(update_user, dados)
    conn.commit()
    print(cursor.rowcount, 'Usuario(s) modificados com sucesso.')
    # cursor.close()


def update_email(novo_email, nome_cont, id_):
    """
    Função de atualização do email de um contato

    :param novo_email: Novo Email
    :param nome_cont: Nome do contato
    :param id_: Id do usuario atravez da chamada da fução id_user(n)
                para identificar a FK na REFERENCIA na tabela contato

    """
    update_user = "UPDATE CONTATOS SET EMAIL =%s WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (novo_email, nome_cont, id_)

    cursor.execute(update_user, dados)
    conn.commit()
    print(cursor.rowcount, 'Usuario(s) modificados com sucesso.')
    # cursor.close()


def update_tel(tel, nome, id_):
    """
    Função de atualização do telefone de um contato

    :param tel: Novo telefone do contato
    :param nome: Nome do contato para atualização
    :param id_: Id do usuario atravez da chamada da fução id_user(n)
                para identificar a FK na REFERENCIA na tabela contato
    """
    update_user = "UPDATE CONTATOS SET TELEFONE =%s WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (tel, nome, id_)

    cursor.execute(update_user, dados)
    conn.commit()
    print(cursor.rowcount, 'Usuario(s) modificados com sucesso.')
    # cursor.close()


def delete_contatos(nome, id_usuario):
    """
    Função de deleção de contatos

    :param nome: Nome do contato para deleção
    :param id_usuario: Id do usuario atravez da chamada da fução id_user(n)
                       para identificar a FK na REFERENCIA na tabela contato
    """

    delete = "DELETE FROM CONTATOS WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (nome, id_usuario)

    cursor.execute(delete, dados)

    conn.commit()
    print(cursor.rowcount, 'Usuario(s) excluido com sucesso.')
    # cursor.close()


def apagar_reg(id_usuario):
    """
    Função que apaga todos os registros de um agenda referente ao seu usuario

    :param id_usuario: Id do usuario atravez da chamada da fução id_user(n)
                       para identificar a FK na REFERENCIA na tabela contato
    """
    apagar = "DELETE FROM CONTATOS WHERE ID_USUARIO = %s"
    dados = id_usuario

    cursor.execute(apagar, dados)

    conn.commit()
    print(cursor.rowcount, 'Dados excluido com sucesso.')
    # cursor.close()


def config(nome):

    """
    Função de configuração
    :param nome:
    :return:
    """
    admin = "SELECT TIPO FROM USUARIO WHERE NOME=%s AND TIPO=%s"
    tipo = (nome, 'adm')

    cursor.execute(admin, tipo)

    if cursor:
        for i in cursor:
            if i[0] == 'adm':
                try:
                    opc = int(input('1 - Alterar usuario | 2 - Excluir usuario: '))

                    if opc == 1:
                        try:
                            alterar = int(input('\n1 - Alterar nome | 2 - Alterar senha | 3 - Alterar tipo'))

                            # Alterando nome de usuario
                            if alterar == 1:
                                print('------ Alterar Nome de Usuario ---------\n')

                                nome_user = input('Nome do usuario a ser alterado: ')
                                novo_nome = input('Novo nome para o usuario.\n').upper()

                                upd = "UPDATE USUARIO SET NOME =%s WHERE NOME =%s;"
                                dados = (novo_nome, nome_user)
                                sleep(.5)
                                cursor.execute(upd, dados)

                                conn.commit()
                                print(cursor.rowcount, 'Nome do usario(a) alterado com uscesso.')
                                # cursor.close()

                            # Alterando senha de usuario
                            elif alterar == 2:
                                print('\n------ Alterar Senha de Usuario ---------\n')

                                nome_user = input('Nome do usuario a ser alterado: ')
                                nova_senha = input('Insira uma nova senha: ')

                                upd = "UPDATE USUARIO SET SENHA =%s WHERE NOME =%s;"
                                dados = (nova_senha, nome_user)

                                sleep(.5)
                                cursor.execute(upd, dados)

                                conn.commit()
                                print(cursor.rowcount, 'Senha alterado com uscesso.')
                                # cursor.close()

                            # Alterando tipo de usuario
                            elif alterar == 3:
                                print('\n------ Alterar Tipo de Usuario ---------\n')

                                nome_user = input('Nome de usuario a ser alterado: ')
                                novo_tipo = input('Insira qual sera o tipo do usuario. ADM/CSL: ').upper()

                                upd = "UPDATE USUARIO SET TIPO =%s WHERE NOME =%s;"
                                dados = (novo_tipo, nome_user)

                                sleep(.5)
                                cursor.execute(upd, dados)

                                conn.commit()
                                print(cursor.rowcount, 'Tipo do usuario alterado com uscesso.')
                                # cursor.close()

                        except ValueError:
                            print('Insira um valor numérico. ')

                    elif opc == 2:
                        print('----- Excluir usiario ------\n')

                        nome_user = input('Nome do usuario a ser excluido')

                        deletar = input(f'Deletar usuario {nome_user}?\n'
                                        f'Todos os dados de {nome_user} serão '
                                        f'removidos permanentemente.\n'
                                        f'S/N: ')

                        # Apagando registro do usuario
                        if deletar == 's' or deletar == 'S':
                            print('Deletando usuario..')
                            sleep(1)
                            # Apagando contatos do usuairo
                            apagar_reg(id_user(nome_user))

                            dlt = "DELETE FROM USUARIO WHERE NOME =%s;"
                            # Excluindo o usuario
                            cursor.execute(dlt, nome_user)
                            conn.commit()
                            print(cursor.rowcount, 'Usuario deletado com uscesso.')

                except ValueError:
                    print('Insira um valor numérico. ')

    return cursor
