class Armas:
    def __init__(self, id, nome, custo, dano, peso, propriedade):
        self.id = id
        self.nome = nome
        self.custo = custo
        self.dano = dano
        self.peso = peso
        self.propriedade = propriedade
        self.danoExtra = None
        self.recomendada = '(Arma Recomendada!)'
        self.descricao = ''
        if (dano > 15) :
            self.danoExtra = '+2'

    def addDescricao(self, descricao):
        self.descricao = f'''
            ######################################################################################################
            {descricao}
            ######################################################################################################
        '''


    def toString(self, recomenado = False):
        if recomenado:
            return f'''
    id: {self.id}
    nome: {self.nome} {self.recomendada}
    custo: {self.custo}
    dano: {self.dano}
    peso: {self.peso}
    propriedade: {self.propriedade}
            '''
        return f'''
    id: {self.id}
    nome: {self.nome}
    custo: {self.custo}
    dano: {self.dano}
    peso: {self.peso}
    propriedade: {self.propriedade}
        '''