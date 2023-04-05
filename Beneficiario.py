from Pessoa import Pessoa


class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo

    def __repr__(self):
        return self.__str__()

