---
layout: home
author_profile: true
title: Instalando o Selenium
permalink: /lessons/softeng/intro/selenium/
sidebar:
    nav: "softeng-intro"
---
Criado em Março de 2023 por *Maxwell Anderson*

<figure>
    <img src="../../../../assets/images/gpt/cat_studying_glasses3.jpg" width="350" alt="Gato estudando usando óculos. Prompt: Create an image of a cat studying software engineering">
    <figcaption>Gato estudando Engenharia de Software.</figcaption>
    <small><strong>Fonte:</strong> gerado por IA com Bing por Maxwell Anderson (2023)<br><strong>Prompt:</strong> Create an image of a cat studying software engineering</small>
</figure>

## Introdução

O Selenium é uma ferramenta de automação de testes de software. Ele permite que você escreva testes automatizados que simulam ações de usuários em um navegador web. O Selenium é uma ferramenta muito poderosa e versátil, e é amplamente utilizada na indústria de desenvolvimento de software.

## Instalação

Realize os passos abaixo para instalar o Selenium no Windows:

- Para instalar o Selenium, abra o Terminal do Windows ou o Prompt de Comando e digite o comando abaixo:

    ```bash
    pip install selenium
    ```

- Após o término da instalação, digite o comando abaixo para verificar a versão do Selenium instalada:

    ```bash
    python -c "import selenium; print(selenium.__version__)"
    ```

Pronto! O Selenium foi instalado com sucesso no Windows.

### Instalação do driver do navegador Firefox

> Para instalação do driver do navegador, consulte a [documentação oficial](https://selenium-python.readthedocs.io/installation.html#drivers).

Para esta atividade, utilizaremos o [FirefoxDriver](https://github.com/mozilla/geckodriver/releases) disponível em https://github.com/mozilla/geckodriver/releases.

1. Se você não tiver o Firefox instalado, baixe e instale o Firefox para Windows.
2. Baixe a versão mais recente do driver e descompacte o arquivo `geckodriver.exe` na pasta `C:\Windows`. Exemplo de arquivo: geckodriver-v0.33.0-win32.zip

3. Para testar a instalação, abra o Terminal do Windows ou o Prompt de Comando e digite o comando abaixo:

    ```bash
    geckodriver --version
    ```
4. Se tudo estiver correto, você verá a versão do driver instalada. Agora vamos testar o Selenium com o Python:

    ```bash
    python -c "from selenium import webdriver; print(webdriver.__version__)"
    ```
5. Agora vamos ver o Selenium em ação com o uso de Python:

    ```bash
    python -c "from selenium import webdriver; driver = webdriver.Firefox(); driver.get('https://www.google.com'); driver.quit()"
    ```
    Ou execute o código abaixo em um arquivo python:

    ```python
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get('https://www.google.com')
    driver.quit()
    ```

6. Se tudo ocorrer bem, você verá o Firefox sendo executado, acessando o Google e fechando em seguida.



