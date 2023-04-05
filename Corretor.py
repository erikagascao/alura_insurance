from Pessoa import Pessoa

class Corretor(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, contato, num_susep, apolice):
        super().__init__(primeiro_nome, sobrenome, None, None, None, None, contato)
        self._num_susep= num_susep
        self._apolice = apolice