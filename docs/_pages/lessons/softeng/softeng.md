---
title: Práticas em Engenharia de Software
permalink: /lessons/softeng/
sidebar:
    nav: "softeng"

layout: single
author_profile: true
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_studying_glasses.jpg
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: create an image of a cat studying software engineering"
---
> Se o gato consegue, você conseguirá.

# Bem-vindo!

**Seja bem-vindo ao curso de Práticas em Engenharia de Software.**

Este curso tem como objetivo apresentar inicialmente as práticas de Engenharia de Software, como:

* a preparação para iniciação ao entendimento do problema ou demanda a ser atendida, bem como sobre suas funcionalidades;
* o desenvolvimento de software, que envolve a codificação, testes, integração e entrega;

O foco é manter a simplicidade, deixando de lado, quando cabível, assuntos mais complexos. O objetivo é apresentar as práticas de forma simples e objetiva, de forma que o aluno possa entender e aplicar em seu dia a dia.

Os vídeos e aulas são direcionadas ao público de desenvolvedores de software, partindo dos iniciantes de nível médio ao superior, mas podem ser utilizadas por qualquer pessoa que tenha interesse em aprender sobre o assunto.

Maxwell Anderson Ielpo do Amaral

# Conteúdo do curso

* Introdução
  * [Introdução à Engenharia de Software](/lessons/softeng/zero/intro/)
  * [Artefatos de exemplo](#artefatos)
* Preparação do ambiente
  * [Introdução](/lessons/softeng/intro/intro/)
  * [Criando uma conta no GitHub](/lessons/softeng/intro/github/)
  * [Instalando o Git no Windows](/lessons/softeng/intro/git/)
  * [Instalando o Visual Studio Code](/lessons/softeng/intro/vscode/)
  * [Instalando o Python no Windows](/lessons/softeng/intro/python/)
  * [Instalando o Django no Windows](/lessons/softeng/intro/django/)
* Engenharia de Requisitos
  * [Introdução à Engenharia de Requisitos](/lessons/softeng/requirements/intro/)
  * [Elicitação de Requisitos](/lessons/softeng/requirements/elicitation/)
  * [Visão do Produto](/lessons/softeng/requirements/vision/)
  * [Análise de custos e vendas](/lessons/softeng/requirements/costs/)
* Análise e Projeto
  * [Introdução à Análise e Projeto](/lessons/softeng/design/intro/)
  * [Análise baseada em visões do sistema](/lessons/softeng/design/views/)
* Engenharia de Testes
  * [Introdução à Engenharia de Testes](/lessons/softeng/tests/intro/)
  * [Histórias de usuários](/lessons/softeng/tests/user-stories/)
  
  <!-- * [Configurando as extensões do VSCode](01.%20Prepara%C3%A7%C3%A3o%20do%20ambiente/06.%20Configurando%20as%20extens%C3%B5es%20do%20VSCode.md) 
  * Test Driven Development (TDD)
  * [Introdução](/lessons/softeng/tdd/intro/)
  * [Escrevendo histórias de usuários](/lessons/softeng/tdd/user-histories/)

  -->

# Artefatos de exemplo

Segue também um quadro geral sobre os artefatos gerados como exemplo de um projeto de software relacionado a um sistema de controle de garantias de produtos.

| Fase              | Artefato                    | Descrição                                                                                                                                  |
| :---------------- | :-------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Requisitos        | [Visão do Produto][1]       | Descreve o produto a ser desenvolvido de maneira abrangente                                                                                |
| Requisitos        | [Requisitos de Software][2] | Lista os requisitos funcionais e não funcionais do sistema                                                                                 |
| Análise e Projeto | [Visão de Casos de Uso][3]  | Descreve o sistema sob a perspectiva de casos de uso e histórias de usuários (em construção e designing) 👷‍♂️                                  |
| Análise e Projeto | Visão lógica                | Permite visualizar a estrutura do sistema em uma perspectiva baseada na arquitetura e na implementação do sistema                          |
| Análise e Projeto | Visão de componentes        | Permite visualizar o sistema sob a perspectiva de componentes e seus relacionamentos                                                       |
| Análise e Projeto | Visão de implantação        | Permite visualizar como o sistema deverá ser implantado                                                                                   |
| Análise e Projeto | Visão de concorrência       | Não se aplica ao projeto                                                                                                                   |
| Testes            | Histórias de usuários       | Contém as histórias de usuários construídos na fase de Requisitos e de Análise e Projeto, adicionados os códigos para testes automatizados |

> 💡Importante!
> 
> Apesar da lista acima parecer ser sequencial, na prática, os artefatos são gerados de forma iterativa, incremental e não sequencial. 
>
> Veja um exemplo de linha do tempo de desenvolvimento de projeto de software
{: .notice--warning}

[![Gantt](http://tinyurl.com/24u2e6ke)](http://tinyurl.com/24u2e6ke)<!--![Gantt](../../../assets/puml/gantt_artefacts.puml)-->
{: .align-center} 

## Discussões sobre Engenharia de Software

> 💡Importante saber!
> 
> Na maioria dos projetos de desenvolvimento de aplicativos não será necessário o desenvolvimento pormenorizado de todos os artefatos. Os artefatos gerados são apenas um exemplo de um projeto de software relacionado a um simples sistema de controle de garantias de produtos. O objetivo é apresentar os artefatos de forma simples e objetiva, de forma que o aluno possa entender e aplicar em seu dia a dia, quando necessário. Isso implica dizer que os artefatos podem ser adaptados de acordo com a necessidade do projeto, ou mesmo, podem não ser utilizados.
> 
> Veja uma discussão sobre o assunto em:
>
> - [Quando um software deve ser modelado?][101]
> - [É sempre necessário criar um projeto de software?][102]
> - [Deve-se ter todos esses papéis em um projeto?][103]
> - [Deve-se executar atividades de todas as áreas da Engenharia de Software em um projeto?][104]
{: .notice--info}

## Livro

Devido à experiência adquirida na implantação de melhoria de processos de desenvolvimento de software, pude escrever sobre o assunto em um livro. Se você se interessar, pode baixá-lo gratuitamente em [http://editora.ifpb.edu.br](http://editora.ifpb.edu.br/index.php/ifpb/catalog/book/7)

{% 
  include figure 
  image_path="/assets/images/lessons/intro09.png" 
  alt="Implantação de melhoria de processos de software com CMMI-DEV nível 2" 
  caption="Implantação de melhoria de processos de software com CMMI-DEV nível 2" 
%}
{: .align-center} 

Criado em Março de 2023 por *Maxwell Anderson*

[1]: <https://github.com/maxwellamaral/maxwellamaral.github.io/blob/main/specs/requirements/vision.md>
[2]: <https://github.com/maxwellamaral/maxwellamaral.github.io/blob/main/specs/requirements/requirements.md>
[3]: <https://github.com/maxwellamaral/maxwellamaral.github.io/blob/main/specs/design/view-usecase.md>

[101]: </lessons/softeng/design/intro#quando-um-software-deve-ser-modelado>
[102]: </lessons/softeng/design/intro#é-sempre-necessário-criar-um-projeto-de-software>
[103]: </lessons/softeng/zero/intro#deve-se-ter-todos-esses-papéis-em-um-projeto>
[104]: </lessons/softeng/zero/intro#deve-se-executar-atividades-de-todas-as-áreas-da-engenharia-de-software-em-um-projeto>