---
title: Diagrama de sequência
permalink: /lessons/softeng/design/uml_sequences/
sidebar:
    nav: "softeng-design"

layout: single
author_profile: true
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_design03.png
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023)"
---

<center>
    <figure>
        <img src="../../../../assets/images/gpt/cat_design03.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um diagrama de atividades UML.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

# Introdução

O diagrama de sequência é um diagrama de interação que mostra como os processos operam com base em uma sequência de mensagens que são trocadas entre os objetos. Essas mensagens são métodos de classes. Ele também define a ordem em que devem ser executadas.

[![Exemplo de diagrama de sequência](https://tinyurl.com/yko3nbqm)](https://tinyurl.com/yko3nbqm)<!--![Exemplo de diagrama de sequência](../../../../assets/puml/uml_sequence01.puml)-->
<br>
<small>Exemplo de diagrama de sequência</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Você deve ler da seguinte forma:

1. Cliente insere cartão da conta através do frontend;
2. Frontend envia mensagem `numero_conta()` para o `Controlador_Banco`;
3. Controlador_Banco envia mensagem `consultar_conta()` para o objeto `ContaComum`;
4. O objeto `ContaComum` envia mensagem `true` para o `Controlador_Banco`;
5. O  `Controlador_Banco` envia mensagem `solicitar_senha()` para o frontend;
6. E assim por diante...

O que vem a ser as linhas?

Abaixo de cada elemento deve-se desenhar uma linha vertical:

- se a linha for tracejada, o objeto está inativo, isto é, não é instanciado na memória ou não atua naquele momento;
- se a linha for contínua e cheia (retângulo vertical), o objeto está ativo, onde o método do objeto está sendo executado. Quando a execução termina, ela volta a ficar tracejada.

A seta da esquerda para direita com o nome da ação ou do método indica o início da chamada.

A seta voltando da direita para a esquerda indica o retorno ou resposta da chamada.

Quando o retorno é omitido, pode significar:

1. o tipo do retorno é `void`;
2. o retorno não é relevante para que seja representado no diagrama.

Quando existe um pequeno retângulo vertical (veja no retorno `enviar_saldo()` a partir do `Controlador_Banco`), isto significa uma ativação do método.

# Referências

---. Aula 03 UML Parte01. Universidade Salvador.

Guedes, G. T. A. UML 2 Uma abordagem prática. 1ª edição. São Paulo: Novatec Editora, 2009.

Marco Tulio Valente. Engenharia de Software Moderna: Princípios e Práticas para Desenvolvimento de Software com Produtividade, Editora: Independente, 395 páginas, 2020.

Pressman, S. R. Engenharia de Software. 6ª edição. São Paulo: McGraw-Hill, 2006.

Tonsig, S. L. Engenharia de Software. Análise e Projeto de Sistemas. 1ª edição. São Paulo: Futura, 2003.

---
Criado em Junho de 2023 por *Maxwell Anderson*
