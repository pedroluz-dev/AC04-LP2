from abc import ABC,


class Pessoa(ABC):
    def __init__(self, nome, telefone, rg, cpf):
        self.nome = nome
        self.telefone = telefone
        self.rg = rg
        self.cpf = cpf


class Medico(Pessoa):
    def __init__(self)
