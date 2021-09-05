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

