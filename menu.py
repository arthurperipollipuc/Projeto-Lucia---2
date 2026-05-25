import funcoes
import os

pedidos=[]
entregadores=[]
operacoes=[]

def principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====MENU PRINCIPAL====")
    print("1- Cadastrar Pedido")
    print("2- Cadastrar Entregador")
    print("3- Listar Pedidos")
    print("4- Consultar Pedido")
    print("5- Sair")

    opcao = int(input(f"\nSelecione uma opção: "))
    if opcao == 1:
        cadastro_pedidos()
    elif opcao == 4:
        consulta_pedido()
    elif opcao == 5:
        exit()
    else:
        print("Opção inválida. Selecione uma opção válida.")
        principal()


def cadastro_pedidos():
    pedidos.append(funcoes.cadastro_pedidos())
    principal()

def consulta_pedido():
    lista = funcoes.consultar_pedidos(pedidos)
    print(lista)
    input("Pressione Enter para voltar ao menu principal")
    principal()


principal()