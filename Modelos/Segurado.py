from typing import List

from Beneficiario import beneficiario
from Contato import contato
from Endereco import endereco
from Pessoa import pessoa

class Segurado:
    def __init__(
        self,
        pessoa: pessoa,
        endereco: endereco,
        contato: contato,
        beneficiarios: List[beneficiario],
        apolices,
    ):
        self._pessoa = pessoa
        self._endereco = endereco
        self._contato = contato
        self._beneficiarios = beneficiarios
        self._apolices = apolices