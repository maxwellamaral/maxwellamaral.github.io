---
layout: home
author_profile: true
title: Escrevendo histórias de usuários
permalink: /lessons/softeng/tests/user_stories/
sidebar:
    nav: "softeng-tests"
---
Criado em Março de 2023 por *Maxwell Anderson*

<center>
    <figure>
        <img src="../../../../assets/images/gpt/cat_tdd2.jpg" alt="Gato engenheiro de software que está realizando testes automatizados">
        <figcaption>
            Gato engenheiro de software que está realizando testes automatizados.<br>
            <em>Prompt: create an image of a software engineer cat that is performing automated tests</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

Histórias de usuários em TDD são histórias que são escritas de forma a serem testadas. A ideia é que os testes sejam escritos de forma a falhar, e então o código é escrito de forma a fazer os testes passarem.

Antes de criar as histórias de usuários, é necessário entender o que é um usuário. Um usuário é uma pessoa que utiliza o sistema. Um usuário pode ser um cliente, um funcionário, um fornecedor, etc. Um usuário pode ter diferentes perfis, e cada perfil pode ter diferentes permissões. Por exemplo, um usuário pode ser um cliente, e ter permissão para criar uma garantia, mas não pode ter permissão para criar um produto. Um usuário pode ser um funcionário, e ter permissão para criar um produto, mas não pode ter permissão para criar uma garantia.

Vamos utilizar o projeto que se encontra em <https://github.com/maxwellamaral/garantias-mono-dj> como exemplo, partindo das modificações a serem realizadas na branch **aula01**.

Antes de escrevermos a primeira história de usuário é necessário entender os requisitos que se encontram no [Documento de Requisitos](/lessons/softeng/requirements/req/sample/) validado junto ao cliente. Digamos que a **RF001** foi a primeira a ser priorizada pelo cliente, e que o cliente deseja que seja implementada o mais rápido possível. A RF001 é a seguinte:

> RF001 - Como um cliente, eu gostaria de poder cadastrar os produtos que eu compro e controlar as garantias, para que eu possa saber quando o produto estará fora de garantia. Os produtos devem ser cadastrados com os seguintes dados: nome do produto, data de compra, data de vencimento da garantia, segmento do produto, marca e modelo do produto, local de compra, valor pago pelo produto, valor da garantia e modo de compra (online ou físico).

Entendeu a necessidade do cliente? Vamos escrever a primeira história de usuário que seja testável por um humano. Vamos escrevê-la usando comentários em Python. Vamos chamar o cliente de Max.

Crie uma pasta chamada `funcional_tests` na raiz do projeto. Crie os arquivos conforme ilustrado abaixo:

```bash
📦functional_tests
 ┣ 📜__init__.py
 ┗ 📜tests.py
```

No arquivo `tests.py`, crie a primeira história de usuário. Ela será a seguinte:

```python
# Max acessa a página de cadastro de produtos.

# Ele verifica que o título da página na aba do navegador e
# na própria página é "Cadastro de produtos".

# Ele verifica que existe um campo para o nome do produto, 
# data de compra, data de vencimento da garantia, segmento do produto,
# marca e modelo do produto, local de compra, valor pago pelo produto, 
# valor da garantia e modo de compra (online ou físico).

# Ele verifica que existe um botão para cadastrar o produto. 

# Ele preenche os campos com os dados do produto que ele deseja cadastrar e 
# clica no botão para cadastrar o produto. 

# Ele verifica que a página de cadastro de produtos é exibida novamente, 
# e que existe uma mensagem informando que o produto foi 
# cadastrado com sucesso.
```

Agora, vamos escrever o código que fará os testes falharem. Em `tests.py` escreva o seguinte código:

```python
# ... 
# Ele verifica que a página de cadastro de produtos é exibida novamente, 
# e que existe uma mensagem informando que o produto foi 
# cadastrado com sucesso.


```
