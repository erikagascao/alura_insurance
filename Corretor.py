from Pessoa import Pessoa
from Contato import Contato

class Corretor():
    def __init__(self, primeiro_nome, sobrenome, contato: Contato, num_susep, apolice):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._contato = contato
        self._num_susep= num_susep
        self._apolice = apolice