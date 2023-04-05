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