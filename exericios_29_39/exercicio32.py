'''
32 - Login Simulado:
Defina um nome de usuário e senha. 
Peça ao usuário que insira o nome de usuário e a senha. 
Se estiverem corretos, imprima "Acesso concedido". 
Se estiverem incorretos, imprima "Acesso negado".
'''
usuario_correto = "admin"
senha_correta = "123"

nome_usuario = input("Digite nome de usuario: ")
senha = input("Digite senha: ")

if nome_usuario == usuario_correto and senha == senha_correta:
    print("Acesso concedido")
else:
    print("Acesso negado")