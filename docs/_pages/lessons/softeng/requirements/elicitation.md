---
layout: home
author_profile: true
title: Elicitação de Requisitos
permalink: /lessons/softeng/requirements/elicitation/
sidebar:
    nav: "softeng-requirements"
---
Criado em Março de 2023 por *Maxwell Anderson*

<figure>
    <img src="../../../../assets/images/gpt/cat_conducting_interview1.jpg" width="350" alt="Gato realizando uma entrevista junto a um cliente. Prompt: create a image of a software engineer cat conducting an interview with a client">
    <figcaption>Gato realizando uma entrevista junto a um cliente.</figcaption>
    <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
</figure>

> Se o gato consegue, você também consegue!

# Introdução

Esta atividade abrange identificar quais as principais necessidades das partes envolvidas ou *stakeholders* no projeto. A partir daí, é possível identificar os requisitos do sistema.

# Objetivos

- Identificar os principais stakeholders do projeto.
- Realizar o levantamento de informações sobre o problema e as necessidades dos stakeholders.
  - Realizando entrevistas e brainstormings.
  - Realizando o levantamento de informações em documentos, prototipação de baixa fidelidade, encenações, interpretação de papéis, etc.
- Realizar a análise dos dados coletados.
- Escrever os requisitos do produto.

# Atividades práticas

Aqui estão algumas atividades práticas que podem ser realizadas para a obtenção dos requisitos do sistema.

## Entrevistas

As entrevistas são uma das principais técnicas de elicitação de requisitos. Elas podem ser realizadas com os stakeholders do projeto, com usuários finais, com especialistas, etc.

Nós, engenheiros de software, temos que ser bons ouvintes. É importante que você esteja atento às informações que estão sendo passadas e que você esteja preparado para fazer perguntas que ajudem a esclarecer o problema e as necessidades dos stakeholders.

Outra coisa que vale salientar: nós não somos, inicialmente, os especialistas no problema. É importante que você seja humilde e que você esteja disposto a aprender com os stakeholders, sobre a maneira como eles trabalham e exercem suas atividades diárias. Geralmente estas pessoas exercem suas atividades manualmente, utilizando provavelmente papel e caneta, e elas podem ter dificuldades em explicar como elas fazem as coisas. É importante que você esteja disposto a aprender com elas e que você esteja disposto a fazer perguntas que ajudem a esclarecer o problema e as necessidades dos stakeholders, já que o objetivo é desenvolver um produto de software que ajude a agilizar e automatizar as atividades que eles realizam.

> 💡**Exemplo**
>
> Se um advogado ou um escritório de advocacia solicita a você que seja desenvolvido um sistema para gerenciar os processos judiciais?
>
> Pergunta: você entende do ramo do Direito? Provavelmente não.
>
> Então, você pode perguntar a ele como ele organiza os processos judiciais. Você pode perguntar a ele como ele organiza os documentos, as informações, as datas, etc. Você pode perguntar a ele como ele organiza as informações sobre os clientes, sobre os advogados, os processos judiciais, etc.

### Entrevistas livre de contexto

As entrevistas livre de contexto são aquelas em que o entrevistador não tem nenhum conhecimento prévio sobre o assunto. O entrevistador deve ser capaz de entender o problema e as necessidades dos stakeholders apenas com as informações que são passadas durante a entrevista.

Exemplos de entrevistas livre de contexto:

- Para encontrar os atores:
  - Quem são os clientes que irão solicitar o desenvolvimento do sistema?
  - Quem são os usuários que irão utilizar o sistema?
  - As necessidades deles são diferentes?
  - Quais são suas habilidades e conhecimentos técnicos?
  - Quais são as suas formações acadêmicas e ambientes de trabalho?
- Para compreender os processos e as atividades que eles executam:
  - Qual o problema vocês estão enfrentando?
  - Por que vocês desejam resolver este problema? Existem outras razões?
  - Como se resolve este problema hoje?
  - Existe em outro lugar uma solução para este problema?
  - Por que é tão importante uma solução para este problema?
- Para entender os principais requisitos do produto a ser criado:
  - Que problemas o sistema deve resolver?
  - Poderão existir riscos para o usuário?
  - Em que ambiente o produto deverá ser executado?
  - O que você espera do produto com relação a:
    - qualidade
    - desempenho
    - segurança
    - usabilidade
    - ...

### Perguntas com base em contexto

- Perguntas que induzem a uma resposta:
  - Você precisa de uma tela touch screen para utilizar o sistema?
  - Você necessita de um sistema que seja executado em um computador desktop?
- Perguntas com respostas:
  - São necessários 10 usuários para utilizar o sistema?
  - É necessário acesso via web para utilizar o sistema?
- Orientações controladas:
  - Podemos responder as minhas dúvidas?
  - Você pode me explicar melhor sobre o problema?
- Perguntas longas e complexas:
  - Tenho uma pergunta que se divide em 3 partes.

### Considerações

- Não faça perguntas que você já sabe a resposta.
  - Por exemplo, se você já sabe que o cliente deseja um sistema que seja executado em um computador desktop, não pergunte se ele deseja um sistema que seja executado em um computador desktop.
- Evite pedir ao cliente que descreva algo que ele normalmente não descreve.
  - Por exemplo, se o cliente não tem experiência em desenvolvimento de software, evite perguntar sobre aspectos técnicos muito específicos.
- Não formule perguntas que pressupõem que o cliente pode descrever atividades complexas.
  - Por exemplo, em vez de perguntar "como você descreveria o processo de integração de dados entre sistemas?", prefira perguntar "como os diferentes sistemas se comunicam atualmente?".
- De modo geral, os clientes podem realizar muitas atividades que não conseguem descrever.
  - Por exemplo, um cliente pode utilizar um software complexo diariamente, mas não saber explicar detalhes técnicos sobre seu funcionamento.
- Existem poucas correlações empíricas que comprovam isso.
  - Por exemplo, pode haver casos em que o cliente não consiga descrever uma atividade, mas ao mesmo tempo possua uma grande quantidade de informações valiosas sobre outras atividades.
- Formule perguntas que não possuem respostas definitivas.
  - Por exemplo, em vez de perguntar "qual é a solução ideal para este problema?", prefira perguntar "como vocês lidam atualmente com este problema?".
- Evite perguntas que começam com "Por que...?", pois elas podem gerar uma postura defensiva.
  - Por exemplo, em vez de perguntar "por que vocês fizeram desta forma?", prefira perguntar "vocês já consideraram outras opções para resolver este problema?".

### Condução da entrevista

- Seja gentil e educado.
- Seja paciente e atencioso.
- Não espere que o entrevistado responda todas as suas perguntas.
- Não espere respostas curtas e simples.
- Não apresse o entrevistado quando estiver respondendo.
- Lembre-se que existem partes interessadas que não são usuários de sistemas de informação e/ou que possuem vários níveis de conhecimento e formação educacional, alguns com conhecimentos técnicos e outros não.
- Sempre ouça!
