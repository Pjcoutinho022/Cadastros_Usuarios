
cadastros = {}


def menu():
    texto = """
     1- Login.
     2- Cadastrar-se.
     3- Lista de Cadastros.
     4- Sair.
     """

    return texto


def verif_login():

    usuario = input("Informe seu usuario: ")
    senha = input("Informe sua senha: ")

    if cadastros.get(usuario) == senha:
        print("\nLogin efetuado com sucesso!")

    else:
        print("Usuário e senha não cadastrados!")


def cadastrar():
    while True:
        usuario = input("Informe seu usuario: ")
        if cadastros.get(usuario):
            print("Este Usuário ja existe!")

        else:
            senha = input("Informe sua senha: ")
            if len(senha) >= 6:
                cadastros[usuario] = senha
                print("\nCadastro realizado com sucesso.\n")
                break

            else:
                print("No minímo 6 caracteres!\n")


def senha_lista_cadastro():
    pin = 7777
    while True:
        senha = int(input("Digite o pin de segurança: "))
        if senha == pin:
            print("""
            Acesso liberado!
                """)

            if not cadastros:
                print("\nNão tem nenhum cadastro!\n")
                break

            else:
                print(cadastros)
                break

        else:
            print("\nPin incorreto! Você não tem permissão para ver a lista de cadastro.")
            break


while True:
    menu()
    try:
        opcao = int(input("\nInforme a opção desejada: "))

        if opcao == 1:
            verif_login()

        elif opcao == 2:
            cadastrar()

        elif opcao == 3:
            senha_lista_cadastro()

        elif opcao == 4:
            break

    except ValueError:
        print("Opção Inválida!")
