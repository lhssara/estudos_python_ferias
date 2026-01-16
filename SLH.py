import time

# Peça a matéria primeiro
materia = input ( "O que você esta estudando hoje?")

# Depois abra o arquivo para salvar
with open("historico_de_estudos.txt", "a") as arquivo:
    arquivo.write( f"Estudo em {time.ctime()} {materia} \n")

    print(f"Sucesso! Registrado estudo de {materia} em historico_de_estudo.txt")

# O seu contador de tarefas que funcionou ontem
contador = 0
while contador < 3:
    contador += 1
    print( f"Processando progresso da tarefa {contador}...")
    time.sleep(1)