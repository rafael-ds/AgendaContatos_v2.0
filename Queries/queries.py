from BD import bd

conn = bd.conexao_bd()
conn.execute('USE BD_AGENDA')


def id_user(n):
    """
    Função que busca o usuario conectado e
    retorna o ID do mesmo

    :return: Retorno do ID do tipo INT
    """

    conn.execute("SELECT IDUSUARIO FROM USUARIO WHERE NOME =%s;", n)
    for i in conn:
        return i[0]

