#Biblioteca para manipular arquivos
import os

#Variavel que controla se esta logado/deslogado
log = False

#Menu Principal
def menuPrincipal():
    while True:
        print(f'{10*"*"} Menu Principal {10*"*"}')
        print("[0] Sair")
        print("[1] Menu Cadastro/Login    ")
        print("[2] Menu Bloco de notas    ")
        print(36 * "*")
        opcaoP = int(input("Digite uma opção: "))
        if opcaoP == 0:
            break
        elif opcaoP == 1:
            menuUsuario()
        elif opcaoP == 2 and log == True:
            menuNotas()
        else:
            print("Opção inválida!")

#Cadastro/Login
def menuUsuario():
    while True:
        print(f'{10 * "*"} Menu Usuário {10 * "*"}')
        print("[0] Sair")
        print("[1] Voltar para Menu Principal")
        print("[2] Ir para Menu Bloco de Notas")
        print("[3] Cadastrar")
        print("[4] Login")
        print(36 * "*")
        opcaoU = int(input("Digite uma opçao: "))
        if opcaoU == 0:
            break
        elif opcaoU == 1:
            menuPrincipal()
        elif opcaoU == 2 and log == True:
            menuNotas()
        elif opcaoU == 3:
            cadastro()
        elif opcaoU == 4:
            login()
        else:
            print("Opção Inválida!")

def cadastro():
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha com 8 dígitos mínimos: ")
    if len(senha) < 8:
        print("Senha inválida!\n")
        return cadastro()

    arq1 = open('dados.txt', 'r')
    for i in arq1:
        i = i.strip()
        dados = i.split(' ')
        if dados[0] == usuario:
            print("Nome de usuário já existente!\n")
            return cadastro()

    arq = open('dados.txt', 'a')
    arq.write(f"{usuario} {senha}\n")
    arq.close()
    print("Cadastro feito com sucesso!\n")
    login()

def login():
    global log
    print("Página de Login")
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")
    arq = open("dados.txt",'r')

    for i in arq:
        i = i.strip()
        dados = i.split(" ")
        if usuario == dados[0]:
            if senha == dados[1]:
                print("Login feito com sucesso!\n")
                log = True
                menuNotas()
                break
            else:
                print("Senha incorreta!\n")
                return menuUsuario()

#Notas
def menuNotas():
    while True:
        print(f'{10 * "*"} Menu Bloco de Notas {10 * "*"}')
        print("[0] Sair")
        print("[1] Voltar para menu principal")
        print("[2] Adicionar anotação")
        print("[3] Remover anotação")
        print("[4] Ver anotação")
        print(36 * "*")
        opcaoN = int(input("Digite uma opção: "))
        if opcaoN == 0:
            break
        elif opcaoN == 1:
            menuPrincipal()
        elif opcaoN == 2:
            AddNota()
        elif opcaoN == 3:
            removerNota()
        elif opcaoN == 4:
            verNota()
        else:
            print("Opção Inválida!")

def AddNota():
    nomeArquivo = input("Digite o nome da anotação: ")
    if os.path.exists(f"minhasNotas/{nomeArquivo}.txt"):
        opcao = int(input("Arquivo já existente, deseja sobreescrever [0] ou escolher novo nome [1]: "))
        if opcao == 0:
            pass
        else:
            return AddNota()

    arq = open(f"minhasNotas/{nomeArquivo}.txt","w")
    anotacao = input("Notas: ")
    anotacao = anotacao.replace('.','.\n')
    arq.write(anotacao)
    print("Anotação feita com sucesso!!!")
    arq.close()

def removerNota():
    nome = input("Digite o nome da anotação: ")
    if os.path.exists(f"minhasNotas/{nome}.txt"):
        os.remove(f"minhasNotas/{nome}.txt")
        print("Anotação removida com sucesso!!!")
    else:
        print("Nome incorreto - arquivo não encontrado!")

def verNota():
    nome = input("Digite o nome do arquivo: ")
    if os.path.exists(f"minhasNotas/{nome}.txt"):
        arq = open(f"minhasNotas/{nome}.txt","r")
        linhas = arq.readlines()
        for i in linhas:
            i = i.strip()
            print(i)
        print()
        arq.close()
    else:
        print("Nome incorreto - arquivo não encontrado!")

menuPrincipal()