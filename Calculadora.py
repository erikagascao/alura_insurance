from typing import List
from Apolice import Apolice



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
        