import mysql.connector
from armas import Armas

mydb = mysql.connector.connect(
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
dadosDoDB = repository.fetchall()
dados = []

for dado in dadosDoDB:
    dados.append(Armas(*dado))

for dado in dados:
    print(dado.toString())

#Verificar valor de entrada

armaSelecionada = int(input('Selecione uma arma(id): ')) - 1
while True:
    if(armaSelecionada >= 0 and armaSelecionada < len(dados)):
        break
    else:
        armaSelecionada = int(input('Erro! Valor selecionado não existe. Tente novamente(id): '))-1


    
    

armaPersonagem = dados[armaSelecionada]

print('A arma que você selecionou foi:')
print(armaPersonagem.toString())

##############################################################

repository.close()
mydb.close()

