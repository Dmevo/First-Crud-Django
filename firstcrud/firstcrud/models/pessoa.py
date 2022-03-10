class Pessoa:

    def __init__(self, id=None, nome=None, sobrenome=None, idade=None, cidade=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def get_sobrenome(self):
        return self.sobrenome

    def set_idade(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_cidade(self):
        return self.cidade
