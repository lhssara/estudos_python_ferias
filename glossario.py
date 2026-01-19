import datetime
# 1. Coleta das informações
print ( "--- Novo Registro de Inglês ---")
palavra_en = input("Digite a palavra em inglês: ")
data_atual = datetime.datetime.now() .strftime("%d/%m/%Y %H:%M" )
significado_pt = input("Digite o significado em portiguês: ")
# 2. Formação de dados
info = f" {data_atual} - {palavra_en} : {significado_pt} \n"
# 3. Armazenamento de dados
with open( "meu_dicionario.txt" , "a" , encoding= "utf-8" ) as arquivo:
    arquivo.write(info)
    print("Seu registro foi salvo com sucesso no dicionário!")