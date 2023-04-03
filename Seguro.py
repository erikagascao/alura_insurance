from typing import List
from enum import Enum
from datetime import date
import regex as re

class Estados(Enum):
    RJ = 1
    SP = 2
    PE = 3
    AM = 4
    GO = 2

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
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco: Endereco, contato):

        formato_cpf = re.compile('\d{3}\.\d{3}\.\d{3}\-\d{2}')
        if not formato_cpf.search(cpf):
            return print(f"Digite um CPF válido")

        dict= {'Primeiro Nome': primeiro_nome,'Sobrenome':sobrenome}   
        for nome in dict:
            if not dict[nome] or not dict[nome].strip() or len(dict[nome])<=2:
                return print(f"Digite um {nome} válido")
            
        if not rg:
            return print(f"Digite um RG válido")
        try:
            Estados[endereco._estado] 
        except(KeyError):
            return print("Digite um estado válido")
        
        dict2= {'rua': endereco._rua,'numero': endereco._numero,'cep':endereco._cep, 'cidade': endereco._cidade}   
        try:
            for nome in dict2:
                if not dict2[nome] or not dict2[nome].strip():
                    return print(f"Digite um {nome} válido")
        except(AttributeError):
            if endereco._numero==0:
                return print(f"Digite um {nome} válido")
            else: pass
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

endereco1=Endereco("MERCES","  ","casa 4","25585-180","RJ","SJM")
pessoa1=Pessoa("Erika","Nascimento",date(1995,11,20),"133.242.267-59",123,endereco1,123)
pessoa1=Pessoa("Erika","Nascimento",date(1995,11,20),"1",123,endereco1,123)
pessoa1=Pessoa("   ","Nascimento",date(1995,11,20),"133.242.267-59",123,endereco1,123)

X={'Primeiro Nome': 'ERIKA','Sobrenome':'NASCIMENTO'}
X.values

class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo

    def __repr__(self):
        return self.__str__()

class Corretor(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, contato, num_susep, apolice):
        super().__init__(primeiro_nome, sobrenome, None, None, None, None, contato)
        self._num_susep= num_susep
        self._apolice = apolice


class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios: List[Beneficiario], corretor: List[Corretor], apolice):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._beneficiarios = beneficiarios
        self._corretor = corretor
        self._apolice = apolice
        
    def __str__(self):
        lista = [str(p) for p in self._beneficiarios]
        return f"{lista}"

class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4
        
class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado: Segurado, corretor: Corretor, vig: date, dt_criacao: date, status):
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._valor_benef = valor_benef
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        self._dt_criacao = dt_criacao
        self._status = status
    
    def __str__(self):
        return f"{self._numero} - {self._vig.strftime('%d/%m/%Y')} - {self._dt_criacao.strftime('%d/%m/%Y')}"            

class Calculadora():
    
    def __init__(self, apolice: List[Apolice]):
        self._apolice = apolice
        
    
    def calcula(self):
        valor = 0
        for i in self._apolice:
            if i._tipo.value == 1:
                valor += 0.005 * i._valor_premio + 100 + (1000 if i._valor_benef > 850000 else 0)
            elif i._tipo.value == 2:
                valor += 0.0035 * i._valor_premio + 75.50
            elif i._tipo.value == 3:
                valor += 0.002 * i._valor_premio
            else:
                valor += 200
        return valor    
        

     
# endereco1 = Endereco("Merces", 43, "casa", "123", "Rio de Janeiro", "RJ")
# endereco2 = Endereco("Tres Rios", 172, "casa", "22745160", "Rio de janeiro", "RJ")
# benef1 = Beneficiario("Erika", "Gascao", date(2000, 1, 1), "123456", "798", endereco1, "abc", "filha")
# benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "45679", "9878",endereco2, "hdkhbd", "esposa")
# corret1 = Corretor("Paloma", "Ferraz", "002", "999", "774")            
# seg1 = Segurado ("Diego", "Guerrieri", "30/11/1987", "05878456", "21245", endereco2, "1254877", [benef1, benef2], corret1, "apol1")
# apol1 = Apolice (1, TipoApolice.Vida, 100, 1000000, seg1,corret1, date(2023, 1, 1), date(2023, 3, 30),"Ativa")
# apol2 = Apolice (2, TipoApolice.Casa, 500, 5000000, seg1,corret1, date(2023, 2, 2), date(2023, 3, 30),"Ativa")
# calc1 = Calculadora([apol1, apol2])
# apol1._tipo.value

# calc1.calcula()


# print(benef1)


# seg1._beneficiarios[0]._primeiro_nome
# seg1._beneficiarios[0]
# print(seg1)
