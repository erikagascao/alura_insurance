from typing import List
from Pessoa import Pessoa
from Beneficiario import Beneficiario
from Corretor import Corretor
from datetime import date, datetime
import regex as re

class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios: List[Beneficiario], corretor: List[Corretor], apolice):
        lista = []
        try:
            teste=0
            if len(beneficiarios)>10:
                teste="erro"
            teste+1
        except(TypeError):
            lista="Número de beneficiários ultrapassou o limite de 10"
            pass

        try:
            idade=datetime.now().year - data_nasc.year
            if datetime.now().month<data_nasc.month:  
                idade+=-1
            teste=0
            if idade<18:
                teste="erro"
            teste+1
        except(TypeError):
            lista="Segurado menor de idade."
            pass

        if lista ==[]:
            pass
        else:
            return print(lista)
  
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        
        self._beneficiarios = beneficiarios
        self._corretor = corretor
        self._apolice = apolice
        
    def __str__(self):
        lista = [str(p) for p in self._beneficiarios]
        return f"{lista}"