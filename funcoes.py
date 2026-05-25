
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
    while len(id_pedido) != 5 or not id_pedido[0].isalpha() or not id_pedido[1:].isdigit():
        print("Id do pedido deve conter 5 caracteres, sendo a primeira letra e as demais números.")
        id_pedido = input("Digite o Id do pedido: ")

    
    id_entregador= int(input('Digite o id do entregador: '))

    lista = [nome_cliente, endereco, prioridade, descricao, status, id_pedido, id_entregador]
    return lista
    

def consultar_pedidos(lista_pedidos):
    id_pedido = input("Digite o Id do pedido: ")
    for pedido in lista_pedidos:
        if pedido[5] == id_pedido:
            return pedido
    print("Pedido não encontrado.")
    return None