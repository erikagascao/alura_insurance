class pessoa:
    def __init__(self, primeironome, sobrenome, datanascimento = None ,cpf = None,rg= None, contato = None):
        self._primeironome = primeironome.title()
        self._sobrenome = sobrenome.title()
        self._datanascimento=datanascimento
        self._cpf= cpf
        self._rg= rg
        self._contato= contato

    def nome_completo(self):
        return f'{self._primeironome} {self._sobrenome}'
    
class Beneficiario(Pessoa):
    def __init__(self,  primeironome, sobrenome,datanascimento ,cpf,rg,contato,endereco):
        super().__init__(primeironome, sobrenome,datanascimento ,cpf,rg,contato)
        self.endereco=endereco




segurado1=Pessoa('erika','nasc','20/11/1995','133','248','21984')
benef1=Beneficiario('cristina ','nasc','20/11/1995','133','248','21984','endereço')

