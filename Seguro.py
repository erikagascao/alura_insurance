from typing import List
from enum import Enum

class Endereco():
    def __init__(self, rua, numero, complemento, cep, estado, cidade):
        self._rua = rua
        self._numero = numero
        self._complemento = complemento
        self._cep = cep
        self._estado = estado
        self._cidade = cidade
    
    def __str__(self):
        return f"{self._rua} - {self._numero}"

class Pessoa():
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco: Endereco, contato):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._data_nasc = data_nasc
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._contato = contato

    def nome_completo(self):
        return f"{self._primeiro_nome.title()} {self._sobrenome.title()}"

    def __str__(self):
        return f"{self._primeiro_nome}"       
           
class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo

    def __str__(self):
        return f"{self._primeiro_nome}"

class Corretor():
    def __init__(self, primeiro_nome, sobrenome, contato, num_susep, apolice):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._contato = contato
        self._num_susep= num_susep
        self._apolice = apolice

class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios: List[Beneficiario], corretor: List[Corretor], apolice):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._beneficiarios = beneficiarios
        self._corretor = corretor
        self._apolice = apolice
        
    def __str__(self):
        lista = []
        for p in self._beneficiarios:
            lista += [p._primeiro_nome]    
        return f"{lista}"

class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4
        
class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado: Segurado, corretor: Corretor, vig, dt_criacao, status):
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._valor_benef = valor_benef
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        self._dt_criacao = dt_criacao
        self._status = status
        
     
# endereco1 = Endereco("Merces", 43, "casa", "123", "Rio de Janeiro", "RJ")
# endereco2 = Endereco("Tres Rios", 172, "casa", "22745160", "Rio de janeiro", "RJ")
# benef1 = Beneficiario("Erika", "Gascao", "01/01/2000", "123456", "798", endereco1, "abc", "filha")
# benef2 = Beneficiario("Fernanda", "Muniz", "21/07/1992", "45679", "9878",endereco2, "hdkhbd", "esposa")
# corret1 = Corretor("Paloma", "Ferraz", "002", "999", "774")            
# seg1 = Segurado ("Diego", "Guerrieri", "30/11/1987", "05878456", "21245", endereco2, "1254877", [benef1, benef2], corret1, "apol1")

# print(seg1)