"""
A ideia desse script é facilitar a vida na hora de escolher as refeições principais (café almoço e janta)
e também de facilitar o controle da quantidade dos ingredientes necessários para cada prato.

Estrutura dos dados:

cada uma das refeições é composta por uma lista de dicionários, cada um desses dicionários representa um prato daquela
refeição. Dentro de cada dicionário temos três duplas de chave:valor

ex:
jantar = [ {'nome': nome do prato em snake_case, 'ingredientes': [lista de ingredientes que compõe o prato],
'quantidades' : {'ingrediente': quantidade de cada ingrediente}}]

A partir dessa estrutura de dados serão sorteados os pratos que compoem as refeições da semana (ou do mês, a ver...).

Uma vez sorteadas as refeições, será possivel extrair delas os ingredientes e as quantidades.

Outra possibilidade de uso desse script é escolher um ingrediente e filtrar somente os pratos que tem aquele ingrediente
nas lista de ingredientes.

As bibliotecas de refeição são: almoco, janta, cafe

prato: compostos por ingredientes:quantidade e nome, fazem parte do banco de dados de cada uma das refeições


padrão de escrita dos ingredientes:


"""
from random import(randint)

almoco = [{'nome': 'lasanha_de_carne', 'quantidades': {'massa': '200g','molho de tomate':'300ml', 'carne moida': '300g',
        'queijo mussarela': '300g','requeijão': '100g' ,'oregano': 'a gosto'}},
         {'nome': 'lasanha_de_frango','quantidades': {'massa': '200g','molho de tomate':'300ml', 'peito de frango': '300g',
        'queijo mussarela': '300g','requeijão': '100g' ,'oregano': 'a gosto'}},
         {'nome': 'carne','quantidades': {'massa': '200g', 'molho de tomate': '300ml', 'carne moida': '300g',
         'queijo mussarela': '300g', 'requeijão': '100g', 'oregano': 'a gosto'}},
         {'nome': 'frango','quantidades': {'massa': '200g', 'molho de tomate': '300ml', 'peito de frango': '300g',
         'queijo mussarela': '300g', 'requeijão': '100g', 'oregano': 'a gosto'}},
         {'nome': 'lasanha','quantidades': {'massa': '200g', 'molho de tomate': '300ml', 'carne moida': '300g',
         'queijo mussarela': '300g', 'requeijão': '100g', 'oregano': 'a gosto'}},
         {'nome': 'de','quantidades': {'massa': '200g', 'molho de tomate': '300ml', 'peito de frango': '300g',
         'queijo mussarela': '300g', 'requeijão': '100g', 'oregano': 'a gosto'}}
         ]


#
def sorteio(num_ref,refeicao):
    """
    Essa função faz o processo de sorteio de cada um dos pratos que serão utilizados

    :param num_ref: número inteiro de refeições a serem sorteadas
    :param refeicao: uma das listas (almoço ou jantar) a serem utilizadas para o sorteio
    :return: a lista das refeições já sorteadas
    """
    lista_sorteio = []
    while len(lista_sorteio) < num_ref:
        prato = refeicao[randint(0, (len(refeicao)-1))]
        if prato not in lista_sorteio:
            lista_sorteio.append(prato)
        else:
            pass
    return lista_sorteio


def impressao_sorteio(lista):
    """ função simples só pra imprimir cada prato separadamente"""
    contador = 1
    for i in lista:
        print(f" O {contador}º prato sorteado foi {i['nome']}, que tem os seguintes ingredientes {i['quantidades'].keys()}")
        contador+=1


# todo encontrar uma forma de mostrar em quais pratos os dois ingredientes estão presentes


def ingrediente(refeicao,*args):
    """
    :param refeicao: lista contendo os pratos
    :param args: quais ingredientes se está procurando
    :return: lista dos pratos que contem aquele ingrediente
    """
    lista_ingredientes = []
    for j in args:
        for i in refeicao:
            if j in i['quantidades'].keys():
                print(f" O prato '{i['nome']}' tem o ingrediente '{j}' na lista de ingredientes. "
                      f"Esse são todos os ingredientes desse prato -> {list(i['quantidades'].keys())}")
                lista_ingredientes.append(i)
            else:
                pass
    if len(lista_ingredientes) ==0:
        print(f'O(s) ingrediente(s) {args} não está(ão) em nenhuma refeição da lista escolhida')


def lista_compras(lista):
    """
    :param lista: resultado do sorteio de pratos daquela semana
    :return: lista de compras com um set dos ingredientes que precisam ser comprados para fazer os pratos sorteados
    """
    lista_unica =[]
    for prato in lista:
        lista_unica += list(prato['quantidades'].keys())
    return list(set(lista_unica))

