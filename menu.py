import funcoes
import os

pedidos=[]
entregadores=[]
operacoes=[]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def principal():
    limpar_tela()
    print(f"==== MENU PRINCIPAL ====\n")
    print("1- Gerenciamento de Entregadores")
    print("2- Gerenciamento de Pedidos")
    print("3- Gerenciamento de Operações")
    print("5- Sair")

    opcao = input(f"\nSelecione uma opção: ")
    if opcao == "1":
        gerenciamento_ent()
    elif opcao == "2":
       gerenciamento_pedidos()
    elif opcao == "5":
        exit()
    else:
        print(f"\nOpção inválida. Selecione uma opção válida.")
        principal()

def gerenciamento_ent():
    limpar_tela()
    print(f"\n==== GERENCIAMENTO ENTREGADORES ====\n")
    print("1- Cadastrar Entregador")
    print("2- Listar Entregadores")
    print("3- Associar Pedidos")
    print("4- Relatório Entregadores")
    print("5- Voltar")

    opcao = input(f"\nSelecione uma opção: ")
    if opcao == "1":
        cadastro_ent()
    elif opcao == "2":
        listar_ent()
    elif opcao == "5":
        principal()
    else:
        gerenciamento_ent()


def cadastro_ent():
    lista = funcoes.cadastro_entregador(entregadores)
    if(lista!=None):
        entregadores.append(lista)
    principal()

def listar_ent():
    funcoes.listar_entregadores(entregadores)
    input(f"\nPressione Enter para voltar ao menu principal")
    principal()

       
def gerenciamento_pedidos():
    limpar_tela()
    print(f"==== GERENCIAMENTO PEDIDOS ====\n")
    print("1- Cadastrar Pedido")
    print("2- Listar Pedidos")
    print("3- Consultar Pedido")
    print("4- Atualização de Pedido")
    print("5- Voltar")

    opcao = input(f"\nSelecione uma opção: ")
    if opcao == "1":
        cadastro_pedidos()
    elif opcao == "2":
        listar_pedidos()
    elif opcao == "3":
        consulta_pedido()
    elif opcao == "4":
        atualizar_pedido()
    elif opcao == "5":
        principal()
    else:
        gerenciamento_pedidos()



def atualizar_pedido():
    limpar_tela()
    opcao=None
    while opcao == None:
        print(f"\n==== ATUALIZAÇÃO ====\n")
        print("1- Alterar Status")
        print("2- Cancelar Pedido")
        print("3- Associar Entregador")
        print("4- Remover Entregador")
        print("5- Voltar")
        o = input(f"\nQual alteração deseja fazer: ")
        if(o== "1"):
            funcoes.alt_status(pedidos)
            gerenciamento_pedidos()
        elif(o== "2"):
            funcoes.cancel_pedido(pedidos)
        elif (o== "3"):
            funcoes.ass_entregador(pedidos,entregadores)
        elif (o== "4"):
            funcoes.remover_ent(pedidos,entregadores)
            principal()
        elif (o== "5"):
            gerenciamento_pedidos()
        else:
            print(f"\nSelecione uma das opções: ")
            opcao== None


def cadastro_pedidos():
    lista = funcoes.cadastro_pedidos(pedidos, entregadores)

    if(lista!=None):
        pedidos.append(lista)
    principal()

def listar_pedidos():
    funcoes.listar_pedidos(pedidos, entregadores)
    input(f"\nPressione Enter para voltar ao menu principal")
    principal()

def consulta_pedido():
    lista = funcoes.consultar_pedidos(pedidos)

    if lista == "VOLTAR":
        principal()
    else:
        print(lista)
        input(f"\nPressione Enter para voltar ao menu principal")
        principal()

    


principal()
