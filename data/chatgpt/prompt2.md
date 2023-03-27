Crie uma tabela para armazenar informações sobre os produtos de uma loja. A tabela deve ter as seguintes colunas:

- id: identificador único do produto (inteiro, chave primária)
- nome: nome do produto (texto)
- categoria: categoria do produto (texto)
- data_compra: data em que o produto foi comprado (data)
- tempo_garantia: tempo de garantia do produto em dias (inteiro)
- tempo_garantia_estendida: tempo de garantia estendida do produto em dias (inteiro)
- total_garantia: tempo total de garantia do produto em dias (inteiro)
- data_fim_garantia: data em que a garantia do produto expira (data)
- preco_unitario: preço unitário do produto (numérico com duas casas decimais)
- preco_desconto: valor do desconto aplicado ao produto (numérico com duas casas decimais)
- preco_liquido: preço líquido do produto (preco_unitario - preco_desconto) (numérico com duas casas decimais)
- quantidade: quantidade de unidades do produto compradas (inteiro)
- preco_final: preço final do produto (preco_liquido * quantidade) (numérico com duas casas decimais)
- preco_garantia_estendida: preço da garantia estendida do produto (numérico com duas casas decimais)
- preco_final_garantia: preço final do produto com a garantia estendida (preco_final + preco_garantia_estendida) (numérico com duas casas decimais)

Preencha a tabela com informações de pelo menos 5 produtos.