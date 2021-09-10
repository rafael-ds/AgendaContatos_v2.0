# from BD import bd
import pymysql as sql

# conn = bd.conexao_bd()
# conn.execute('USE BD_AGENDA')

conn = sql.connect(
    host="localhost",
    user="root",
    password="1234",
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
    update_user = "UPDATE CONTATOS SET NOME_CONT =%s WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (novo_cont, nome_cont, id_us)

    cursor.execute(update_user, dados)
    conn.commit()
    print(cursor.rowcount, 'Usuario(s) modificados com sucesso.')
    cursor.close()


def update_email(novo_email, nome_cont, id_):
    update_user = "UPDATE CONTATOS SET EMAIL =%s WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (novo_email, nome_cont, id_)

    cursor.execute(update_user, dados)
    conn.commit()
    print(cursor.rowcount, 'Usuario(s) modificados com sucesso.')
    cursor.close()


def update_tel(tel, nome, id_):
    update_user = "UPDATE CONTATOS SET TELEFONE =%s WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (tel, nome, id_)

    cursor.execute(update_user, dados)
    conn.commit()
    print(cursor.rowcount, 'Usuario(s) modificados com sucesso.')
    cursor.close()


def delete_contatos(nome, id_usuario):
    delete = "DELETE FROM CONTATOS WHERE NOME_CONT =%s AND ID_USUARIO =%s"
    dados = (nome, id_usuario)

    cursor.execute(delete, dados)

    conn.commit()
    print(cursor.rowcount, 'Usuario(s) excluido com sucesso.')
    cursor.close()


def apagar_reg(id_usuario):
    apagar = "DELETE FROM CONTATOS WHERE ID_USUARIO = %s"
    dados = id_usuario

    cursor.execute(apagar, dados)

    conn.commit()
    print(cursor.rowcount, 'Dados excluido com sucesso.')
    cursor.close()

