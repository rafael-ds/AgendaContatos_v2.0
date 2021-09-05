# Class usuario
class Usuario:
    def __init__(self, nome, senha, tipo):
        self.__nome = nome
        self.__senha = senha
        self.__tipo = tipo

    def nome(self):
        return self.__nome

    def senha(self):
        return self.__senha

    def tipo(self):
        return self.__tipo


# Class Contatos
class Contatos:
    def __init__(self, nome, telefone, email=''):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def nome(self):
        return self.__nome

    def tel(self):
        return self.__telefone

    def email(self):
        return self.__email

