---
layout: home
author_profile: true
title: Visões do Sistema
permalink: /lessons/softeng/design/views/
sidebar:
    nav: "softeng-design"
---
Criado em Junho de 2023 por *Maxwell Anderson*

<center>
    <figure>
        <img src="../../../../assets/images/gpt/cat_design02.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um projeto de software em UML. O gato deve estar usando roupas formais.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

## Conteúdo

- [Introdução](#introdução)
- [Visão de casos de uso](#visão-de-casos-de-uso)
  - [Diagrama de Casos de Uso](#diagrama-de-casos-de-uso)
    - [Como extrair Casos de Uso de Requisitos Funcionais?](#como-extrair-casos-de-uso-de-requisitos-funcionais)
  - [Como extrair as etapas de um Caso de Uso?](#como-extrair-as-etapas-de-um-caso-de-uso)
    - [Passos para criação de um diagrama de atividades](#passos-para-criação-de-um-diagrama-de-atividades)
    - [Diagrama de atividades UCS Manter Produtos e Garantias](#diagrama-de-atividades-ucs-manter-produtos-e-garantias)
    - [Diagrama de atividades UCS Manter Clientes](#diagrama-de-atividades-ucs-manter-clientes)

# Introdução

As visões exibem o sistema de diferentes perspectivas. Elas são usadas para representar os requisitos do sistema, a arquitetura do sistema, o projeto do sistema, etc.

Após a construção de um carro, vários especialistas podem estar envolvidos, como um especialista em mecânica, funilaria, pintura, eletrônica, etc. Cada um tem uma visão específica. O especialista em mecânica se concentra no funcionamento do motor, das rodas e no movimento do carro. O especialista em funilaria se preocupa com a montagem das peças. O especialista em pintura cuida da pintura do carro, enquanto o especialista em eletrônica se interessa pela parte elétrica e pelo funcionamento dos componentes.

Cada especialista tem sua própria perspectiva do carro e pode utilizar diferentes diagramas para representá-lo. Por exemplo, o especialista em mecânica usa um diagrama do motor, o de funilaria usa um diagrama de montagem, o de pintura usa um diagrama de pintura, e o de eletrônica usa um diagrama de circuito elétrico. Esses diagramas podem ser usados individualmente ou em conjunto para representar o carro.

> ⚠️ **Ponto de atenção**
>
> Realizar engenharia reversa de sistemas não conhecidos por você é uma atividade trabalhosa. É necessário entender o sistema, suas funcionalidades, suas regras de negócio, suas tecnologias, etc. E, para isso, é necessário ter acesso ao código fonte do sistema. 
>
> Por vezes, o sistema é complexo e não é entendível por completo. Neste caso, é muito útil utilizar ferramentas CASE que permitem gerar diagrama UML da arquitetura do sistema. E, melhor ainda, é quando você consegue fazer engenharia reversa utilizando análise baseada em Visões UML.

O mesmo acontece com o software. O software pode ser representado de várias formas, sob várias perspectivas. Cada perspectiva é chamada de visão. As visões são usadas para representar:

<center>
    <figure>
        <img src="../../../../assets/images/lessons/design02.png" width=500 alt="Visões clássicas de um sistema de software">
        <figcaption>
            Visões clássicas de um sistema de software
        </figcaption>
        <small>Fonte: criação própria, em jun/2023</small>
    </figure>
</center>

- Visão de casos de uso
- Visão de lógica
- Visão de componentes
- Visão de concorrência
- Visão de implantação

Assim, cada uma irá mostrar aspectos particulares, dando enfoque a determinados ângulos e níveis de abstrações diferentes.

Isto é muito útil! Não adianta conhecer todas as formas de representação ou modelagem de sistemas sem saber como e quando aplicá-las. E é aí que as visões entram. Elas são usadas para representar o sistema de diferentes perspectivas, cada uma com um foco diferente.

> ⚠️ **Ponto de atenção**
>
> Não é necessário representar todo um sistema de software utilizando todos os fluxos possíveis, todas as funcionalidades e casos de usos, para todos os requisitos do cliente. Lembre-se que somente deverão ser modelados e especificados as funcionalidades necessárias para um bom entendimento do sistema, isto é, funcionalidades que são complexas e que podem ser mal interpretadas.
>
> **O contrário é engessamento do processo de desenvolvimento.**

<center>⚠️ Faça somente aquilo que for útil! ⚠️</center>

# Visão de casos de uso

A visão de casos de uso exibe as funcionalidades do sistema e como elas são percebidas pelos usuários enquanto atores que interagem com o sistema.

Os principais modelos a serem utilizados são:

- Diagrama de casos de uso
- Diagrama de atividades
- Diagrama de sequência
- Diagrama de comunicação
- Protótipos visuais de baixo ou alto nível de fidelidade

Deve ser entendida por:

- Clientes
- Designers
- Desenvolvedores
- Gerentes de projeto

## Diagrama de Casos de Uso

Como você sabe, os requisitos funcionais definidos em **Documento de Requisitos** em [/lessons/softeng/requirements/req/sample/](/lessons/softeng/requirements/req/sample/) definem as funcionalidades que estarão presentes no sistema. E, para representar estas funcionalidades, utilizamos o diagrama de casos de uso.

O diagrama de casos de uso é um diagrama de comportamento que descreve as funcionalidades do sistema e como elas são percebidas pelos usuários enquanto atores que interagem com o sistema. Reveja o assunto relacionado ao Diagrama de Casos de Uso, se necessário.

### Como extrair Casos de Uso de Requisitos Funcionais?

Desta forma, vamos seguir as seguintes etapas para poder construir um diagrama de casos de uso:

1. Identificar os atores
   1. Dê uma olhada no **RF001** do [Documento de Requisitos](/lessons/softeng/requirements/req/sample/). Quais são os atores envolvidos?
   2. Foi identificado o Cliente, pois ele atua como usuário da funcionalidade de cadastro de produto, bem como poderá alterar, excluir e consultar os produtos cadastrados por ele. 
   3. Desenhe o ator "Cliente" no diagrama de casos de uso.
2. Identifique o caso de uso
   1. Faça a seguinte pergunta sobre o **RF001**: a ação de "Manter" é uma funcionalidade do sistema ou uma etapa de uma ação ou processo maior?
   2. Como mencionado, o Cliente poderá cadastrar, alterar, excluir e consultar os produtos cadastrados por ele. Assim sendo, "Manter" significa que o cliente poderá realizar todas estas ações. Assim sendo, a ação nos remete à funcionalidade e, por isto, é candidato a ser um caso de uso. Se fosse uma etapa de uma ação ou processo maior, seria um fluxo principal, alternativo ou fluxo de exceção de um caso de uso. 
   3. Desenhe o caso de uso "Manter Produtos".
3. Identifique os relacionamentos entre os atores e os casos de uso
   1. O Cliente é o ator que interage com o caso de uso "Manter Produtos".
   2. Desenhe o relacionamento entre o ator "Cliente" e o caso de uso "Manter Produtos".
4. O diagrama, inicialmente, deverá ficar assim:

    [![Caso de Uso 01](https://tinyurl.com/2mszgurt)](https://tinyurl.com/2mszgurt)<!--![Caso de Uso 01](../../../../assets/puml/usecase_rf01.puml)-->
    <br>
    <small>
        Diagrama de Casos de Uso UC Manter Produto
    <br>
        Fonte: criação própria, em jun/2023
    </small>
5. Continuando a análise sobre o mesmo requisito funcional **RF001**, o ator deverá "controlar as garantias, para que eu possa saber quando o produto estará fora de garantia".
   1. O ator "Cliente" interage com uma funcionalidade à parte. Com isso entendemos que um produto poderá possuir várias garantias, o que é verdade, pois temos a garantia normal, definida por lei, a garantia dada pelo fabricante e a garantia estendida.
   2. Assim sendo, a funcionalidade não é uma etapa adicional, mas uma funcionalidade que, inclusive, poderá ser executada por outras funcionalidades dentro do mesmo sistema.
6. Desenhe o caso de uso "Manter Garantias".
7. Identifique os relacionamentos entre atores e casos de usos, bem como entre casos de usos e casos de usos.
   1. Até o momento o ator não realiza uma ação direta, ou acessa diretamente a ação "Manter garantias", pois tem que passar pela ação "Manter produto" quando ele necessita realizar uma consulta ao produto antes de adicionar, alterar ou excluir uma garantia.
   2. Assim, podemos identificar uma ação **opcional** do ator "Cliente" para com o caso de uso "Manter Garantias". 
   3. Por que opcional? Porque o ator pode ou não realizar a ação de "Manter Garantias", assim que ele executa a ação de "Manter Produtos".
   4. Desta forma, o relacionamento será entre os casos de usos "Manter Produtos" e "Manter Garantias", como sendo uma **opcionalidade**. Desenhe o relacionamento como "extends".
8. O diagrama, inicialmente, deverá ficar assim:

    [![Caso de Uso 02](https://tinyurl.com/2mub4322)](https://tinyurl.com/2mub4322)<!--![Caso de Uso 02](../../../../assets/puml/usecase_rf01_2.puml)-->
    <br>
    <small>
        Diagrama de Casos de Uso UC Manter Produto e UC Manter Garantias
    <br>
        Fonte: criação própria, em jun/2023
    </small>

    Após a realização deste procedimento sobre cada requisito funcional, o diagrama de casos de uso ficará assim:

    > ℹ️ **Nota**
    >
    > O diagrama de caso de uso abaixo modela o requisito funcional RF001 até o RF007 do [Documento de Requisitos](/lessons/softeng/requirements/req/sample/) validado junto ao cliente.

    [![Caso de Uso 02](https://tinyurl.com/2nvzsd5k)](https://tinyurl.com/2nvzsd5k)<!--![Caso de Uso 02](../../../../assets/puml/usecase_view.puml)-->
    <br>
    <small>
        Diagrama de casos de uso
    <br>
        Fonte: criação própria, em jun/2023
    </small>

## Como extrair as etapas de um Caso de Uso?

Agora que temos o diagrama de casos de uso, vamos extrair as etapas de cada caso de uso. Para isto, vamos utilizar o diagrama de atividades.

### Passos para criação de um diagrama de atividades

O diagrama de atividades é um diagrama de comportamento que descreve o comportamento do sistema em termos de atividades. Ele é utilizado para modelar o fluxo de trabalho de um sistema. Reveja o assunto relacionado ao Diagrama de Atividades, se necessário.

Para extrair as etapas de um caso de uso, vamos seguir as seguintes etapas:

1. Identifique o caso de uso
   1. Vamos utilizar o caso de uso "Manter Produtos" como exemplo.
2. Verifique na descrição do requisito se exitem etapas ou passos a serem realizados. Se existirem, desenhe-as no diagrama de atividades.
   1. Vamos utilizar o requisito funcional RF001 como exemplo.
   2. Durante a atividade de análise, você irá identificar que o termo "Manter", como dito anteriormente, significa que o cliente poderá cadastrar, alterar, excluir e consultar os produtos cadastrados por ele.
   3. Desenhe as etapas no diagrama de atividades.

### Diagrama de atividades UCS Manter Produtos e Garantias

Nesta caso, estou somente representando o caso de uso Manter Produtos e Garantias.

[![Caso de uso Manter Produtos e Garantias](https://tinyurl.com/2d8zfbw9)](https://tinyurl.com/2d8zfbw9)<!--![Caso de uso Manter Produtos e Garantias](../../../../assets/puml/activity_view01.puml)-->
<br>
<small>
    Diagrama de atividades das UCS Manter Produtos e Garantias
<br>
    Fonte: criação própria, em jun/2023
</small>

### Diagrama de atividades UCS Manter Clientes

Aqui estou representando, para fins de exemplo, o diagrama de atividades da UC Manter Clientes.

[![Diagrama de Atividades da UC Manter Clientes](https://tinyurl.com/222rgl6x)](https://tinyurl.com/222rgl6x)<!--![Diagrama de Atividades da UC Manter Clientes](../../../../assets/puml/activity_view02.puml)-->
<br>
<small>
    Diagrama de atividades das UCS Manter Clientes
<br>
    Fonte: criação própria, em jun/2023
</small>

> ℹ️ **Nota**
>
> Apesar de ter mencionado que podemos utilizar também os diagramas de sequência, de comunicação e/ou protótipos visuais de baixo ou alto nível de fidelidade, estes não foram utilizados aqui por não haver necessidade - pelo menos até o momento. Lembre-se, faça somente aquilo que for útil!

<!-- # Visão lógica

A visão lógica exibe a estrutura do sistema e como os componentes do sistema interagem entre si.

Os principais modelos que podem ser utilizados são:

- Para análise de estrutura estática
  - Diagrama de classes
  - Diagrama de objetos
- Para análise de comportamento dinâmico
  - Diagrama de máquina de estados
  - Diagrama de atividades

Deve ser entenda por:

- Designers
- Desenvolvedores

## Arquitetura do sistema

Você pode estar se perguntando:

- Possuo documentos ou um backlog de requisitos, e agora?
- Possuo análise do sistema baseada na visão de casos de uso, por onde devo começar? -->
