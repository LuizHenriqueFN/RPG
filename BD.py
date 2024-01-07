import mysql.connector as BD
from armas import Armas

mydb = BD.connect(
  host="localhost",
  user="root",
  password="",
  database="rpg"
)
repository = mydb.cursor()

# CRUD

##############################################################
comando = 'SELECT * FROM armas'
repository.execute(comando)
armasDoDB = repository.fetchall()
dados = []

for dado in armasDoDB:
    dados.append(Armas(*dado))

dados[2].addDescricao("Elfos possuem proeficiencia em armas de longa distância.")

classeNome = input('Digite sua classe: ')

for dado in dados:
    if(classeNome == 'Elfo' and dado.nome == 'Arco'):
        print(dado.toString(True))
    else:
        print(dado.toString())

#Verificar valor de entrada
armaSelecionada = int(input('Selecione uma arma(): ')) - 1
while True:
    if(armaSelecionada >= 0 and armaSelecionada < len(dados)):
        break
    else:
        armaSelecionada = int(input('Erro! Valor selecionado não existe. Tente novamente(id): '))-1


    
    

armaPersonagem = dados[armaSelecionada]

print('A arma que você selecionou foi:')
print(armaPersonagem.toString())
if classeNome == 'Elfo':
    print(armaPersonagem.descricao)
if armaPersonagem.danoExtra != None:
    print(armaPersonagem.danoExtra)

##############################################################

repository.close()
mydb.close()

