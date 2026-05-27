
def verificar_ent(lista_entregadores, id_entregador):
    for i in range(len(lista_entregadores)):
        if id_entregador == lista_entregadores[i][2]:
            return True
    return False

def validar_id_ent(lista_entregadores, id_entregador):

    if len(id_entregador) != 4 or not id_entregador[:].isdigit():
        return False
    
    for i in range(len(lista_entregadores)):
        if id_entregador == lista_entregadores[i][2]:
            return False
            
    return True

def validar_id_pedido(lista_pedidos, id_pedido):

    if len(id_pedido) != 5 or not id_pedido[0].isalpha() or not id_pedido[1:].isdigit():
        return False

    for i in range(len(lista_pedidos)):
        if id_pedido == lista_pedidos[i][5]:
            return False
    
           
    return True