import time
#O 'a'  significa append (adicionar ao final do arquivo)
with open ("historico_de_estudos.txt" , "a") as arquivo:
    arquivo.write ( "Sessao de estudo iniciada em: {time.ctime()}\n")
    print ("Log de ínicio registrado com sucesso no seu computador!")

    accountant = 0
    while accountant < 5 :
        accountant += 1
        print ( f"Executando tarefa{accountant}...") 
        time.sleep (2) # Simula uma tarefa que leva tempo para ser concluída