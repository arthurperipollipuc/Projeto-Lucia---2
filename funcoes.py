
import verificacoes
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastro_pedidos(lista_pedidos, lista_entregadores):
    limpar_tela()
    print(f"==== CADASTRO DE PEDIDO ====\n")

    nome_cliente = input(f"Digite o Nome do Cliente: ")
    endereco = input(f"\nDigite o Endereço: ")

    prioridade= len(lista_pedidos)+1
    
    descricao = input(f"\nDescreva os detalhes do pedido: ")

    status=None
    while status == None:
        print(f"\n====STATUS====")
        print("1- Pendente")
        print("2- Em Rota")
        print("3- Entregue")
        print("4- Cancelado")
        s = input(f"\nSelecione o status: ")
        if(s== "1"):
            status = 'Pendente'
        elif(s== "2"):
            status = 'Em rota'
        elif (s== "3"):
            status= 'Entregue'
        elif(s== "4"):
            status = 'Cancelado'
        else:
            print("Selecione uma das opções")
            status== None
    
    id = input(f"\nDigite o ID do pedido (1 Letra + 4 dígitos): ")
    while verificacoes.validar_id_pedido(lista_pedidos, id) == "INVALIDO":
        print(f"\no ID do pedido deve ser Original - Conter 5 Caracteres - Iniciar com Letra seguida de 4 Dígitos")
        id = input("Digite o ID do pedido (1 Letra + 4 dígitos): ")
    id_pedido = verificacoes.validar_id_pedido(lista_pedidos, id)

    
    id_entregador = input(f"\nDigite o ID do entregador: ")
    while not verificacoes.verificar_ent(lista_entregadores, id_entregador):
        print(f"\nO ID do entregador não foi Encontrado. Digite um Id válido - ou Digite 0 para cancelar")
        id_entregador = input("Digite o Id do entregador: ")
        if id_entregador == "0":
            return
        

    lista = [nome_cliente, endereco, prioridade, descricao, status, id_pedido, id_entregador]
    print(f"\n[Pedido Cadastrado com Sucesso!]")
    input(f"Pressione Enter para voltar ")
    return lista


def cadastro_entregador(lista_entregadores):
    limpar_tela()
    print(f"==== CADASTRO DE ENTREGADOR ====\n")

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
            print(f"\nSelecione uma das opções: ")
            veiculo=None
    
    id_entregador = input("\nDigite o ID do entregador (4 dígitos): ")
    while not verificacoes.validar_id_ent(lista_entregadores, id_entregador):
        print(f"\nO ID do Entregador deve ser Original e conter 4 Dígitos")
        id_entregador = input("Digite o ID do entregador (4 dígitos): ")      

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
    

    lista = [nome_entregador, veiculo, id_entregador, disponibilidade]
    print(f"\n[Entregador Cadastrado com Sucesso!]")
    input(f"Pressione Enter para voltar ")
    return lista


def listar_entregadores(lista_ent):
    limpar_tela()

    if len(lista_ent) == 0:
            print(f"[Nenhum entregador cadastrado]\n")
            return

    for i in range(len(lista_ent)):

        nome= lista_ent[i][0]
        veiculo= lista_ent[i][1]
        id_entregador= lista_ent[i][2]
        disponibilidade= lista_ent[i][3]
        print(f"{i+1}| {nome} - Id: {id_entregador} - Veículo: {veiculo} - Disponibilidade: {disponibilidade}")
        


def listar_pedidos(lista_pedidos, lista_entregadores):
    limpar_tela()

    if len(lista_pedidos) == 0:
        print(f"[Nenhum pedido cadastrado]\n")
        return

    for i in range(len(lista_pedidos)):
        prioridade = lista_pedidos[i][2]
        nome = lista_pedidos[i][0]
        endereco = lista_pedidos[i][1]
        descricao = lista_pedidos[i][3]
        status = lista_pedidos[i][4]
        id_pedido = lista_pedidos[i][5]
        id_entregador = lista_pedidos[i][6]

        for j in range(len(lista_entregadores)):
            if id_entregador == lista_entregadores[j][2]:
                entregador = lista_entregadores[j][0]
                break

        print(f"{prioridade}| ({id_pedido}) {nome} - Endereço: {endereco} - Descrição: {descricao} - Status: {status} - Entregador: {entregador} ({id_entregador})")

def consultar_pedidos(lista_pedidos):
    limpar_tela()
    print(f"==== CONSULTA DE PEDIDO ====\n")
    print(f"0 - Voltar")
    id_pedido = input("Digite o ID do pedido: ")

    if id_pedido == "0":
        return "VOLTAR"

    for i in range(len(lista_pedidos)):
        if id_pedido == lista_pedidos[i][5]:
            prioridade = lista_pedidos[i][2]
            nome = lista_pedidos[i][0]
            endereco = lista_pedidos[i][1]
            descricao = lista_pedidos[i][3]
            status = lista_pedidos[i][4]
            id_entregador = lista_pedidos[i][6]

            return (f"\n{prioridade}| ({id_pedido}) {nome} - Endereço: {endereco} - Descrição: {descricao} - Status: {status} - Id do Entregador: {id_entregador}")
        
    print(f"\n[Pedido não encontrado]")
    input(f"Pressione Enter para voltar ")
    return None


