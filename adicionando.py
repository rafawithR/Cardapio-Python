
def adicionar(nome,qtd_ingredientes):
    """
    Função simples para adicionar um novo prato à lista de refeições

    :param nome: nome do prato a ser adicionado
    :param qtd_ingredientes: quantidades de ingredientes que compoem o prato que vai ser adicionado à biblioteca

    """
    ingredientes = []
    quantias = []
    cont = 0
    prato = {}
    while cont < qtd_ingredientes:
        item = input('Digite o nome do ingrediente: ')
        qtd = input('Digite a quantidade deste ingrediente: ')
        ingredientes.append(item)
        quantias.append(qtd)
        cont+=1
    prato['quantidade'] = dict(zip(ingredientes,quantias))
    prato['nome'] = nome
    return prato



