---
layout: home
author_profile: true
title: Exemplo de Documento de Requisitos de Software
permalink: /lessons/softeng/requirements/req/sample/
sidebar:
  nav: "softeng-requirements"
---

Criado em Abril de 2023 por _Maxwell Anderson_

## Capa

---

<h1>Requisitos de Software</h1>

<h2>Sistema de Controle de Garantias de Produtos (SCGP)</h2>

<small>Versão 1.0</small>

---

## Histórico de revisões

|    Data    | Versão |          Descrição          |      Autor       |
| :--------: | :----: | :-------------------------: | :--------------: |
| 01/04/2023 |  1.0   |    Criação do documento     | Maxwell Anderson |
| 02/04/2023 |  1.1   | Adição de novas informações | Maxwell Anderson |

---

## Sumário

- [Introdução](#introdução)
  - [Definições, Acrônimos e Abreviações](#definições-acrônimos-e-abreviações)
- [Usuários identificados](#usuários-identificados)
- [Requisitos funcionais](#requisitos-funcionais)
- [Requisitos não-funcionais](#requisitos-não-funcionais)
  - [Disponibilidade](#disponibilidade)
  - [Privacidade e segurança](#privacidade-e-segurança)
  - [Usabilidade](#usabilidade)
  - [Suportabilidade](#suportabilidade)
  - [Interoperabilidade](#interoperabilidade)
  - [Manutenibilidade](#manutenibilidade)
  - [Desempenho](#desempenho)
  - [Implementação](#implementação)
  - [Implantação](#implantação)
- [Matriz de rastreabilidade](#matriz-de-rastreabilidade)
  - [Rastreabilidade entre NFs e RNFs](#rastreabilidade-entre-nfs-e-rnfs)

---

# Introdução

O objetivo deste documento é apresentar os requisitos de software do produto **Sistema de Controle de Garantias de Produtos (SCGP)**

## Definições, Acrônimos e Abreviações

Esta subseção fornece as definições de todos os termos, acrônimos e abreviações necessárias à adequada interpretação do Documento de Requisitos.

- Identificação dos requisitos: por convenção, a referência a requisitos é feita através do identificador de requisitos, de acordo como descrito abaixo:

  `[IDENTIFICADOR DO TIPO DE REQUISITOSidentificador do requisito]`

  O identificador do tipo de requisitos é conforme abaixo:

  - RF – Requisito Funcional
  - RNF – Requisito Não-Funcional
  - NR – Não-Requisito

  O identificador do requisito será uma sequência numérica. Esse número sequencial será único para todo o conjunto de tipos de requisitos.

  **Exemplo**: RF0001, RF1234, RNF1234, NR1212

- Atributos dos Requisitos: os atributos de requisitos estabelecidos são:
  - **Requisitos vinculados**: fornece uma lista dos requisitos que mantém rastreabilidade.
  - **Prioridade**: Essencial, Importante, Desejável
  - **Complexidade**: Complexa, Alta, Média ou Baixa.
  - **Risco**: Alto, Médio, Baixo

# Usuários identificados

Os seguintes usuários foram identificados para o sistema:

- Usuário do sistema
  - Usuários comuns
    - Usuário cliente
    - Patrocinador
    - Fabricantes
    - Varejistas
    - Atendente de suporte
  - Administrador do sistema

# Requisitos funcionais

Os requisitos funcionais são descritos a seguir.

- **[RF001]** - Como um cliente, eu gostaria de poder cadastrar os produtos que eu compro e controlar as garantias, para que eu possa saber quando o produto estará fora de garantia. Os produtos devem ser cadastrados com os seguintes dados: nome do produto, data de compra, data de vencimento da garantia, segmento do produto, marca e modelo do produto, local de compra, valor pago pelo produto, valor da garantia e modo de compra (online ou físico).
- **[RF002]** - Como administrador, eu gostaria de oferecer aos clientes a possibilidade de contratar uma assinatura do serviço, onde eles possam pagar uma mensalidade e terem acesso a um número ilimitado de garantias, bem como possibilitar uma assinatura gratuita com acesso a recursos limitados, como por exemplo, apenas registrar até 20 produtos.
- **[RF003]** - Como administrador, gostaria de oferecer aos patrocinadores uma oportunidade de divulgar seus produtos, para que eles possam aumentar suas vendas, de acordo com os segmentos de produtos que os clientes já possuem conforme registrado no sistema.
- **[RF004]** - Como administrador, gostaria de oferecer aos fabricantes a possibilidade venda de dados dos produtos dos clientes. As informações que serão vendidas são: nome do produto, data de compra, data de vencimento da garantia, segmento do produto, marca e modelo do produto, local de compra, valor pago pelo produto e valor da garantia.
- **[RF005]** - Como administrador, gostaria de oferecer aos varejistas a possibilidade de se comunicar com os clientes após a venda, caso estes concordem em receber atualizações sobre oportunidades e promoções.
- **[RF006]** - Como cliente, gostaria de ser notificado quando a garantia de um produto estiver prestes a vencer, para que eu possa providenciar a troca do produto em caso de defeitos.
- **[RF007]** - Como cliente, gostaria de encontrar os contatos dos fabricantes, para que eu possa entrar em contato com eles em caso de defeitos no produto. Os contatos devem ser fornecidos pelo fabricante, podendo ser um telefone, um e-mail ou um site do departamento de vendas e/ou de atendimento ao cliente.
- **[RF008]** - Como cliente, gostaria de realizar a busca pelos produtos que eu possuo, a fim de evitar a compra de novos produtos que eu já possuo. A busca deve ser feita por nome do produto, marca, modelo, segmento e local de compra.
- **[RF009]** - Como cliente, gostaria de verificar quais as regras de garantia de cada produto, para que eu possa saber de que forma o produto será substituído em caso de defeito.
- **[RF010]** - Como administrador, gostaria de realizar o backup dos dados dos clientes, para que eu possa recuperar os dados em caso de falha no sistema.
- **[RF011]** - Como cliente, gostaria de realizar o download dos dados dos produtos que eu possuo, para que eu possa ter uma cópia dos dados em caso de falha no sistema. Os formatos dos arquivos para download poderão ser JSON, planilhas eletrônicas (XLS, XLSX, CSV) e HTML com tabelas e formato acessível para leitores de tela.
- **[RF012]** - Como administrador, gostaria que todos os usuários realizassem login no sistema, para que eu possa ter controle sobre os acessos e possa realizar auditorias de acesso.
- **[RF013]** - Como administrador, gostaria de oferecer aos clientes a possibilidade de realizar o login com o Google, para que eles possam ter uma experiência mais rápida e segura.
- **[RF014]** - Como administrador, gostaria de realizar o gerenciamento de usuários.
- **[RF015]** - Como administrador, gostaria que os usuários fossem comunicados sobre as atualizações do sistema, para que eles possam ter uma experiência mais segura e atualizada.
- **[RF016]** - Como usuário comum, gostaria de reportar problemas no sistema, para que eu possa ajudar a melhorar a experiência dos usuários.
- **[RF017]** - Como usuário comum, gostaria de receber notificações sobre manutenções agendadas no sistema, para que eu possa ter uma experiência mais segura e atualizada.
- **[RF018]** - Como usuário comum, gostaria de poder me cadastrar no sistema.
- **[RF019]** - Como usuário comum, gostaria de poder alterar o meu e-mail, para que eu possa ter uma experiência mais segura. A alteração de e-mail somente poderá ser realizada por meio de um e-mail de confirmação para acesso a uma página de alteração de e-mail.
- **[RF020]** - Como usuário comum, gostaria de poder alterar a minha senha, para que eu possa ter uma experiência mais segura. A alteração de senha somente poderá ser realizada por meio de um e-mail de confirmação para acesso a uma página de alteração de senha.
- **[RF021]** - Como usuário comum, gostaria de poder ativar acesso por biometria, para que eu possa ter uma experiência mais segura.
- **[RF022]** - Como usuário comum, gostaria de poder ativar acesso por dois fatores, para que eu possa ter uma experiência mais segura.
- **[RF023]** - Como usuário comum, gostaria que minha senha fosse criptografada, para que eu possa ter uma experiência mais segura. A troca de senha somente poderá ser realizada por meio de um e-mail de confirmação para acesso a uma página de troca de senha.
- **[RF024]** - Como cliente, gostaria de poder cadastrar as solicitações de reparo dos produtos que eu possuo, para que eu possa ter um controle sobre as solicitações de reparo.
- **[RF025]** - Como cliente, gostaria de obter relatórios sobre os status das garantias dos produtos que eu possuo, bem como sobre o histórico de solicitações de reparo, devolução ou substituição.
- **[RF026]** - Como administrador, gostaria que o sistema realizasse a verificação sobre se atende aos requisitos mínimos de hardware e software para a execução do sistema, e caso não atenda, deve exibir uma mensagem de erro informando o motivo.
- **[RF027]** - Como usuário comum, gostaria de verificar quais as regras de privacidade e uso de dados de maneira resumida e simplificada, para que eu possa ter uma experiência mais segura. As regras de privacidade e uso de dados também devem ser apresentadas em uma página de termos de uso e política de privacidade, que deve ser acessível a partir do rodapé do site, a partir da página de cadastro e da página de regras simplificadas.
- **[RF028]** - Como usuário gostaria de ler informações em meu idioma, para que eu possa ter uma experiência mais agradável. O sistema deve ser desenvolvido de forma que possa ser traduzido para outros idiomas, priorizando o inglês, o espanhol e o português do Brasil.

# Requisitos não-funcionais

Os requisitos não-funcionais são descritos a seguir.

## Disponibilidade

- **[RNF001]** - O sistema deve ser desenvolvido de forma que possa ser implantado em qualquer plataforma.
- **[RNF011]** - O sistema deve ser desenvolvido de forma que possa ser executado em qualquer dispositivo com conexão offline, e com posterior sincronização dos dados com o servidor.
- **[RNF012]** - O sistema deve estar disponível 24 horas por dia, 7 dias por semana, 365 dias por ano.
- **[RNF013]** - O sistema deve ser desenvolvido de forma que possa ser escalável, ou seja, deve ser possível aumentar a capacidade de armazenamento de dados e de processamento de requisições sem que haja perda de desempenho.

## Privacidade e segurança

- **[RNF002]** - O sistema deve ser desenvolvido de forma que os dados dos clientes sejam protegidos e não sejam acessíveis por terceiros.
- **[RNF003]** - O sistema deve atender aos requisitos de privacidade da LGPD (Lei Geral de Proteção de Dados).
- **[RNF014]** - O sistema deve ser desenvolvido de forma que os dados pessoais dos clientes sejam criptografados, como endereço de e-mail, senha, nome completo, cidade e estado. A criptografia deverá ser realizada com o algoritmo SHA-512, e deve impossibilitar a recuperação dos dados originais.

## Usabilidade

- **[RNF004]** - O sistema deve ser desenvolvido de forma que seja fácil de usar e de fácil aprendizado, de forma que os usuários não precisem de treinamento para utilizá-lo.
- **[RNF019]** - O sistema deve ser desenvolvido de forma que possa ser acessado por pessoas com deficiência visual, auditiva e física.

## Suportabilidade

- **[RNF005]** - O sistema deve ser desenvolvido de forma que possa ser executado nos três principais navegadores da web: Google Chrome, Mozilla Firefox e Microsoft Edge através de um computador com sistema operacional Windows, Linux ou Mac OS, bem como tablets e smartphones com sistema operacional Android ou iOS.
- **[RNF006]** - O sistema deve ser desenvolvido de forma que possa ser executado em aplicativos nativos para Android e iOS.

## Interoperabilidade

- **[RNF007]** - O sistema deve ser desenvolvido de forma que possa ser integrado com a API do Google para autenticação de usuários.

## Manutenibilidade

- **[RNF008]** - O sistema deve ser desenvolvido de forma que possa ser facilmente atualizado e mantido, preferencialmente, de maneira automatizada.
- **[RNF009]** - O sistema deve ser desenvolvido de forma que possa ser facilmente testado e validado, de forma manual e automatizada.
- **[RNF016]** - O sistema deve ser documentado de forma que possa ser facilmente compreendido por terceiros e para facilitar a manutenção do sistema.

## Desempenho

- **[RNF010]** - O sistema deve ser desenvolvido de forma que possa ser executado em qualquer dispositivo com conexão à internet, com velocidade de conexão de no mínimo 1 Mbps com tempo de resposta de no máximo 5 segundos.

## Implementação

- **[RNF015]** - O sistema deve ser desenvolvido com APIs de acesso aos dados, para que possa ser integrado com outros sistemas.

## Implantação

- **[RNF017]** - O sistema deve ser desenvolvido de forma que possa ser implantado em qualquer plataforma de software atualizada.
- **[RNF018]** - O sistema deve ser desenvolvido de forma que possa ser implantado em plataformas de hardware x64 e ARM64, com arquitetura mínima de 64 bits.
- **[RNF020]** - O sistema deve ser verificado quanto ao desempenho mínimo tolerado dos lados servidor e clientes. As especificações sobre pré-requisitos de hardware e software para a execução do sistema devem ser apresentadas em uma página de pré-requisitos, que deve ser acessível a partir do rodapé do site.

# Matriz de rastreabilidade

A matriz de rastreabilidade é apresentada a seguir.

## Rastreabilidade entre NFs e RNFs

| RF / RNF | RF001 | RF002 | RF003 | RF004 | RF005 | RF006 | RF007 | RF008 | RF009 | RF010 | RF011 | RF012 | RF013 | RF014 | RF015 | RF016 | RF017 | RF018 | RF019 | RF020 | RF021 | RF022 |
| :------: | :---: | :---: | :---: | :---: | :---: | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  RNF001  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF002  |       |       |   X   |   X   |   X   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF003  |       |       |   X   |   X   |   X   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF004  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF005  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF006  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF007  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF008  |       |       |       |       |       |       |       |       |       |       |       |       |       |       | X     |       |       |       |       |       |       |       |
|  RNF009  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF010  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF011  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF012  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF013  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
|  RNF014  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       | X     | X     | X     | X     | X     |
