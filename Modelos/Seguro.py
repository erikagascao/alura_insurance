class Segurado:
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios, corretor):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__data_nasc = data_nasc
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__contato = contato
        self.__beneficiarios = beneficiarios
        self.__corretor = corretor
        self.premio_total = 0
                        
    def nome_completo_segurado(self):
        return f"{self.__primeiro_nome.title()} {self.__sobrenome.title()}"
    
    @property
    def primeiro_nome(self):
        return self.__primeiro_nome.title()
    
    @property
    def sobrenome(self):
        return self.__sobrenome.title()
    
    def valor_premio(self, valor):
        self.premio_total += valor  
        return self.premio_total
    
    def valor_comissao(self):
        comissao_total = self.premio_total * 0.01
        return comissao_total
        
class Beneficiario:
    def __init__(self, primeiro_nome, sobrenome, dt_nasc, cpf, rg, tipo, endereco, contato ):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__dt_nasc = dt_nasc
        self.__cpf = cpf
        self.__rg = rg
        self.__tipo = tipo
        self.__endereco = endereco
        self.__contato = contato
        
class Apolice():
    def __init__(self, numero, tipo, valor_premio, valor_benef, segurado, corretor, vig, dt_criacao, status):
        self.__numero = numero
        self.__tipo = tipo
        self.__valor_premio = valor_premio
        self.__valor_benef = valor_benef
        self.__segurado = segurado
        self.__corretor = corretor
        self.__vig = vig
        self.__dt_criacao = dt_criacao
        self.__status = status

class Corretor():
    def __init__(self, primeiro_nome, sobrenome, num_susep, apolice, contato):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__num_susep = num_susep
        self.__apolice = apolice
        self.__contato = contato