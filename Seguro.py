from typing import List
from enum import Enum
from datetime import date, datetime
import regex as re
from Endereco import Endereco
from Estados import Estados
from Apolice import Apolice, TipoApolice
from Beneficiario import Beneficiario
from Calculadora import Calculadora
from Contato import Contato
from Corretor import Corretor
from Pessoa import Pessoa
from Segurado import Segurado


Contato1=Contato("123","123","123","erikagascao@gmail.com")
endereco1=Endereco("MERCES",'1',"casa 4","25585-180","RJ","SJM")
pessoa1=Pessoa("Erika","Nascimento",date(1995,11,20),"133.242.267-59",'',endereco1,Contato1)
pessoa1=Pessoa("Erika","  ",date(1995,11,20),"   ",123,endereco1,123)

X={'Primeiro Nome': 'ERIKA','Sobrenome':'NASCIMENTO'}
X.values
 
endereco1 = Endereco("Merces", '43', "casa", "123", "RJ", "RJ")
endereco2 = Endereco("Tres Rios", 172, "casa", "22745160", "RJ", "RJ")
Pessoa1=Pessoa("Erika","Nasc",date(2010, 1, 1),"133.242.267-59","123",endereco2,Contato1)
benef1 = Beneficiario("Erika", "Gascao", date(2010, 1, 1), "133.242.267-59", "798", endereco1, "abc", "filha")
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "790.066.557-91","123",endereco2, "hdkhbd", "esposa")
corret1 = Corretor("Paloma", "Ferraz", "002", "999", "774")            
seg1 = Segurado ("Diego", "Guerrieri", "30/11/1987", "05878456", "21245", endereco2, "1254877", [benef1, benef2], corret1, "apol1")
apol1 = Apolice (1, TipoApolice.Vida, 100, 1000000, seg1,corret1, date(2023, 1, 1), date(2023, 3, 30),"Ativa")
apol2 = Apolice (2, TipoApolice.Casa, 500, 5000000, seg1,corret1, date(2023, 2, 2), date(2023, 3, 30),"Ativa")
calc1 = Calculadora([apol1, apol2])
apol1._tipo.value

endereco2 = Endereco("Tres Rios", 172, "casa", "22745160", "RJ", "RJ")
Pessoa1=Pessoa("Erika","Nasc",date(2010, 1, 1),"133.242.267-59","123",endereco2,Contato1)
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "790.066.557-91","123",endereco2, "hdkhbd", "esposa")

# calc1.calcula()


# print(benef1)


# seg1._beneficiarios[0]._primeiro_nome
# seg1._beneficiarios[0]
# print(seg1)
