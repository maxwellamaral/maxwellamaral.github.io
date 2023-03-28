# -*- coding: utf-8 -*-

"""
Gera dados aleatórios para o arquivo de entrada.
Cria os arquivos com dados para os seguintes formatos de dados:
- CSV
- JSON
- XML
- Excel
- PostgreSQL

Para executar o script, execute o seguinte comando no terminal:
python gerarDados.py

Criado por: Maxwell Anderson Ielpo do Amaral
Data: 2019-10-01
Versão 1.0.0
Licença: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import random

from datetime import datetime, timedelta
from faker import Faker
import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)


class Product:
    """
    Produto
    """

    def __init__(
        self,
        name: str,
        category: str = None,
        date: datetime = datetime.now(),
        warranty_days: int = 365,
        extended_warranty_days: int = 0,
        price: float = 0.0,
        discount: float = 0.0,
        quantity: int = 1,
        extended_warranty_price: float = 0.0,
    ):
        # Nome do produto
        self.name = name
        # Categoria do produto
        self.category = category
        # Data de compra
        self.date = date
        # Dias de garantia
        self.warranty_days = warranty_days
        # Dias de garantia estendida
        self.extended_warranty_days = extended_warranty_days
        # Preço
        self.price = price
        # Desconto
        self.discount = discount
        # Quantidade
        self.quantity = quantity
        # Preço da garantia estendida
        self.extended_warranty_price = extended_warranty_price

    @property
    def date_final(self) -> datetime.date:
        """
        Data final da garantia
        :return: Data final da garantia
        """
        return (
            self.date
            + timedelta(days=self.warranty_days)
            + timedelta(days=self.extended_warranty_days)
        )

    @property
    def price_liquid(self) -> float:
        """
        Preço líquido
        :return: Preço líquido
        """
        return self.price - self.discount

    @property
    def price_final(self) -> float:
        """
        Preço final
        :return: Preço final
        """
        return self.price_liquid * self.quantity

    @property
    def extended_warranty_price_final(self) -> float:
        """
        Preço final com garantia estendida
        :return: Preço final com garantia estendida
        """
        return self.price_final + self.extended_warranty_price

    def __str__(self):
        """
        Representação textual do produto
        :return: Representação textual do produto
        """
        return (
            f"Nome: {self.name}\n"
            f"Categoria: {self.category}\n"
            f"Data de compra: {self.date}\n"
            f"Data de final da garantia: {self.date_final}\n"
            f"Preço: {self.price}\n"
            f"Desconto: {self.discount}\n"
            f"Preço líquido: {self.price_liquid}\n"
            f"Preço final: {self.price_final}\n"
            f"Quantidade: {self.quantity}\n"
            f"Preço da garantia estendida: {self.extended_warranty_price}\n"
            f"Preço final com garantia estendida: {self.extended_warranty_price_final}\n"
        )


class DataGenerator:
    """
    Gerador de dados aleatórios
    """

    def __init__(self, seed: int = None):
        """
        Inicialização
        :param seed: Semente para a geração de números aleatórios
        """
        # Gera números aleatórios
        self.random = random.Random(seed)
        # Gera dados aleatórios
        # Datas de compra
        self.dates = []
        # Dias de garantia
        self.warranty_days = []
        # Dias de garantia estendida
        self.extended_warranty_days = []
        # Preços
        self.prices = []
        # Descontos
        self.discounts = []
        # Quantidades
        self.quantities = []
        # Preços da garantia estendida
        self.extended_warranty_prices = []

    def generate(self, n: int = 1):
        """
        Gera dados aleatórios
        :param n: Número de dados a serem gerados
        :return: Dados gerados
        """
        # Gera dados aleatórios
        self.dates = [
            datetime(
                self.random.randint(2010, 2019),
                self.random.randint(1, 12),
                self.random.randint(1, 28),
            )
            for _ in range(n)
        ]
        self.warranty_days = [self.random.choice([90, 180, 365]) for _ in range(n)]
        self.extended_warranty_days = [
            self.random.choice([365, 365 * 2, 365 * 3, 365 * 4]) for _ in range(n)
        ]
        self.prices = [self.random.uniform(100, 10000) for _ in range(n)]
        self.discounts = [self.random.uniform(0, 50) for _ in range(n)]
        self.quantities = [self.random.randint(1, 10) for _ in range(n)]
        self.extended_warranty_prices = [self.random.uniform(10, 100) for _ in range(n)]

        return [
            Product(
                fake.ecommerce_name(),
                fake.ecommerce_category(),
                self.dates[i],
                self.warranty_days[i],
                self.extended_warranty_days[i],
                self.prices[i],
                self.discounts[i],
                self.quantities[i],
                self.extended_warranty_prices[i],
            )
            for i in range(n)
        ]

    def generate_excel_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo do Excel
        :param n: Número de dados a serem gerados
        """
        # Salva os dados em um arquivo do Excel
        import xlsxwriter

        workbook = xlsxwriter.Workbook("data.xlsx")
        worksheet = workbook.add_worksheet()

        # Escreve os dados com o cabeçalho
        worksheet.write(0, 0, "Nome")
        worksheet.write(0, 1, "Data de compra")
        worksheet.write(0, 2, "Data de final da garantia")
        worksheet.write(0, 3, "Preço")
        worksheet.write(0, 4, "Desconto")
        worksheet.write(0, 5, "Preço líquido")
        worksheet.write(0, 6, "Preço final")
        worksheet.write(0, 7, "Quantidade")
        worksheet.write(0, 8, "Preço da garantia estendida")
        worksheet.write(0, 9, "Preço final com garantia estendida")
        worksheet.write(0, 10, "Quantidade de dias de garantia")
        worksheet.write(0, 11, "Quantidade de dias de garantia estendida")
        worksheet.write(0, 12, "Categoria")
        for i, product in enumerate(products):
            worksheet.write(i + 1, 0, product.name)            
            worksheet.write(i + 1, 1, product.date)
            worksheet.write(i + 1, 2, product.date_final)
            worksheet.write(i + 1, 3, product.price)
            worksheet.write(i + 1, 4, product.discount)
            worksheet.write(i + 1, 5, product.price_liquid)
            worksheet.write(i + 1, 6, product.price_final)
            worksheet.write(i + 1, 7, product.quantity)
            worksheet.write(i + 1, 8, product.extended_warranty_price)
            worksheet.write(i + 1, 9, product.extended_warranty_price_final)
            worksheet.write(i + 1, 10, product.warranty_days)
            worksheet.write(i + 1, 11, product.extended_warranty_days)
            worksheet.write(i + 1, 12, product.category)
            
        # Formata os campos de data
        date_format = workbook.add_format({"num_format": "dd/mm/yyyy"})
        worksheet.set_column(1, 2, 15, date_format)
        
        # Formata os campos de preço
        price_format = workbook.add_format({"num_format": "#,##0.00"})
        worksheet.set_column(3, 9, 15, price_format)
        
        # Formata os campos de quantidade
        quantity_format = workbook.add_format({"num_format": "#,##0"})
        worksheet.set_column(7, 7, 15, quantity_format)
        
        # Formata os campos de dias
        days_format = workbook.add_format({"num_format": "#,##0"})
        worksheet.set_column(10, 11, 15, days_format)

        workbook.close()

    def generate_xml_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo XML
        :param n: Número de dados a serem gerados
        """

        # Salva os dados em um arquivo XML
        import xml.etree.ElementTree as ET

        root = ET.Element("root")
        for product in products:
            product_xml = ET.SubElement(root, "product")
            # Adiciona os dados do produto
            ET.SubElement(product_xml, "name").text = product.name
            # Adiciona a categoria do produto
            ET.SubElement(product_xml, "category").text = product.category
            # Adiciona a data de compra no formato ISO 8601
            ET.SubElement(product_xml, "date").text = product.date.isoformat()
            # Adiciona a data de final da garantia no formato ISO 8601
            ET.SubElement(product_xml, "date_final").text = product.date_final.isoformat()
            # Adiciona o preço do produto no formato de moeda
            ET.SubElement(product_xml, "price").text = f"{product.price:.2f}"
            # Adiciona o desconto do produto no formato de moeda
            ET.SubElement(product_xml, "discount").text = f"{product.discount:.2f}"
            # Adiciona o preço líquido do produto no formato de moeda
            ET.SubElement(product_xml, "price_liquid").text = f"{product.price_liquid:.2f}"
            # Adiciona o preço final do produto no formato de moeda
            ET.SubElement(product_xml, "price_final").text = f"{product.price_final:.2f}"            
            # Adiciona a quantidade do produto no formato de número inteiro
            ET.SubElement(product_xml, "quantity").text = f"{product.quantity:.0f}"
            # Adiciona o preço da garantia estendida no formato de moeda
            ET.SubElement(product_xml, "extended_warranty_price").text = f"{product.extended_warranty_price:.2f}"
            # Adiciona o preço final com a garantia estendida no formato de moeda
            ET.SubElement(product_xml, "extended_warranty_price_final").text = f"{product.extended_warranty_price_final:.2f}"
            # Adiciona a quantidade de dias de garantia no formato de número inteiro
            ET.SubElement(product_xml, "warranty_days").text = f"{product.warranty_days:.0f}"
            # Adiciona a quantidade de dias de garantia estendida no formato de número inteiro
            ET.SubElement(product_xml, "extended_warranty_days").text = f"{product.extended_warranty_days:.0f}"

        # Salva o arquivo XML
        tree = ET.ElementTree(root)
        tree.write("data.xml")

    def generate_csv_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo CSV
        :param n: Número de dados a serem gerados
        """

        # Salva os dados em um arquivo CSV
        with open("data.csv", "w") as file:
            file.write(
                "Nome,Categoria,Data de compra,Data de final da garantia,Preço,Desconto,Preço líquido,Preço final,Quantidade,Preço da garantia estendida,Preço final com garantia estendida,Quantidade de dias de garantia,Quantidade de dias de garantia estendida\n"
            )
            for product in products:
                file.write(
                    f"{product.name},{product.category},{product.date},{product.date_final},{product.price:.2f},{product.discount:.2f},{product.price_liquid:.2f},{product.price_final:.2f},{product.quantity:.0f},{product.extended_warranty_price:.2f},{product.extended_warranty_price_final:.2f},{product.warranty_days:.0f},{product.extended_warranty_days:.0f}\n"
                )

    def generate_json_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo JSON
        :param n: Número de dados a serem gerados
        """

        # Salva os dados em um arquivo JSON
        with open("data.json", "w") as file:
            file.write("[\n")
            for i, product in enumerate(products):
                file.write(
                    f'{{"Nome": "{product.name}", "Categoria": "{product.category}", "Data de compra": "{product.date}", "Data de final da garantia": "{product.date_final}", "Preço": {product.price:.2f}, "Desconto": {product.discount:.2f}, "Preço líquido": {product.price_liquid:.2f}, "Preço final": {product.price_final:.2f}, "Quantidade": {product.quantity:.0f}, "Preço da garantia estendida": {product.extended_warranty_price:.2f}, "Preço final com garantia estendida": {product.extended_warranty_price_final:.2f}, "Quantidade de dias de garantia": {product.warranty_days:.0f}, "Quantidade de dias de garantia estendida": {product.extended_warranty_days:.0f}}}'
                )
                if i < len(products) - 1:
                    file.write(",\n")
                else:
                    file.write("\n")
            file.write("]")

    def generate_postgresql_script_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo de script do PostgreSQL
        :param n: Número de dados a serem gerados
        """
        # Cria script para criar a tabela, sobrescrevendo caso já exista
        with open("create.sql", "w") as file:
            # Insere comentário sobre o tipo de banco de dados
            file.write("-- PostgreSQL\n")
            # Insere comando para criar a tabela
            file.write("DROP TABLE IF EXISTS products;\n")
            file.write("CREATE TABLE products (\n")
            file.write("    id SERIAL PRIMARY KEY,\n")
            file.write("    name VARCHAR(255) NOT NULL,\n")
            file.write("    category VARCHAR(255) NOT NULL,\n")
            file.write("    date_purchase DATE NOT NULL,\n")
            file.write("    date_final DATE NOT NULL,\n")
            file.write("    price NUMERIC(10, 2) NOT NULL,\n")
            file.write("    discount NUMERIC(10, 2) NOT NULL,\n")
            file.write("    price_liquid NUMERIC(10, 2) NOT NULL,\n")
            file.write("    price_final NUMERIC(10, 2) NOT NULL,\n")
            file.write("    quantity INTEGER NOT NULL,\n")
            file.write("    extended_warranty_price NUMERIC(10, 2) NOT NULL,\n")
            file.write("    extended_warranty_price_final NUMERIC(10, 2) NOT NULL,\n")
            file.write("    warranty_days NUMERIC(10, 0) NOT NULL,\n")
            file.write("    extended_warpyranty_days NUMERIC(10, 0) NOT NULL\n")
            file.write(");\n")

        # Salva os dados em um arquivo de script do PostgreSQL
        with open("data.sql", "w") as file:
            # Insere comentário sobre o tipo de banco de dados
            file.write("-- PostgreSQL\n")
            # Insere comando para inserir os dados
            for product in products:
                file.write(
                    f"INSERT INTO products (name, category, date_purchase, date_final, price, discount, price_liquid, price_final, quantity, extended_warranty_price, extended_warranty_price_final) VALUES ('{product.name}', '{product.category}', '{product.date}', '{product.date_final}', {product.price:.2f}, {product.discount:.2f}, {product.price_liquid:.2f}, {product.price_final:.2f}, {product.quantity:.0f}, {product.extended_warranty_price:.2f}, {product.extended_warranty_price_final:.2f}, {product.warranty_days:.0f}, {product.extended_warranty_days:.0f});\n"
                )

    def generate_markdown_table_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo Markdown
        :param n: Número de dados a serem gerados
        """

        # Salva os dados em um arquivo Markdown
        with open("data.md", "w") as file:
            file.write("| Nome | Categoria | Data de compra | Data de final da garantia | Preço | Desconto | Preço líquido | Preço final | Quantidade | Preço da garantia estendida | Preço final com garantia estendida | Quantidade de dias de garantia | Quantidade de dias de garantia estendida |\n")
            file.write("| ---- | --------- | -------------- | ------------------------- | ----- | -------- | ------------- | ----------- | ---------- | --------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |\n")
            for product in products:
                file.write(
                    f"| {product.name} | {product.category} | {product.date} | {product.date_final} | {product.price:.2f} | {product.discount:.2f} | {product.price_liquid:.2f} | {product.price_final:.2f} | {product.quantity:.0f} | {product.extended_warranty_price:.2f} | {product.extended_warranty_price_final:.2f} | {product.warranty_days:.0f} | {product.extended_warranty_days:.0f}\n"
                )
                
    def generate_yaml_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo YAML
        :param n: Número de dados a serem gerados
        """
        # Salva os dados em um arquivo YAML
        with open("data.yml", "w") as file:
            file.write("---\n")
            for product in products:
                file.write(
                    f"- name: {product.name}\n"
                    f"  category: {product.category}\n"
                    f"  date: {product.date}\n"
                    f"  date_final: {product.date_final}\n"
                    f"  price: {product.price:.2f}\n"
                    f"  discount: {product.discount:.2f}\n"
                    f"  price_liquid: {product.price_liquid:.2f}\n"
                    f"  price_final: {product.price_final:.2f}\n"
                    f"  quantity: {product.quantity:.0f}\n"
                    f"  extended_warranty_price: {product.extended_warranty_price:.2f}\n"
                    f"  extended_warranty_price_final: {product.extended_warranty_price_final:.2f}\n"
                    f"  warranty_days: {product.warranty_days:.0f}\n"
                    f"  extended_warranty_days: {product.extended_warranty_days:.0f}\n"
                )
                
    def generate_toml_datafile(self, products: list):
        """
        Gera dados aleatórios e salva em um arquivo TOML
        :param n: Número de dados a serem gerados
        """
        # Salva os dados em um arquivo TOML
        with open("data.toml", "w") as file:
            for product in products:
                file.write(
                    f"[{product.name}]\n"
                    f"  category = '{product.category}'\n"
                    f"  date = '{product.date}'\n"
                    f"  date_final = '{product.date_final}'\n"
                    f"  price = {product.price:.2f}\n"
                    f"  discount = {product.discount:.2f}\n"
                    f"  price_liquid = {product.price_liquid:.2f}\n"
                    f"  price_final = {product.price_final:.2f}\n"
                    f"  quantity = {product.quantity:.0f}\n"
                    f"  extended_warranty_price = {product.extended_warranty_price:.2f}\n"
                    f"  extended_warranty_price_final = {product.extended_warranty_price_final:.2f}\n"
                    f"  warranty_days = {product.warranty_days:.0f}\n"
                    f"  extended_warranty_days = {product.extended_warranty_days:.0f}\n"
                )

# Inicialização
if __name__ == "__main__":

    DATA_QTY = 100    

    # Gera dados aleatórios
    data_generator = DataGenerator()

    # Gera os produtos
    products = data_generator.generate(DATA_QTY)

    # Gerador de dados aleatórios e salva em um arquivo do Excel
    data_generator.generate_excel_datafile(products)

    # Gerador de dados aleatórios e salva em um arquivo XML
    data_generator.generate_xml_datafile(products)

    # Gerador de dados aleatórios e salva em um arquivo CSV
    data_generator.generate_csv_datafile(products)

    # Gerador de dados aleatórios e salva em um arquivo JSON
    data_generator.generate_json_datafile(products)

    # Gerador de dados aleatórios e salva em um arquivo de script do PostgreSQL
    data_generator.generate_postgresql_script_datafile(products)
    
    # Gerador de dados aleatórios e salva em um arquivo Markdown
    data_generator.generate_markdown_table_datafile(products)
    
    # Gerador de dados aleatórios e salva em um arquivo YAML
    data_generator.generate_yaml_datafile(products)
    
    # Gerador de dados aleatórios e salva em um arquivo TOML
    data_generator.generate_toml_datafile(products)
    

