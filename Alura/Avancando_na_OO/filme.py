class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like (self):
        self.likes += 1
    
    
        
class Serie:
    
    def __init__(self, name, ano, temporadas):
        self.name = name.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like (self):
        self.likes += 1