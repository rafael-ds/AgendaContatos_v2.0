# importando o pyMySQL
import pymysql as sql


# Acesso ao MySQL
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


# Criação da tabela usuario
def tabela_user():
    """
    Função que tem como objetivo a criação da tabela usuario
    """
    tab_user = conexao_bd()
    # ACESSA O BANCO BD_AGENDA
    tab_user.execute('USE BD_AGENDA')

    # Cria uma tabela chamada de USUARIO no Banco BD_Agenda
    tab_user.execute("CREATE TABLE USUARIO("
                     "IDUSUARIO INT PRIMARY KEY AUTO_INCREMENT, "
                     "NOME VARCHAR(30) NOT NULL,"
                     "SENHA VARCHAR(15) NOT NULL,"
                     "TIPO CHAR(3) NOT NULL)")

    return tab_user


# Criação da tabela contatos
def tabela_contatos():
    """
    Função que tem como objetivo a criação da tabela usuario
    """
    tab_cont = conexao_bd()
    # ACESSA O BANCO BD_AGENDA
    tab_cont.execute('USE BD_AGENDA')

    # Cria uma tabela chamada de USUARIO no Banco BD_Agenda
    tab_cont.execute("CREATE TABLE CONTATOS(IDCONTATOS INT PRIMARY KEY AUTO_INCREMENT,NOME_CONT VARCHAR(30) NOT NULL,"
                     "EMAIL VARCHAR(15),TELEFONE VARCHAR(15) NOT NULL,ID_USUARIO INT NOT NULL,FOREIGN KEY("
                     "ID_USUARIO)REFERENCES USUARIO(IDUSUARIO))")

    return tab_cont


# Inserção de usuarios
def inserir_usuario(nome, senha, tipo):
    """
    Função que tem como objetivo a a inserção de usuarios
    na tabela USUARIO
    :param nome:
    :param senha:
    :param tipo:
    :return:
    """
    conn = sql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='bd_agenda'

    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO USUARIO(NOME, SENHA, TIPO) VALUES(%s, %s, %s);",
                   (nome, senha, tipo))

    conn.commit()
    print(cursor.rowcount, 'Usuario cadastrado com sucesso.')
    cursor.close()


# Inserção de Contatos
def inserir_contato(nome, email, tel, id_u):
    """
    :param nome: nome do contato obrigatorio
    :param email: email do contato 'podendo deixar em em branco
    :param tel: telefone obrigatorio
    :param id_u: id correspontente a id do usuario obrigatorio

    OBS - id_u corrensponte a chave universal
    """

    # Pedido de senha caso o acesso ao BD necessite
    # caso contrario so dar ENTER
    # senha = input('Senha do MySQL: ')

    conn = sql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='BD_AGENDA'

    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO CONTATOS(NOME_CONT, EMAIL, TELEFONE, ID_USUARIO) VALUES(%s, %s, %s, %s);",
                   (nome, email, tel, id_u))

    conn.commit()
    print(cursor.rowcount, 'Contato inserido com sucesso. ')
    cursor.close()