def alt_status(lista_pedidos):
    print(f"==== ALTERAÇÃO DE STATUS ====\n")
    qntd_pedidos = None
    while qntd_pedidos == None:
        q = input(f"Quantos pedidos deseja alterar o status: ")
        if not q.isdigit() or q<0:
            print(f"\nDigite um número válido")
            qntd_pedidos = None
        elif q == "0":
            return
        else:
            qntd_pedidos = int(q)
    
    pedidos_a_consultar = []
    for i in range(qntd_pedidos):
        id_pedido = input(f"\nDigite o ID do pedido ({i+1}): ")
        for j in range(len(lista_pedidos)):
            if id_pedido == lista_pedidos[j][5]:
                pedidos_a_consultar.append(id_pedido)
                break
            else:
                print(f"\n[Pedido Não Encontrado]")
                o = input(f"Insira o ID do pedido novamente - ou Digite 0 para seguir\n")
                if o == "0":
                    return
                else:
                    id_pedido = input(f"Digite o ID do pedido ({i+1}): ")
    


            
    

            


def cancel_pedido(lista_pedidos):
    limpar_tela()
    id_pedido=input("Insira o ID do Pedido: ")
    for i in range(len(lista_pedidos)):
        if id_pedido == lista_pedidos[i][5]:
            
            opcao=None
            while opcao == None:
                o=input(f"\nDeseja cancelar o seguinte pedido?\n {lista_pedidos[i]} - S/N: ")
                if(o=="S" or o=="s"):
                    lista_pedidos[i][4] = "Cancelado"
                    return
                elif(o=="N" or o=="n"):
                    return
                else:
                    opcao=None
        else:
            print(f"\n[Pedido Não Encontrado]")
            o = input(f"Insira o ID do pedido novamente - ou Digite 0 para cancelar\n")
            if o == "0":
                return
            else:
                cancel_pedido(lista_pedidos)


def remover_ent(lista_pedidos, lista_entregadores):
    limpar_tela()
    id_pedido=input("Insira o ID do Pedido: ")
    for i in range(len(lista_pedidos)):
        if id_pedido == lista_pedidos[i][5]:

            id_entregador = lista_pedidos[i][6]
            for j in range(len(lista_entregadores)):
                if id_entregador == lista_entregadores[j][2]:
                    entregador = lista_entregadores[j][0]
                    
                    opcao=None
                    while opcao==None:
                        o = input(f"\nVocê deseja remover {entregador}(id:{id_entregador}) do Pedido {id_pedido}?\n - S/N: ")
                        if o == 'S' or o == 's':
                            lista_pedidos[i][6] = "Nenhum Entregador"
                            print("Entregador removido com sucesso!")
                            input("Pressione Enter para continuar ")
                            return
                        elif o == 'N' or o == 'n':
                            print("Operação cancelada.")
                            input("Pressione Enter para voltar ")
                            return
                        else:
                            opcao=None

                else:
                    print(f"\n[Entregador Não Encontrado]")
                    p = input(f"Tentar Novamente - ou Digite 0 para cancelar\n")
                    if p == "0":
                        return
                    else:
                        remover_ent(lista_pedidos, lista_entregadores)
                
        else:
            print(f"\n[Pedido Não Encontrado]")
            o = input(f"Insira o ID do pedido novamente - ou Digite 0 para cancelar\n")
            if o == "0":
                return
            else:
                remover_ent(lista_pedidos, lista_entregadores)


def ass_entregador(lista_pedidos, lista_entregadores):
    limpar_tela()
    id_pedido=input("Insira o ID do pedido: ")
    for i in range(len(lista_pedidos)):
        if id_pedido == lista_pedidos[i][5]:

            id_entregador = lista_pedidos[i][6]
            for j in range(len(lista_entregadores)):
                if id_entregador == lista_entregadores[j][2]:
                    print(f"\nEntregador Atual: {lista_entregadores[j][0]}")
                    print(f"ID: {lista_entregadores[j][2]}")

                    n_id=int(input(f"\nInsira o ID do Novo Entregador: "))
                    lista_pedidos[i][6] = n_id
                    return

                else:
                    print(f"\n[Entregador Não Encontrado]")
                    o = input("Tentar Novamente - ou Digite 0 para cancelar\n")
                    if o == "0":
                        return
                    else:
                        ass_entregador(lista_pedidos, lista_entregadores)
        else:
            print(f"\n[Pedido Não Encontrado]")
            p = input(f"Insira o ID do pedido novamente - ou Digite 0 para cancelar\n")
            if p == "0":
                return
            else:
                ass_entregador(lista_pedidos, lista_entregadores)
