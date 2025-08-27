def saudacao(nome, cidade):
    if cidade.lower() == "rio de janeiro":
        print(f"{nome}, seja bem-vindo à Cidade Maravilhosa!")
    else:
        print(f"{nome}, você está digitando de {cidade}.")

 Programa principal
nome_usuario = input("Digite seu nome: ")
cidade_usuario = input("Digite a cidade de onde está digitando: ")

 Chamada da função com os argumentos
saudacao(nome_usuario, cidade_usuario)
