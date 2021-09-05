# importando o pyMySQL
import pymysql as sql


def conexao_bd():
    """
    Função que se conecta a um banco de dados MySQL
    """

    # Pedido de senha caso o acesso ao BD necessite
    # caso contrario so dar ENTER
    # senha = input('Entre com a senha do banco')

    conexao = sql.connect(
        host='localhost',
        user='root',
        password='1234'
    )

    cursor = conexao.cursor()
    return cursor


def tabela_user():
    """
    Função que tem como objetivo a criação da tabela usuario
    """
    tab = conexao_bd()
    # ACESSA O BANCO BD_AGENDA
    tab.execute('USE BD_AGENDA')

    # Cria uma tabela chamada de USUARIO no Banco BD_Agenda
    tab.execute("CREATE TABLE USUARIO("
                "IDUSUARIO INT PRIMARY KEY AUTO_INCREMENT, "
                "NOME VARCHAR(30) NOT NULL,"
                "SENHA VARCHAR(15) NOT NULL,"
                "TIPO CHAR(3) NOT NULL)")

    return tab
