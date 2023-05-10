from datetime import date, datetime
from Pessoa import Pessoa
from Endereco import Endereco
from Contato import Contato
from Beneficiario import Beneficiario
from Corretor import Corretor
from Apolice import Apolice, TipoApolice
from Segurado import Segurado



class TestClass:
    def test_quando_chama_nome_completo_retorna_nome_sobrenome(self):
        #Given-Contexto
        nome = 'Erika' 
        sobrenome = 'Gascao'
        esperado = 'Erika Gascao'
        Contato1=Contato("123","123","123","erikagascao@gmail.com")
        endereco1 = Endereco("Merces", '3', "casa", "123", "RJ", "RJ")
        Pessoa1 = Pessoa(nome,sobrenome,date(1995,11,20),'133.242.267-59',"123",endereco1,Contato1)

        #When ação
        resultado=Pessoa1.nome_completo()

        #then desfecho
        assert resultado==esperado