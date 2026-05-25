
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

    
    id_entregador = input("Digite o Id do entregador: ")
    while len(id_entregador) != 4 or not id_entregador[:].isdigit():
        print("Id do pedido deve conter 4 dígitos")
        id_entregador = input("Digite o Id do pedido: ")


    lista = [nome_cliente, endereco, prioridade, descricao, status, id_pedido, id_entregador]
    return lista

def cadastro_entregador():

    nome_entregador = input("Digite o Nome do Entregador: ")

    veiculo=None
    while veiculo == None:
        print(f"\n====VEÍCULO====")
        print("1- Carro")
        print("2- Van")
        print("3- Moto")
        v = int(input("Selecione o veículo: "))
        if(v==1):
            veiculo = 'Carro'
        elif(v==2):
            veiculo = 'Van'
        elif(v==3):
            veiculo = 'Moto'
        else:
            print("Selecione uma das opções: ")
            veiculo=None
    
    id_entregador = input("Digite o Id do entregador: ")
    while len(id_entregador) != 4 or not id_entregador[:].isdigit():
        print("Id do pedido deve conter 4 dígitos")
        id_entregador = input("Digite o Id do pedido: ")

    id_pedido = input("Digite o Id do pedido: ")
    while len(id_pedido) != 5 or not id_pedido[0].isalpha() or not id_pedido[1:].isdigit():
        print("Id do pedido deve conter 5 caracteres, sendo a primeira letra e as demais números.")
        id_pedido = input("Digite o Id do pedido: ")

    disponibilidade=None
    while disponibilidade == None:
        print(f"\n====DISPONIBILIDADE====")
        print("1- Manhã")
        print("2- Tarde")
        print("3- Noite")
        d = int(input("Selecione a Disponibilidade: "))
        if(d==1):
            disponibilidade = 'Manhã'
        elif(d==2):
            disponibilidade = 'Tarde'
        elif (d==3):
            disponibilidade= 'Noite'
        else:
            print("Selecione uma das opções")
            disponibilidade== None
    

    lista = [nome_entregador, veiculo, id_entregador, id_pedido, disponibilidade]
    return lista

def listar_entregadores(lista_ent):
    for i in range(len(lista_ent)):
        print(lista_ent[i])

def listar_pedidos(lista_pedidos):
    for i in range(len(lista_pedidos)):
        print(lista_pedidos[i])


def consultar_pedidos(lista_pedidos):
    id_pedido = input("Digite o Id do pedido: ")
    for pedido in lista_pedidos:
        if pedido[5] == id_pedido:
            return pedido
    print("Pedido não encontrado.")
    return None
