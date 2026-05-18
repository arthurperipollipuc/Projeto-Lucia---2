import random
import os

pedidos=[]
entregadores=[]

def cadastro_pedidos():

    nome_cliente = input("Digite seu Nome: ")
    endereco = input("Digite seu Endereço: ")

    prioridade=None
    while prioridade == None:
        print(f"\n====PRIORIDADE====")
        print("1- Alta")
        print("2- Normal")
        p = int(input("Selecione a prioridade: "))
        if(p==1):
            prioridade = 'Alta'
        elif(p==2):
            prioridade = 'Normal'
        else:
            print("Selecione uma das opções: ")
            prioridade=None
    
    descricao = input("Descreva os detalhes do pedido: ")

    status=None
    while status == None:
        print(f"\n====STATUS====")
        print("1- Pendente")
        print("2- Em Rota")
        print("3- Entregue")
        print("4- Cancelado")
        s = int(input("Selecione o status: "))
        if(s==1):
            status = 'Pendente'
        elif(s==2):
            status = 'Em rota'
        elif (s==3):
            status= 'Entregue'
        elif(s==4):
            status = 'Cancelado'
        else:
            print("Selecione uma das opções")
            status== None
    
    id_pedido = input("Digite o Id do pedido: ")
    if len(id_pedido) != 5:
        return False
    elif not id_pedido[0].isalpha():
        return False
    elif not id_pedido[1:].isdigit():
        return False
    else:
        return True
    
    id_entregador= int(input('Digite o id do entregador: '))
    

    

    
    

print(cadastro_pedidos())
    
