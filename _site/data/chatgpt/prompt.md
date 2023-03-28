# Tabela com prompts utilizados no chatGPT

1. Crie uma tabela em markdown com os seguintes campos:
    * Nome do produto
    * Categoria
    * Data de compra (no formato aaaa-mm-dd)
    * Tempo de garantia (em dias)
    * Tempo de garantia estendida (em dias)
    * Total de garantia (em dias)
    * Data final da garantia (no formato aaaa-mm-dd)
    * Preço unitário (em formato americano de numeração decimal, sem cifrão)
    * Preço com desconto (em formato americano de numeração decimal, sem cifrão)
    * Preço líquido (em formato americano de numeração decimal, sem cifrão)
    * Quantidade
    * Preço final (em formato americano de numeração decimal, sem cifrão)
    * Preço da garantia estendida (em formato americano de numeração decimal, sem cifrão)
    * Preço final com garantia estendida (em formato americano de numeração decimal, sem cifrão)
  
    Calcule os valores dos campos "Total de garantia", "Data final da garantia", "Preço líquido", "Preço final" e "Preço final com garantia estendida" seguindo as instruções abaixo:

      * Total de garantia = tempo de garantia + tempo de garantia estendida
      * Data final da garantia = data de compra + total de garantia
      * Preço líquido = preço unitário - preço com desconto
      * Preço final = preço líquido * quantidade
      * Preço final com garantia estendida = preço final + preço da garantia estendida

    Insira pelo menos 10 produtos na tabela.

2. Converta a tabela em markdown para um arquivo CSV. Faça a lista completa de todos os produtos.
3. Converta a tabela em markdown para um arquivo JSON. Faça a lista completa de todos os produtos.
4. Converta a tabela em markdown para um arquivo XML. Faça a lista completa de todos os produtos.
5. Converta a tabela em markdown para um arquivo YAML. Faça a lista completa de todos os produtos.
6. Converta a tabela em markdown para um arquivo TOML. Faça a lista completa de todos os produtos.
7. Converta a tabela em markdown para um arquivo de script SQL para Postgresql. Faça a lista completa de todos os produtos.



