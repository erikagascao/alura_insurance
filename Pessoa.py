from typing import List
from enum import Enum
from datetime import date, datetime
import regex as re
from Endereco import Endereco
from Contato import Contato
from Estados import Estados


class Pessoa():
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco: Endereco, contato: Contato):

        lista=[]
        try:
            formato_cpf = re.compile('\d{3}\.\d{3}\.\d{3}\-\d{2}')
            if not formato_cpf.search(cpf): raise (TypeError)
        except(TypeError):
            lista=["Digite um CPF válido"]
            pass
        
        dict= {'Primeiro Nome': primeiro_nome,'Sobrenome':sobrenome}   
        for nome in dict:
            try:
                if not dict[nome] or dict[nome].strip()=="" or len(dict[nome])<=2: "erro" + 1
            except(TypeError):
                lista+=[f"Digite um {nome} válido"]
                pass
        
        try:
            if not rg: "erro" + 1
        except(TypeError):
            lista+=["Digite um RG válido"]
            pass
        
        try:
            Estados[endereco._estado] 
        except(KeyError):
            lista+=["Digite um estado válido"]
            pass

        try:
            formato_email= re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            if not formato_email.search(contato._email): "erro" + 1
        except(TypeError):
            lista=["Digite um email válido"]
            pass
        
        dict2= {'rua': endereco._rua,'numero': endereco._numero,'cep':endereco._cep, 'cidade': endereco._cidade}   
        for nome in dict2:
            try:
                if not dict2[nome] or dict2[nome].strip()=="": 1/0
            except(ZeroDivisionError):
                    lista+= [f"Digite o(a) {nome} válido(a)"]
            except(AttributeError):
                    lista+= [f"Digite o {nome} como string "]
        if lista !=[]:
            return print(lista)
    
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
        return f"{self._primeiro_nome} {self._sobrenome} - {self._data_nasc.strftime('%d/%m/%Y')}"