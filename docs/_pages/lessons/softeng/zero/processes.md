---
layout: single
author_profile: true
title: Processos
permalink: /lessons/softeng/zero/processes/
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
sidebar:
    nav: "softeng-zero"
header:
    image: /assets/images/gpt/headers/cat_studying_glasses3.jpg
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: create an image of a cat studying software engineering"
---
<!--SLIDE-->

Vamos entender o que são processos de desenvolvimento de software?

<!--SLIDE-->

# O que é um processo de desenvolvimento de software?

É uma sequência lógica de atividades que tem por objetivo final de produzir ou evoluir um produto de software.

É caracterizado por um conjunto de:

- Atividades
- Papéis
- Artefatos ou produtos de trabalho de entrada ou saída
- Fluxos

<!--vSLIDE-->

{% 
  include figure 
  image_path="/assets/images/lessons/processes1.png" 
  alt="Exemplo de atividade" 
  caption="Criado pelo autor (2009)" 
%}
{: .align-center} 

<!--SLIDE-->

## Atividade

“É uma unidade de trabalho que um indivíduo naquele papel poderá ser solicitado a executar” (Kruchten, 2003).

Atividades definem o **como fazer**

Em um primeiro nível, as atividades são ordenadas e interligadas e descrevem um fluxo de tarefas.

<!--vSLIDE-->

Exemplos:

- _Analisar_ solicitação do cliente
- Levantar requisitos
- Documentar requisitos
- Realizar estimativas de tamanho
- Validar requisito junto ao cliente
- Realizar planejamento do projeto
- Validar projeto junto aos stakeholders
- Especificar requisitos
- Projetar arquitetura
- Desenvolver requisitos
- Realizar testes

<!--SLIDE-->

## Papel

“Define as responsabilidades ou atribuições de um indivíduo ou grupo de indivíduos que trabalham juntos como uma equipe” [1]

Define o que uma pessoa poderá fazer.

É o “chapéu” que alguém poderá utilizar durante um projeto.

Uma pessoa pode ter vários “chapéus” em um projeto. É o famoso funcionário “Bombril”.

<!--vSLIDE-->

**Cargo funcional <> Papel**
{: .notice--warning}

Não existe uma definição padrão mundial para cada papel, aonde suas atribuições são iguais em qualquer parte do mundo.

Uma pessoa que é designado como _Design_ em uma empresa pode ter atribuições complemente diferentes de uma outra pessoa que é designado como _Design_ em outra empresa.

<!--vSLIDE-->

Exemplos de papéis:

- Atendente
- Analista de Requisitos ou Analista de Negócios
- Analista de Sistemas, Engenheiro de Software ou Projetista
- Arquiteto de Software
- Gerente de Projetos
- Analista de  Configuração  ou Gerente de Configuração
- Desenvolvedor
- Analista de Testes ou Testador
- Engenheiro da Qualidade ou SQA
- Projetista de Banco de Dados ou Analista de BD 
- Administrador de Banco de Dados ou DBA 

<!--SLIDE-->

## Artefatos ou Produtos de Trabalho

“É um pedaço de informação que é produzida, modificada ou utilizada em um processo” [1]

São produtos tangíveis de um processo:

- Documentos (nunca somente documentos)
- Especificações
- Modelos 
- Post-its
- Código-fonte
- Executáveis
- O próprio processo

<!--vSLIDE-->

São utilizados como entradas, necessárias para a execução das atividades. 
São também criadas ou modificadas após o término das atividades. São os artefatos de saída.

Exemplos:

- Solicitações dos interessados
- Documento de Visão
- Especificação de Caso de Uso
- Diagrama Entidade-Relacionamento
- Código-fonte x
- Plano de Projeto
- Cronograma de Operações ou Cronograma do Projeto

<!--SLIDE-->

## Fluxos

“É uma sequência de atividades que produz um resultado de valor observável” [1]
Pode ser expresso de várias formas:

- Diagrama de Atividades UML
- Diagramas PEPP
- Diagramas BPMN
- Fluxogramas

<!--SLIDE-->

## Diagramas

<!--vSLIDE-->

### Diagrama de Atividades UML

Segue exemplo de digrama de atividades em UML.

{% 
  include figure 
  image_path="/assets/images/lessons/processes2.png" 
  alt="Exemplo de diagrama de atividades" 
  caption="Criado pelo autor (2009)"
%}{: .align-center}

Os retângulos são atividades e os losangos são decisões. As setas indicam o fluxo de atividades. As barras horizontais indicam o início e o fim do paralelismo de atividades. Os círculos indicam o início e o fim do fluxo de atividades.

<!--vSLIDE-->

### Diagramas PEPP

Adaptado por Aguiar e Rouiller (2005) de BPMN e de fluxogramas.

{% 
  include figure 
  image_path="/assets/images/lessons/processes3.png" 
  alt="Exemplo de diagrama PEPP" 
  caption="Adaptado por Aguiar e Rouiller (2005) de Sommerville (2007)"
%}{: .align-center}

