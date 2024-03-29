---
title: Visões do Sistema
permalink: /lessons/softeng/design/views/
sidebar:
    nav: "softeng-design"

layout: single
author_profile: true
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_design02.png
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: create an image of a cat studying software engineering"
---

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

- [Visão de casos de uso](/lessons/softeng/design/views_usecase/)
- [Visão de lógica](/lessons/softeng/design/views_logic/)
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

---
Criado em Janeiro de 2020 por *Maxwell Anderson*