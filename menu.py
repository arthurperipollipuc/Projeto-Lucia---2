import funcoes
import os

pedidos=[]
entregadores=[]
operacoes=[]



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def principal():
    limpar_tela()
    print("====MENU PRINCIPAL====")
    print("1- Gerenciamento de Entregadores")
    print("2- Gerenciamento de Pedidos")
    print("3- Gerenciamento de Operações")
    print("5- Sair")

    opcao = int(input(f"\nSelecione uma opção: "))
    if opcao == 1:
        gerenciamento_ent()
    elif opcao == 2:
       gerenciamento_pedidos()
    elif opcao == 5:
        exit()
    else:
        print("Opção inválida. Selecione uma opção válida.")
        principal()

def gerenciamento_ent():
    limpar_tela()
    print("====GERENCIAMENTO ENTREGADORES====")
    print("1- Cadastrar Entregador")
    print("2- Listar Entregadores")

    opcao = int(input(f"\nSelecione uma opção: "))
    if opcao == 1:
        cadastro_ent()
    elif opcao == 2:
        listar_ent()


def cadastro_ent():
    entregadores.append(funcoes.cadastro_entregador())
    principal()

def listar_ent():
    funcoes.listar_entregadores(entregadores)
    input("Pressione Enter para voltar ao menu principal")
    principal()

       
def gerenciamento_pedidos():
    limpar_tela()
    print("====GERENCIAMENTO PEDIDOS====")
    print("1- Cadastrar Pedido")
    print("2- Listar Pedidos")
    print("3- Consultar Pedido")
    print("4- Atualização do Pedido")
    print("5- Voltar")

    opcao = int(input(f"\nSelecione uma opção: "))
    if opcao == 1:
        cadastro_pedidos()
    elif opcao == 2:
        listar_pedidos()
    elif opcao == 3:
        consulta_pedido()
    elif opcao == 4:
        atualizar_pedido()

def atualizar_pedido():
    opcao=None
    while opcao == None:
        print(f"\n====ATUALIZAÇÃO====")
        print("1- Alterar Status")
        print("2- Cancelar Pedido")
        print("3- Associar Entregador")
        print("4- Remover Entregador")
        print("5- Voltar")
        o = int(input("Qual alteração deseja ser feita: "))
        if(o==1):
            funcoes.alt_status(pedidos)
            principal()
        elif(o==2):
            funcoes.cancel_pedido(pedidos)
        elif (o==3):
            funcoes.ass_entregador(pedidos,entregadores)
        elif (o==4):
            funcoes.remover_ent(pedidos,entregadores)
        elif (o==5):
            principal()
        else:
            print("Selecione uma das opções")
            opcao== None


def cadastro_pedidos():
    pedidos.append(funcoes.cadastro_pedidos())
    principal()

def listar_pedidos():
    funcoes.listar_pedidos(pedidos)
    input("Pressione Enter para voltar ao menu principal")
    principal()

def consulta_pedido():
    lista = funcoes.consultar_pedidos(pedidos)
    print(lista)
    input("Pressione Enter para voltar ao menu principal")
    principal()


principal()
