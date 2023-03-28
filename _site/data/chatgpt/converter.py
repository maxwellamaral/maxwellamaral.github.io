'''
Script para realizar a conversão do arquivoe 'data.csv' para os formatos:
    - 'data.json'
    - 'data.md'
    - 'data.toml'
    - 'data.yaml'
    - 'data.xml'    
'''

import csv
import json
import toml
# import yaml
import xml.etree.ElementTree as ET

# Lê o arquivo 'data.csv' e retorna uma lista de dicionários
def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Converte a lista de dicionários para o formato JSON
def to_json(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        
# Converte a lista de dicionários para o formato Markdown
def to_md(data):
    with open('data.md', 'w', encoding='utf-8') as file:
        for row in data:
            file.write(f"## {row['pergunta']}: {row['resposta']}")
            
# Converte a lista de dicionários para o formato TOML
def to_toml(data):
    with open('data.toml', 'w', encoding='utf-8') as file:
        toml.dump(data, file)
        
# # Converte a lista de dicionários para o formato YAML
# def to_yaml(data):
#     with open('data.yaml', 'w', encoding='utf-8') as file:
#         yaml.dump(data, file)
        
# Converte a lista de dicionários para o formato XML
def to_xml(data):
    root = ET.Element('root')
    for row in data:
        child = ET.SubElement(root, 'row')
        for key, value in row.items():
            ET.SubElement(child, key).text = value
    tree = ET.ElementTree(root)
    tree.write('data.xml', encoding='utf-8', xml_declaration=True)
    
# Executa a conversão
def main():
    data = read_csv()
    to_json(data)
    to_md(data)
    to_toml(data)
    # to_yaml(data)
    to_xml(data)
    
if __name__ == '__main__':
    main()
    
                       
                        
