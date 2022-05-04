# Cardapio-Python
Primeira tentativa de aprender a mexer no Github e poder fazer upload de tudo o que eu tenho feito até agora.

A ideia desse script é facilitar a vida na hora de escolher as refeições principais (café, almoço e janta),facilitar o controle da quantidade dos ingredientes necessários para cada prato, além de agilizar a montagem da lista de compras, recebendo a lista diretamente no celular.

--------------------------------- Estrutura dos dados ---------------------------------

cada uma das refeições é composta por uma lista de dicionários, cada um desses dicionários representa um prato daquela
refeição. Dentro de cada dicionário temos três duplas de chave:valor

ex:
jantar = [ {'nome': nome do prato em snake_case, 'ingredientes': [lista de ingredientes que compõe o prato],
'quantidades' : {'ingrediente': quantidade de cada ingrediente}}]

A partir dessa estrutura de dados serão sorteados os pratos que compoem as refeições da semana (ou do mês, a ver...).

Uma vez sorteadas as refeições, será possivel extrair delas os ingredientes e as quantidades (qtd ainda não implementadas).

Outra possibilidade de uso desse script que ainda quero implementar é poder escolher um ingrediente e filtrar somente os pratos que tem aquele ingrediente
nas lista de ingredientes.


