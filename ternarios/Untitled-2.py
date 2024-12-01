nome_usuario = input("Insira o nome de usuário: ")
senha = input("insira a senha: ")

while nome_usuario == senha:
    print("Erro: Usuário e Senha devem ter valores distintos.")
    nome_usuario = input("Insira o nome de usuário: ")
    senha = input("Insira a senha: ")

print("Acesso liberado.")
