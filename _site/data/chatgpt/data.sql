DROP TABLE IF EXISTS produtos;
CREATE TABLE produtos (
  id SERIAL PRIMARY KEY,
  nome_do_produto VARCHAR(100),
  categoria VARCHAR(50),
  data_de_compra DATE,
  tempo_de_garantia INTEGER,
  tempo_de_garantia_estendida INTEGER,
  total_de_garantia INTEGER,
  data_final_da_garantia DATE,
  preco_unitario NUMERIC(10, 2),
  preco_com_desconto NUMERIC(10, 2),
  preco_liquido NUMERIC(10, 2),
  quantidade INTEGER,
  preco_final NUMERIC(10, 2),
  preco_da_garantia_estendida NUMERIC(10, 2),
  preco_final_com_garantia_estendida NUMERIC(10, 2)
);

INSERT INTO produtos (nome_do_produto, categoria, data_de_compra, tempo_de_garantia, tempo_de_garantia_estendida, preco_unitario, preco_com_desconto, quantidade, preco_da_garantia_estendida)
VALUES
  ('Notebook Lenovo IdeaPad 3', 'Eletrônicos', '2022-02-12', 365, 365, 2599.99, 2349.99, 1, 399.99),
  ('Smartphone Samsung Galaxy S21', 'Eletrônicos', '2022-01-01', 365, 0, 4999.99, 4499.99, 1, 0),
  ('Smartwatch Apple Watch Series 7', 'Eletrônicos', '2022-03-15', 365, 365, 3499.99, 3149.99, 1, 349.99),
  ('TV Samsung QLED Q80A', 'Eletrônicos', '2022-02-28', 365, 365, 9999.99, 8999.99, 1, 599.99),
  ('Fogão Brastemp 5 bocas', 'Eletrodomésticos', '2022-03-10', 365, 0, 1999.99, 1799.99, 1, 0),
  ('Geladeira Electrolux Frost Free', 'Eletrodomésticos', '2022-01-20', 365, 0, 3699.99, 3329.99, 1, 0),
  ('Cama Box Queen Ortobom', 'Móveis', '2022-02-05', 365, 365, 2799.99, 2519.99, 1, 299.99),
  ('Sofá Retrátil e Reclinável Conforto', 'Móveis', '2022-03-01', 365, 365, 3999.99, 3599.99, 1, 499.99),
  ('Mesa de Jantar com 6 Cadeiras', 'Móveis', '2022-01-15', 365, 0, 4999.99, 4499.99, 1, 0),
  ('Bicicleta Caloi Elite', 'Esportes', '2022-02-20', 365, 365, 3999.99, 3599.99, 1, 299.99);