PEPP é um modelo de Processos para Empresas de Pequeno Porte, criado por estudantes e pesquisadores da UFLA. [3]

<!--vSLIDE-->

Possui a seguinte estrutura:

{% 
  include figure 
  image_path="/assets/images/lessons/processes4.png" 
  alt="Estrutura do PEPP" 
  caption="Adaptado por Aguiar e Rouiller (2005) de Sommerville (2007)"
%}{: .align-center}

<!--vSLIDE-->

### Diagramas BPMN

BPMN é a sigla para Business Process Model and Notation. É um padrão de modelagem de processos de negócio.

{% 
  include figure 
  image_path="/assets/images/lessons/processes5.png" 
  alt="Exemplo de diagrama BPMN" 
  caption="Criado pelo autor (2009)"
%}{: .align-center}

<!--vSLIDE-->

É necessário conhecer bem a especificação BPMN para poder compreender os diagramas BPMN. Para mais informações, veja a especificação BPMN 2.0 em [BPMN 2.0](https://www.omg.org/spec/BPMN/2.0/).

<!--SLIDE-->

# Modelos de processos de software

“Um modelo de processo é uma representação abstrata de um processo de software” [2]

Principais modelos de processos: [3]

- Modelo cascata
- Desenvolvimento evolucionário
- Engenharia de software baseada em componentes.

<!--vSLIDE-->

## Modelo cascata ou _waterfall_

É o modelo mais antigo e mais conhecido. Foi o primeiro modelo a ser utilizado na indústria de software. É o modelo mais simples de ser compreendido. É sequencial, aonde as atividades são executadas em sequência, uma após a outra.

{% 
  include figure 
  image_path="/assets/images/lessons/processes6.png" 
  alt="Exemplo de modelo cascata" 
  caption="Criado pelo autor (2009)"
%}{: .align-center}

<!--vSLIDE-->

### Desenvolvimento evolucionário

É um modelo iterativo e incremental. É um modelo mais flexível que o modelo cascata. É um modelo mais adequado para projetos de software de grande porte. 

Podem ser de dois tipos:

- Prototipação
- Desenvolvimento incremental (em espiral)

<!--vSLIDE-->

{% 
  include figure 
  image_path="/assets/images/lessons/processes7.png" 
  alt="Exemplo de modelo evolucionário" 
  caption="Criado pelo autor (2009)"
%}{: .align-center}

<!--vSLIDE-->

{%
  include figure
  image_path="/assets/images/lessons/processes8.png"
  alt="Exemplo de modelo evolucionário"
  caption="Criado pelo autor (2009)"
%}{: .align-center}

<!--vSLIDE-->

O RUP é um modelo de processo de software que utiliza o modelo evolucionário. [1] Ele é representado por um diagrama de "baleias" (whales) ou "ondas" (waves).

{% 
  include figure 
  image_path="/assets/images/lessons/processes9.png" 
  alt="Exemplo de modelo RUP" 
  caption="Criado pelo autor (2009)"
%}{: .align-center}

<!--vSLIDE-->

O SCRUM é um modelo de processo de software que utiliza o modelo evolucionário. É o principal método utilizado no desenvolvimento ágil de software. 

{% 
  include figure 
  image_path="/assets/images/lessons/processes10.png" 
  alt="Exemplo de modelo SCRUM" 
  caption="Criado pelo autor (2009)"
%}{: .align-center}

<!--SLIDE-->

# Ferramentas CASE

Ferramenta CASE é o nome dado ao software utilizado para apoiar as atividades de processo de software. Significa "Engenharia de Software Auxiliada por Computador"
 
Incluem:

- editores de diagramas, 
- dicionário de dados, 
- compiladores, 
- debuggers, 
- ferramentas para construção de sistemas de software etc.

<!--vSLIDE-->

Segue uma lista de ferramentas CASE:

{%
  include figure
  image_path="/assets/images/lessons/processes11.png"
  alt="Exemplo de ferramentas CASE"
  caption="Criado pelo autor (2009)"
%}{: .align-center}

<!--vSLIDE-->

## Classificação CASE

- Ferramentas: apoiam tarefas individuais do processo, como verificação de consistência de um projeto, compilação de um programa e comparação de resultados de um teste;
- Workbenches: apoiam as fases ou atividades de processo, como especificação, projeto etc. Consistem geralmente em um conjunto de ferramentas com integração;
- Ambientes: apoiam todo ou pelo menos parte uma parte substancial do processo de software.

<!--SLIDE-->

# Referências

- [1] Kruchten, P. Introdução ao RUP – Rational Unified Process. Edição Revisada. Rio de Janeiro: Editora Ciência Moderna, 2003.
- [2] Sommerville, I. Engenharia de Software, 8ª edição. São Paulo: Pearson Addison-Wesley, 2007.
- [3] AGUIAR, Heron Vieira ; ROUILLER, Ana Cristina . PEPP: Processo de Software para Empresas de Pequeno Porte baseado no Modelo CMMI. 2005.
