class Armas:
    def __init__(self, id, nome, custo, dano, peso, propriedade):
        self.id = id
        self.nome = nome
        self.custo = custo
        self.dano = dano
        self.peso = peso
        self.propriedade = propriedade

    def toString(self):
        return f'''
        id: {self.id}
        nome: {self.nome}
        custo: {self.custo}
        dano: {self.dano}
        peso: {self.peso}
        propriedade: {self.propriedade}
        '''