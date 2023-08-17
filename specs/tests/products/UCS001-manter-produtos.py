'''
UC001 - Manter produtos

Objetivo: Permitir que o cliente possa cadastrar, alterar, excluir e consultar produtos.

Requisitos: 
- RF001

Ator:
- Cliente
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de cadastro de produtos. Ele verifica que o 
# título da página é "Cadastro de produtos". Ele observa que existe os
# campos:
# - Nome
# - Data de compra
# - Segmento
# - Marca
# - Modelo
# - Local de compra
# - Valor pago
# - Modo de compra (online ou loja física)
# - Listagem de garantias
# - Data de vencimento da garantia
# - Tipo de garantia
# - Valor da garantia
# - Opções
# -- Botão "Salvar"
# -- Botão "Cancelar"

# O ator preenche os campos com os dados do produto. Verifica também que existe
# a data de vencimento, tipo e o valor da garantia em uma lista
# em branco, onde será possível cadastrar mais de um tipo de garantia. Desta forma
# ele preenche o valor, o tipo 'original' e a data de vencimento. [A4]

# Ao concluir o cadastro, ele seleciona a opção "Salvar". [A2][A3] 
 
# O sistema verifica que os dados estão corretos [RN1]

# O sistema exibe a página de cadastro de produtos novamente e exibe uma
# mensagem de sucesso.

# O ator seleciona 'Consultar' no menu.

# O sistema exibe a página de listagem de produtos.

# O ator verifica que o produto cadastrado está na lista.


# 🟠 [A1] - BUSCAR PRODUTO
# ---------------------------------------------------------------

# O ator necessita realizar uma busca por produtos na lista. 
# Ele acessa a página "Listar produto"

# O sistema exibe a página de listagem de produtos.

# Seleciona o campo específico para busca e digita o nome do produto.

# O ator selecionar 'Pesquisar'.

# O sistema exibe todos os produtos que correspondem aos termos 
# que foram digitados.


## 🟠 [A2] EDITAR PRODUTO
# ---------------------------------------------------------------
# O ator executa [A1].

# O ator seleciona o produto na lista e clica no botão 
# para editar o produto.

# Sistema exibe a página de edição de produtos e que os campos 
# estão preenchidos com os dados do produto.

# O ator altera o nome do produto e clica no botão para salvar 
# os dados relacionados ao produto.

# Sistema salva os dados.

# O ator seleciona 'Listar produtos' no menu.

# O sistema exibe uma a lista de produtos cadastrados.

# O ator verifica que o produto cadastrado está na lista.

# 🟠 [A3] EXCLUIR PRODUTO
# ---------------------------------------------------------------

# O ator decide excluir o produto e executa [A1]. 
# Ele visualiza o produto e seleciona a opção 'Excluir'.

# O sistema pergunta se o usuário realmente deseja excluir o produto.

# O ator confirma a exclusão.

# O sistema exclui o produto.

# O ator seleciona 'Listar produtos' no menu.

# O sistema exibe uma a lista de produtos cadastrados.

# O ator verifica que o produto cadastrado não está na lista.

# 🟠 [A4] ADICIONAR GARANTIA
# ---------------------------------------------------------------

# O ator decide adicionar mais uma garantia ao produto. Ele verifica que 
# existe um botão para adicionar garantia e o seleciona

# O sistema exibe novos campos para adicionar a garantia. 

# O ator preenche os campos com os dados da nova garantia: valor, tipo 'estendida'e data de vencimento.

# 🟣 [RN1] VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Todas as informações são obrigatórias, exceto o campo 'valor da garantia'

