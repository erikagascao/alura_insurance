from datetime import date, datetime
from Pessoa import Pessoa
from Endereco import Endereco
from Contato import Contato
from Beneficiario import Beneficiario
from Corretor import Corretor
from Apolice import Apolice, TipoApolice
from Segurado import Segurado



class TestClass2:
    
        
    def test_quando_apolice_recebe_dois_valores_200_deve_retornar_400(self):
        # Given - contexto
        valor_premio1 = 200
        valor_premio2 = 200
        esperado = valor_premio1 + valor_premio2
        Contato1 = Contato("123","123","123","erikaabc@gmail.com")
        endereco2 = Endereco("Tres Rios", "172", "casa", "22745160", "RJ", "RJ")
        benef1 = Beneficiario("Erika", "Gascao", date(2000, 1, 1), "123.456.789-99", "798", endereco2, Contato1, "filha")
        benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "123.456.789-99", "9878",endereco2, Contato1, "esposa")
        corret1 = Corretor("Paloma", "Ferraz", "002", "15414612345678901", "774")
        apol1 = Apolice (1,"Vida", valor_premio1, 1000000, "seg1",corret1, date(2024, 1, 1), date(2023, 3, 30),"Ativa")
        apol2 = Apolice (1,"Vida", valor_premio2, 5000000, "seg1",corret1, date(2024, 2, 2), date(2023, 3, 30),"Cancelada")
        seg1 = Segurado ("Diego", "Guerrieri", date(1987,11,30), "112.367.805-97", "1254877", endereco2, Contato1, [benef1, benef2], corret1, [apol1, apol2])
        
        
        resultado = seg1.calcula_premio()
        
        # tehn - desfecho
        # 
        assert resultado == esperado