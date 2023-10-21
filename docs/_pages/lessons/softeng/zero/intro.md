---
title: Introdução à Engenharia de Software
permalink: /lessons/softeng/zero/intro/
sidebar:
    nav: "softeng-zero"

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


# Conceitos

{% 
  include figure 
  image_path="/assets/images/lessons/intro01.png" 
  alt="Meme" 
  caption="Fonte: desconhecida" 
%}
{: .align-center} 

-- Eu finalmente encontrei ele... depois de 15 anos. A DOCUMENTAÇÃO!

-- PARA FAZER: preencha isto com mais detalhes depois.

## O que é software?

O que é software para você? Deves imaginar um aplicativo ou um programa que é executado em um computador, certo? Mas, será que é só isso?

Conforme mencionado por Pressman (2006), **software** é um produto desenvolvido por profissionais que abrange programas, instruções e dados que são executados em um computador, podendo ser smartphones, tablets, computadores pessoais, servidores etc. Também é constituído por documentos, podendo ser impresso ou digital, desde que a documentação seja necessária para que o programa funcione corretamente.

{% 
  include figure 
  image_path="/assets/images/lessons/intro02.png" 
  alt="Programa de computador mais documentação é igual a software." 
  caption="Criado pelo próprio autor (2009)" 
%}
{: .align-center}

> 🤔 **Para memorizar**
>
> - **Usuário**: é quem utiliza o software. Pode ser uma pessoa, outra máquina ou um outro sistema.
> - **Cliente**: é quem paga pelo software. Pode ser uma pessoa, uma empresa, um governo etc.
> - **Especificação**: é o documento que descreve o que o software deve fazer, de maneira detalhada.
> - **Artefato**: é qualquer coisa que é produzida durante o trabalho de desenvolvimento de software. Pode ser um documento, um programa, um manual, uma especificação etc.
{: .notice--info}

**Mas o que é entregue ao cliente?**

**Depende**: normalmente entregamos um programa funcionando mais o manual do usuário. Mas, dependendo do cliente, poderemos entregar toda a **especificação** e/ou quaisquer outros artefatos oriundos de um processo.

Já vi clientes contratarem empresas para desenvolverem a especificação e o programa. Também já vi clientes comprarem, além disso, o código-fonte.

> 💡 **Você sabia?**
>
> Que existem clientes que podem contratá-lo para desenvolver software e definir, inclusive, que linguagem de programação deve ser utilizada?
{: .notice--success}

## Categorias de produtos de software

- **Produtos genéricos ou de "prateleira"**: são softwares existentes no mercado que podem ser adquiridos por qualquer pessoa ou empresa. Exemplos: Windows, Linux, Microsoft Office, Photoshop etc.
- **Produtos sob encomenda**: são softwares desenvolvidos sob medida para um cliente específico. Exemplos: sistemas de gestão de empresas, sistemas de gestão de universidades, sistemas de gestão de hospitais etc.

# O que é Engenharia de Software?

{% 
  include figure 
  image_path="/assets/images/lessons/intro03.png" 
  alt="Engenharia de software está contida na engenharia de sistemas" 
  caption="Criado pelo próprio autor (2009)"
%}
{: .align-center}

A **engenharia** é uma ciência que estuda a aplicação de conhecimentos científicos e empíricos para a resolução de problemas.

A **engenharia de sistemas** estuda, no sentindo mais amplo, a aplicação de conhecimentos científicos e empíricos para o desenvolvimento de *sistemas em geral* com o objetivo de resolver problemas ou atender necessidades. Assim sendo, um sistema pode ser composto por elementos de vários outros subsistemas, como por exemplo, um robô que é constituído por elementos mecânicos, elétricos, eletrônicos e de software.

A **engenharia de software** é uma área da engenharia que estuda a aplicação de conhecimentos científicos e empíricos para o desenvolvimento de *sistemas de software* com o objetivo de resolver problemas ou atender necessidades. Assim sendo, um sistema de software é constituído por elementos de software, como programas, instruções, dados e documentação, como visto anteriormente.

{% 
  include figure 
  image_path="/assets/images/lessons/intro04.png" 
  alt="Áreas da Engenharia de Sistemas: engenharia mecânica, engenharia civil, engenharia elétrica, engenharia de software, engenharia da computação, engenharia de estruturas, engenharia química, engenharia de produção etc." 
  caption="Criado pelo próprio autor (2009)"
%}
{: .align-center}

# O que se pode fazer em Engenharia de Software?

Se você está em um curso técnico ou superior da área de Engenharia de Software, Ciência da Computação ou afins, pode estar achando que, ao concluir, você será um desenvolvedor ou programador. Talvez você nem goste de programação. Mas, não se preocupe, pois existem várias outras funções que você pode exercer, como:

- *Engenheiro de requisitos* ou *analista de requisitos*
- *Analista de sistemas de software*
- *Arquiteto de software*
- *Gerente de projetos de software*
- *Engenheiro de testes* ou *testador de software*
- *Analista de configuração*
- *Analista de qualidade*, *SQA* ou *analista de processos de software*
- *Analista de segurança da informação*
- *Desenvolvedor*
- *UX Designer* ou *designer de interface*
- *Analista de dados* ou *cientista de dados*
- *Analista de negócios*
- *Analista de suporte*
- *Analista de infraestrutura*
- *DBA* ou *administrador de banco de dados*
- entre outros...

Já tive alunos que não gostavam de programação (já eu amo) e que se tornaram excelentes analistas de requisitos, analistas de testes... e hoje trabalham em grandes empresas.

> 🤔 **Para memorizar**
>
> **Papel** é o termo usado para designar a função desempenhada por uma pessoa em uma equipe de desenvolvimento de software. Uma pessoa pode ser contratada para ser um analista de sistemas e atuar como tal, mas pode ser que, em um determinado projeto, ela atue como desenvolvedor. Neste caso, ela está desempenhando o papel de desenvolvedor, mas continua representando a empresa ou instituição como analista de sistemas.
{: .notice--info}

Vamos tratar de cada uma das principais áreas da Engenharia de Software? Pode ser que você se identifique com alguma delas.

## Principais áreas da Engenharia de Software

{%
    include figure
    image_path="/assets/images/lessons/intro05.png"
    alt="Áreas da engenharia de software"
    caption="Criado pelo próprio autor (2009)"
%}
{: .align-center}

### Engenharia de requisitos

> 🤔 **Para memorizar**
>
> **Requisito** é uma característica ou capacidade que o sistema deve ter para atender a uma necessidade ou resolver um problema. Um requisito pode ser uma funcionalidade, uma restrição ou uma qualidade.
>
> Imagine um requisito como uma frase que começa com "O sistema deve..." ou "O sistema não deve...", ou mesmo "Como cliente, eu gostaria que o sistema permitisse...".
>
> **Exemplo:**
>
> "O sistema deve permitir que o usuário faça login utilizando seu e-mail e senha."
>
> Vamos ver este assunto de maneira detalhada e prática em [Engenharia de Requisitos](/lessons/softeng/requirements/intro/).
{: .notice--info}

A **engenharia de requisitos** é uma área da Engenharia de Software que estuda a aplicação de conhecimentos científicos e empíricos para a elicitação, análise, especificação, validação e gerenciamento de requisitos de software.

Podemos dividir a engenharia de requisitos em 4 subáreas:

1. **Análise de negócio ou do problema**, leva em consideração:
   - a identificação dos interessados ou *stakeholders* do projeto;
   - a identificação do problema ou demanda a ser atendida e suas restrições;
   - as características funcionais principais do produto, com o objetivo de entender de maneira geral o que o produto deve fazer.
2. **Levantamento dos requisitos**:
   - permite descrever os requisitos de forma mais detalhada, com o objetivo de entender o que o produto deve fazer;
   - caracteriza os requisitos, classificando-os em funcionais e não funcionais;
   - analisa a viabilidade de desenvolvimento do produto, levando em consideração o custo, o tempo e a qualidade;
   - rastreabilidade dos requisitos, que permite identificar a origem de cada requisito, bem como a sua relação com outros requisitos.
3. **Validação dos requisitos**: permite verificar se os requisitos estão corretos, completos, consistentes e não ambíguos.
4. **Gerenciamento de mudanças** ou **gerenciamento de requisitos**: permite gerenciar as mudanças que ocorrem nos requisitos durante o desenvolvimento do produto.

> 👷 **Papel**
>
> Assim sendo, a engenharia de requisitos é executado pelo papel de:
>
> - *analista de requisitos*
> - *engenheiro de requisitos*
> - *analista de negócios*
> - *UX Designers*, mais especificamente na elaboração de protótipos visuais preliminares, esboços de telas, fluxos de telas etc.
> - *Product Owner* ou *PO* (pronuncia-se *"pi-ôu"*). Em metodologias ágeis, este papel desempenha total ou parcialmente as atribuições de um engenheiro de requisitos.
> - dentre outros, podendo ter variações de acordo com a empresa ou instituição.
>
> 🎨 **O que criam?**
>
> - *Documento de visão*
> - *Documento de requisitos*
> - *Documento de especificação de requisitos*
> - *Histórias de usuários*
> - *Protótipos visuais preliminares*
> - *Esboços de contratos*
> - *Casos de uso*
> - Dentre outros
{: .notice--info}

🛠️ **Ferramentas utilizadas**

| Ferramentas                 | Descrição                                    |
| --------------------------- | -------------------------------------------- |
| Gerenciamento de requisitos | [Jira][1], [Trello][2], [GitHub Projects][3] |
| Prototipação                | [Adobe XD][4], [Figma][13], [Balsamiq][5]    |
| Escritório                  | [Microsoft Word][6], [Google Docs][7]        |
| Métodos                     | [Kanban][8], [Scrum][9]                      |

### Análise e projeto

A **análise e projeto de sistemas de software** é uma área da Engenharia de Software que estuda a aplicação de conhecimentos em atividades relacionadas à especificação ou detalhamento dos requisitos levantados na engenharia de requisitos, bem como a definição da arquitetura do sistema e a especificação dos componentes do sistema.

É uma atividade crucial para o desenvolvimento de software, pois é nesta fase que o sistema é projetado, ou seja, é definido como o sistema será implementado. É nesta fase que são definidos os componentes do sistema, como eles se relacionam e como eles se comunicam.

Da mesma forma que um engenheiro civil projeta uma casa para um cliente, o analista de sistemas projeta um sistema de software para um cliente. O engenheiro civil pode fazer uma planta da casa e mostrar para o cliente, que pode aprovar ou não.

{%
    include figure
    image_path="/assets/images/lessons/intro06.png"
    alt="Ilustração de uma planta e um protótipo de casa"
    caption="Criado pelo próprio autor (2009)"
%}{: .align-center}

O analista de sistemas pode fazer um protótipo do sistema e mostrar para o cliente e para os desenvolvedores.

{%
    include figure
    image_path="/assets/images/lessons/intro07.png"
    alt="Ilustração de um protótipo de sistema de software"
    caption="Criado pelo próprio autor (2009)"
%}{: .align-center}

Podemos resumir as atividades desempenhadas pelo analista de sistemas como **realizar a especificação de requisitos em um terceiro nível**, ou seja, detalhar os requisitos levantados na engenharia de requisitos de forma que possam ser implementados e entendidos pelos desenvolvedores e, em alguns casos, pelos clientes.

> 👷 **Papel**
>
> A análise e projeto de sistemas de software é executado por:
> 
> - *analista de sistemas*
> - *UX designers*
> - *arquiteto de software*.
> - *analista de dados*
> - *analista de infraestrutura*
> - dentre outros
>
> 🎨 **O que criam?**
>
> - *Esboço da arquitetura do sistema*
> - [*Diagramas UML*](/lessons/softeng/design/uml/) (Unified Modeling Language), com diagramas de caso de uso, diagramas de classe, diagramas de sequência, diagramas de atividade, diagramas de estado etc.
> - *Diagramas DFD* (Diagrama de Fluxo de Dados)
> - *Diagramas de banco de dados*, como DER (Diagrama Entidade-Relacionamento)
> - *Dicionários de dados*
> - *Protótipos visuais*
> - *Especificação textual* de componentes, interfaces, serviços, APIs etc.
{: .notice--info}

🛠️ **Ferramentas utilizadas**

| Ferramentas            | Descrição                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| Ferramentas CASE       | [Visual Paradigm][10], [Astah][11], [Enterprise Architect][12], [Microsoft Visio][12]     |
| Prototipação           | [Adobe XD][4], [Figma][13], [Balsamiq][5]                                                 |
| Modelagem de dados     | [MySQL Workbench][14], [Oracle SQL Developer Data Modeler][15], [SQL Power Architect][16] |
| Modelagem de processos | [Bizagi Modeler][17], [Draw.io][18], [Microsoft Visio][19]                                |

### Gerência de projetos

A gerência de projetos de software é uma área da Engenharia de Software que estuda a aplicação de conhecimentos em atividades relacionadas ao planejamento, execução e controle de tarefas que deverão ser executadas para o desenvolvimento de um produto de software.

Conforme o Guia PMBOK, um **projeto** é "um esforço temporário empreendido para criar um produto, serviço ou resultado exclusivo" (PMI, 2017).

Um projeto é **temporário** no sentido de que tem um início e um término definidos no tempo, e, por isso, um escopo e recursos definidos.

Já o **gerenciamento de projetos** é a "aplicação de conhecimentos, habilidades, ferramentas e técnicas às atividades do projeto a fim de atender aos seus requisitos." (PMI, 2017)

Segundo o mesmo Guia, o gerenciamento de projetos é dividido em áreas de conhecimento principais, como:

1. **Integração**: permite coordenar as atividades de gerenciamento de projetos, integrando-as entre si e com as atividades de desenvolvimento do produto.
2. **Escopo**: permite definir o escopo do projeto, ou seja, o que será feito e o que não será feito no projeto.
3. **Tempo**: permite definir o cronograma do projeto, ou seja, quando cada atividade será executada.
4. **Custo**: permite definir o orçamento do projeto, ou seja, quanto o projeto custará.
5. **Qualidade**: permite definir os padrões de qualidade que o produto deverá atender.
6. **Recursos humanos**: permite definir as pessoas que farão parte da equipe do projeto.
7. **Comunicação**: permite definir como as informações serão comunicadas entre os membros da equipe e com os interessados.
8. **Riscos**: permite identificar, analisar e planejar respostas para os riscos que podem ocorrer durante o projeto.
9. **Aquisições**: permite definir como os recursos serão adquiridos para o projeto.
10. **Partes interessadas**: permite identificar e gerenciar as partes interessadas no projeto.

O gerente de projetos deve se preocupar com as seguintes restrições do projeto:

1. *Escopo*
2. *Qualidade*
3. *Cronograma*
4. *Orçamento*
5. *Custo*
6. *Riscos*

Se alguma restrição acima sofrer mudança, outro fator será afetado.

De que forma poderíamos dar atenção a todas estas restrições? Pergunte a si mesmo:  "Como eu poderia fazer para entregar um produto de qualidade, dentro do prazo e do orçamento, sem correr riscos?"

Eu pergunto a você: se o orçamento de um projeto diminui, isso irá impactar em quais restrições? Você vai conseguir manter a qualidade e o cronograma do projeto?

Se o cronograma de um projeto diminui, isso irá impactar em quais restrições? Você irá conseguir manter os riscos do projeto controlados? Vai conseguir atender todas as necessidades do cliente conforme definido no escopo?

Assim sendo, o gerente de projetos deve se preocupar as restrições descritas acima todos os dias. 

> 👷 **Papel**
>
> - *Gerente de projetos*
> - Em metodologias ágeis, parte das atividades de gerenciamento de projetos é desempenhada pelo *Scrum Master* 
>
> 🎨 **O que criam?**
>
> - *Plano de gerenciamento do projeto*
> - *Plano de gerenciamento de riscos*
> - *Cronogramas do projeto*
> - *Orçamento do projeto*
> - dentre outros
{: .notice--info}

🛠️ **Ferramentas utilizadas**

| Ferramentas               | Descrição                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------- |
| Gerenciamento de projetos | [Jira][1], [Trello][2], [GitHub Projects][3], [Microsoft Project][20]               |
| Escritório                | [Microsoft Word][6], [Google Docs][7], [Microsoft Excel][6], [Google Planilhas][21] |

### Gerência de configuração

A gerência de configuração é uma área da Engenharia de Software que estuda a aplicação de conhecimentos em atividades relacionadas ao controle de versões dos artefatos produzidos durante o desenvolvimento de um produto de software.

Os procedimentos de gerenciamento de configuração definem como:

1. Os artefatos serão identificados, armazenados e controlados;
2. Relacionar mudanças nos artefatos e componentes do sistema;
3. Identificar diferentes versões de um sistema, envolvendo gerenciamento de releases e de baselines;

> 👷 **Papel**
>
> - *Analista de configuração*
> - *Gerente de configuração*
> - *Administrador de configuração*
>
> 🎨 **O que criam?**
>
> - *Plano de gerenciamento de configuração*
> - *Plano de gerenciamento de mudanças, de liberação e de baselines*
> - *Relatórios de mudanças*
{: .notice--info}

🛠️ **Ferramentas utilizadas**

| Ferramentas                   | Descrição                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| Controle de versão            | [Git][22], [GitHub][23], [GitLab][24], [Bitbucket][25]                              |
| Gerenciamento de configuração | [Jira][1], [Trello][2], [GitHub Projects][3]                                        |
| Escritório                    | [Microsoft Word][6], [Google Docs][7]                                               |
| Integração contínua           | [Jenkins][26], [Travis CI][27], [Circle CI][28], [Gitlab][24], [GitHub Actions][23] |
| Automação de testes           | [Selenium][29], [Cypress][30] (somente algumas funcionalidades são utilizadas)      |

### Codificação ou desenvolvimento

A codificação ou desenvolvimento de software é uma área da Engenharia de Software que estuda a aplicação de conhecimentos em atividades relacionadas à implementação de um produto de software.

Envolve em colocar a "mão na massa" quando se trata de programar. É nesta fase que o sistema é implementado, ou seja, é desenvolvido o código-fonte do sistema.

__Exemplos de códigos__

```java
// Leitura do arquivo test.txt em Java
File dir = new File("/home/user/test.txt");
File fin = new File(dir.getCanonicalPath() + File.separator + "test.txt");
FileInputStream fis = new FileInputStream(fin);
BufferedReader br = new BufferedReader(new InputStreamReader(fis));
String aLine = null;
while ((aLine = br.readLine()) != null) {
    System.out.println(aLine);
}
if (aLine.trim().length() == 0) {
    // linha em branco
}
in.close();
```

```python
# Leitura do arquivo test.txt em Python

my_file = open("/home/user/test.txt", "r")
print(my_file.read())
my_file.close()
```

Veja ums lista de linguagens de programação em [https://pt.wikipedia.org/wiki/Lista_de_linguagens_de_programação](https://pt.wikipedia.org/wiki/Lista_de_linguagens_de_programa%C3%A7%C3%A3o )

> 👷 **Papel**
>
> - *Desenvolvedor*
> - *Programador*
>
> 🎨 **O que criam?**
>
> - *Código-fonte*
> - *Testes unitários*
> - *Documentação de código*
> - Dentre outros
{: .notice--info}

🛠️ **Ferramentas utilizadas**

| Ferramentas        | Descrição                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Desenvolvimento    | [Visual Studio Code][31], [PyCharm][32], [Eclipse][33], [IntelliJ IDEA][34], [Netbeans][35], Bloco de notas :smile: |
| Controle de versão | [Git][22], [GitHub][23], [GitLab][24], [Bitbucket][25]                                                              |
| Escritório         | [Microsoft Word][6], [Google Docs][7]                                                                               |

### Engenharia de testes

A engenharia de testes é uma área da Engenharia de Software que estuda a aplicação de conhecimentos em atividades relacionadas à verificação e validação de um produto de software.

A **verificação** é o processo de avaliação de um sistema ou componente para determinar se os produtos de uma determinada fase do ciclo de vida cumprem os requisitos estabelecidos na fase anterior.

A **validação** é o processo de avaliação de um sistema ou componente durante ou no final do ciclo de vida para determinar se ele atende aos requisitos especificados. 

Os testes tem como metas:

1. Demonstrar ao desenvolvedor e ao cliente que o software atende aos requisitos.
2. Descobrir falhas ou defeitos que apresenta comportamento incorreto, não desejável ou em não conformidade com sua especificação.

Possui como atividades:

1. Teste de componente ou de unidade
2. Teste de integração
3. Teste de interfaces
4. Teste de desempenho, de carga ou de estresse
5. Teste de usabilidade
6. Teste de segurança
7. Teste de aceitação

> 👷 **Papel**
>
> - *Engenheiro de testes*
> - *Testador de software*
> - *Analista de testes*
> - *Analista de qualidade de produto*
>
> 🎨 **O que criam?**
>
> - *Plano de testes*
> - *Especificação de casos de testes*
> - *Relatórios de testes*
> - *Relatórios de defeitos*
> - Dentre outros
{: .notice--info}

🛠️ **Ferramentas utilizadas**

| Ferramentas                          | Descrição                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------- |
| Gerenciamento de testes              | [TestLink][36], [TestRail][37]                                                      |
| Gerenciamento de defeitos            | [Jira][1], [Trello][2], [GitHub][23], [Gitlab][24]                                  |
| Monitoramento de desempenho          | [JMeter][38], [Gatling][39]                                                         |
| Monitoramento de segurança           | [OWASP][40], [Burp Suite][41]                                                       |
| Monitoramento de usabilidade         | [Google Analytics][42]                                                              |
| Monitoramento de carga               | Apache Bench, Siege                                                                 |
| Monitoramento de estresse            | [Stress-ng][44]                                                                     |
| Monitoramento de cobertura de código | [SonarQube][43], [Codecov][48]                                                      |
| Monitoramento de qualidade de código | [SonarQube][43], [Code Climate][47]                                                 |
| Monitoramento de vulnerabilidades    | [Snyk][45], [WhiteSource][46]                                                       |
| Escritório                           | [Microsoft Word][6], [Google Docs][7], [Microsoft Excel][6], [Google Planilhas][21] |
| Controle de versão                   | [Git][22], [GitHub][23], [GitLab][24], [Bitbucket][25]                              |
| Integração contínua                  | [Jenkins][26], [Travis CI][27], [Circle CI][28], [Gitlab][24], [GitHub Actions][23] |
| Automação de testes                  | [Selenium][29], [Cypress][30]                                                       |


### Qualidade de Processos ou Garantia da Qualidade

A qualidade de processos ou garantia da qualidade é uma área da Engenharia de Software que estuda a aplicação de conhecimentos em atividades relacionadas à melhoria contínua dos processos de desenvolvimento de software.

Enfatiza-se, qualidade de PROCESSOS.

Conforme o MPS.BR, o propósito do processo Garantia da Qualidade é "assegurar que os produtos de trabalho e a execução dos processos estão em conformidade com os planos e recursos predefinidos." (MPS.BR, 2020)

Conforme os mesmo Guia, os objetivos principais são:

1. Avaliar objetivamente os processos executados, produtos de trabalho e serviços em relação à descrição de processos aplicáveis, padrões e procedimentos;
2. Identificar e documentar itens de não-conformidades;
3. Prover feedback para a equipe do projeto e gerentes como resultado das atividades de Garantia da Qualidade; e
4. Assegurar que as não-conformidades são corrigidas.

> 👷 **Papel**
>
> - *Analista de qualidade*
> - *Analista de processos*
> - *Analista de qualidade de processos*
> - *Analista de garantia da qualidade*
> - *Analista de qualidade de software*
> - *SQA* (Software Quality Assurance)
>
> 🎨 **O que criam?**
>
> - *Plano de qualidade*
> - *Plano de garantia da qualidade*
> - *Plano de medição*
> - *Relatórios de qualidade e de conformidade*
> - Dentre outros
{: .notice--info}

🛠️ **Ferramentas utilizadas**

| Ferramentas              | Descrição                                              |
| ------------------------ | ------------------------------------------------------ |
| Diagramação de processos | [Bizagi Modeler][17], [Draw.io][18]                    |
| Controle de versão       | [Git][22], [GitHub][23], [GitLab][24], [Bitbucket][25] |
| Escritório               | [Microsoft Word][6], [Google Docs][7]                  |


# Discussões sobre Engenharia de Software

## Deve-se ter todos esses papéis em um projeto?

1. Não necessariamente. Em um projeto pequeno, pode ser que uma pessoa desempenhe mais de um papel ao contrário de projetos grandes.
2. Tudo também depende do projeto, do cliente, da empresa, da metodologia de desenvolvimento de software, do tamanho e da maturidade da equipe, do orçamento, do prazo, da qualidade, dos riscos etc.

## Deve-se executar atividades de todas as áreas da Engenharia de Software em um projeto?

1. No mínimo desenvolver algo (risos)
2. Mais uma vez, tudo dependerá.

Adentrando nesta discussão, é muito comum vermos desenvolvedores experientes argumentarem que para todo e qualquer projeto o mínimo que se deve fazer é a análise abrangente, codificação e testes. Mas, será que é isso mesmo?

Como sabemos, não existe *bala de prata* e ao meu ver, sabem muito programar, mas sobre metodologias podem entender pouco, o que é muito comum.

Um bom engenheiro de software deve conhecer ferramentas e boas práticas de desenvolvimento de software, bem como as metodologias, para que possa escolher a melhor abordagem para cada projeto.

O mínimo de levantamento e análise de requisitos é obrigatório. Desenvolvedores experientes devem ter conhecimento necessário para implementar uma arquitetura de software adequada para o projeto. E, claro, nunca deixar os testes de lado.

Outros projetos exigirão especificação mais detalhada dos requisitos, bem como o desenvolvimento da análise e projeto do sistema, com o uso de diagramas para **facilitar** a compreensão daqueles que se beneficiarão com o uso da documentação. Se essa documentação será extensa ou não, mais uma vez, dependerá:

1. **Do projeto**, daí podemos depreender que tudo dependerá do tamanho, da complexidade, do orçamento, do prazo, da qualidade, dos riscos etc.
2. **Dos clientes**, pois estes poderão solicitar uma documentação mais detalhada para compreensão ou mesmo para que possam auditar o projeto. Por vezes um Documento de Visão e um Documento de Requisitos poderão ser apensados em um contrato.
3. **Da empresa**, pois esta poderá exigir uma documentação mais detalhada para que possa auditar o projeto bem como para que possa reutilizar a documentação em outros projetos. É muito comum que todo o conhecimento adquirido em um projeto esteja na "cabeça" dos principais desenvolvedores que, por vezes, não documentam nada. E, quando estes saem da empresa, todo o conhecimento é perdido. Outrossim, já vi um sistema com dez anos "de idade" precisar ser reimplementado totalmente utilizando nova tecnologia - o motivo foi a necessidade de adequação a um novo mercado. O problema é que o sistema era muito antigo e não havia documentação necessária para realizar o procedimento. Sabe-se também que para entender como o sistema funcionava "por debaixo dos panos", havia uma curva de aprendizagem altíssima de cerca de dois anos. Pior foi ver gente ser demitida ou pedir demissão perto do fim desta janela de tempo. O resultado foi que o sistema teve que ser reimplementado do zero. Se houvesse documentação, o custo de reimplementação seria menor.
4. **Da metodologia de desenvolvimento de software**. Em metodologias ágeis, a documentação é mínima, mas existe. Em metodologias tradicionais, a documentação é mais detalhada. Existem as abordagens híbridas, quando se mesclam metodologias ágeis e tradicionais. Neste caso, a documentação pode ser mais detalhada ou não. Sou simpático à flexibilidade, pois acredito que cada projeto é um projeto e deve ser tratado como tal. Como sabemos não existe "bala de prata".
5. **Da equipe**. Depende muito do tamanho, da maturidade e do conhecimento profissional dos componentes da equipe. Se a equipe é pequena, pode ser que um desenvolvedor experiente desempenhe mais de um papel e, ainda por cima, deverá dar suporte aos inexperientes. Vejo que a comunidade de TI no Brasil possui profissionais que auxiliam uns aos outros e é bem comum analistas seniores ensinarem ou transmitirem conhecimento aos juniores. De qualquer forma, a curva de aprendizagem sempre será fator determinante para cumprimento dos prazos de um projeto. Se a equipe é grande, pode ser que existam pessoas que desempenhem papéis específicos, como analista de requisitos, analista de testes, desenvolvedor, arquiteto de software, gerente de projetos etc. Neste caso, a curva de aprendizagem será menor, mas o custo do projeto será maior. São várias as variáveis e as equipes devem ir se auto ajustando a medida que os projetos avançam. O importante é que o projeto seja entregue com qualidade, dentro do prazo e do orçamento.

> 📝 **Tome nota**
>
> Ao processo de aprimoramento constante sobre o conjunto de procedimentos adotados por uma equipe de desenvolvimento, chamamos simplesmente de "Melhoria Contínua" ou, sendo mais detalhado, de "Melhoria de Processos de Desenvolvimento de Software".

> ❔**Você sabia?**
>
> Que existem empresas que contratam outras empresas para fazerem a melhoria de processos de desenvolvimento de software de suas equipes?
>
> Que existem conjuntos de boas práticas de desenvolvimento de software que podem ser adotadas por qualquer empresa? São espécies de "manuais" que podem ser seguidos para que as equipes possam melhorar seu dia a dia de trabalho. Dentre elas temos boas práticas do:
>
> - [Capability Maturity Model Integration for Development (CMMI-DEV)][100]
> - [ISO/IEC 12207][101]
> - [ISO/IEC 15504][102]
> - [Melhoria de Processos de Software Brasileiro (MPS.BR)][103]
> - [Project Management Body of Knowledge (PMBOK)][104]
> - [Software Engineering Body of Knowledge (SWEBOK)][105]
> - E várias relacionadas às metodologias ágeis como [Scrum][8], [XP][106], [Kanban][9], [Lean][107], [FDD][108], [DSDM][109] etc.
>
> **Dica**: sobre as siglas acima, busque mais informações pela Internet. Você vai se surpreender com a quantidade de informações que existem sobre cada uma delas.
{: .notice--info}


Devido à experiência adquirida na implantação de melhoria de processos de desenvolvimento de software, pude escrever sobre o assunto em um livro. Se você se interessar, pode baixá-lo gratuitamente em [http://editora.ifpb.edu.br](http://editora.ifpb.edu.br/index.php/ifpb/catalog/book/7)

{%
    include figure
    image_path="/assets/images/lessons/intro09.png"
    alt="Livro"
    caption="Implantação de melhoria de processos de software com CMMI-DEV nível 2"
    url="http://editora.ifpb.edu.br/index.php/ifpb/catalog/book/7"
%}{: .align-center}

## Responsabilidade profissional do Engenheiro de Software

O engenheiro de software deve ter responsabilidade profissional, ou seja, deve ter consciência de que o seu trabalho pode afetar a vida de outras pessoas.

Deve-se observar sempre:

1. **Confidencialidade**: não divulgar informações confidenciais. A maioria dos projetos de desenvolvimento de software de uma empresa ou instituição são confidenciais. Não se deve divulgar informações sobre o projeto para pessoas que não fazem parte da equipe de desenvolvimento, nem mesmo após a saída do projeto ou da empresa. 
2. **Competência**: manter-se atualizado com as novas tecnologias e ferramentas de desenvolvimento de software. O engenheiro de software deve ter consciência de que o seu trabalho pode afetar a vida de outras pessoas. Por isso, deve ter conhecimento técnico e experiência profissional para desenvolver sistemas de software de qualidade.
3. **Direitos sobre propriedade intelectual**: você sabia que todo software criado em ambiente empresarial ou institucional quaisquer são patrimônio dela? Assim sendo, o software não é seu. Por isso, não se deve copiar, distribuir ou vender o software sem a autorização da empresa ou instituição, conforme consta na Lei de Software (Lei 9.609/1998) e na Lei de Direitos Autorais (Lei 9.610/1998).
4. **Mau uso de computadores**: não utilizar computadores para atividades ilegais, como invasão de sistemas, roubo de informações, distribuição de vírus, spam, phishing etc.

# Referências

- PRESSMAN, Roger S. Engenharia de Software. 6. ed. São Paulo: McGraw-Hill, 2006.
- Project Management Institute (PMI). Um guia do conhecimento em gerenciamento de projetos (Guia PMBOK). 6. ed. Pennsylvania: Project Management Institute, 2017.
- Sommerville. Engenharia de Software. 8ª ed. São Paulo: Pearson Addison-Wesley, 2007.
- ---. Guia de Implementação do MPS.Br nível F. Versão 1.1. SOFTEX, 2007.

[Voltar](/lessons/softeng/)

Criado Janeiro de 2019 e atualizado em Agosto de 2023 por *Maxwell Anderson*

[1]: <https://www.atlassian.com/br/software/jira> "Jira"
[2]: <https://trello.com/pt-BR> "Trello"
[3]: <https://docs.github.com/pt/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects> "GitHub Projects"
[4]: <https://helpx.adobe.com/br/support/xd.html> "Adobe XD"
[5]: <https://balsamiq.com/> "Balsamiq"
[6]: <https://www.office.com/> "Microsoft Office"
[7]: <https://www.google.com/docs/about/> "Google Docs"
[8]: <https://kanbanize.com/pt/recursos-kanban/primeiros-passos/o-que-e-kanban> "Kanban"
[9]: <https://aws.amazon.com/pt/what-is/scrum/> "Scrum"
[10]: <https://www.visual-paradigm.com/> "Visual Paradigm"
[11]: <https://astah.net/pt/> "Astah"
[12]: <https://sparxsystems.com/> "Enterprise Architech"
[13]: <https://www.figma.com/> "Figma"
[14]: <https://www.mysql.com/products/workbench/> "MySQL Workbench"
[15]: <https://www.oracle.com/br/database/sqldeveloper/technologies/sql-data-modeler/> "Oracle SQL Developer Data Modeler"
[16]: <https://dbmstools.com/tools/sql-power-architect> "SQL Power Architect"
[17]: <https://www.bizagi.com/pt/plataforma/modeler> "Bizagi Modeler"
[18]: <https://app.diagrams.net/> "Draw.io"
[19]: <https://www.microsoft.com/pt-br/microsoft-365/visio/flowchart-software> "Microsoft Visio"
[20]: <https://www.microsoft.com/pt-br/microsoft-365/project/project-management-software> "Microsoft Project"
[21]: <https://docs.google.com/spreadsheets> "Google Planilhas"
[22]: <https://git-scm.com/> "Git"
[23]: <https://github.com/> "GitHub"
[24]: <https://about.gitlab.com/> "Gitlab"
[25]: <https://bitbucket.org/> "Bitbucket"
[26]: <https://www.jenkins.io/> "Jenkins"
[27]: <https://www.travis-ci.com/> "Travis CI"
[28]: <https://circleci.com/> "Circle CI"
[29]: <https://www.selenium.dev/> "Selenium"
[30]: <https://www.cypress.io/> "Cypress"
[31]: <https://code.visualstudio.com/> "Visual Studio Code"
[32]: <https://www.jetbrains.com/pt-br/pycharm/> "PyCharm"
[33]: <https://www.eclipse.org/downloads/> "Eclipse"
[34]: <https://www.jetbrains.com/idea/> "IntelliJ IDEA"
[35]: <https://netbeans.apache.org/download/index.html> "Netbeans"
[36]: <https://testlink.org/> "Testlink"
[37]: <https://www.testrail.com/> "TestRail"
[38]: <https://jmeter.apache.org/> "JMeter"
[39]: <https://gatling.io/> "Gatling"
[40]: <https://owasp.org/> "OWASP"
[41]: <https://portswigger.net/burp> "Burp Suite"
[42]: <https://analytics.google.com/analytics/web/> "Google Analytics"
[43]: <https://www.sonarsource.com/products/sonarqube/> "SonarQube"
[44]: <https://gvasanka.medium.com/attack-cpu-memory-of-a-linux-machine-using-stress-and-stress-ng-commands-9a7aa1ee0a25> "Stress-ng"
[45]: <https://snyk.io/> "Snyk"
[46]: <https://www.mend.io/> "WhiteSource"
[47]: <https://codeclimate.com/> "Code Climate"
[48]: <https://about.codecov.io/> "Codecov"

[100]: <https://cmmiinstitute.com/> "CMMI-DEV"
[101]: <https://pt.wikipedia.org/wiki/ISO/IEC_12207> "ISO/IEC 12207"
[102]: <https://pt.wikipedia.org/wiki/ISO/IEC_15504> "ISO/IEC 15504"
[103]: <https://www.softex.br/wp-content/uploads/2013/07/MPS.BR_Guia_Geral_Software_2012-c-ISBN-1.pdf> "MPS.BR"
[104]: <https://pmisp.org.br/pmbok-guide/> "PMBOK"
[105]: <https://www.ieee.org/about/ieee-india/ieee-computer-society-india/swebok.html> "SWEBOK"
[106]: <https://asana.com/pt/resources/extreme-programming-xp> "XP"
[107]: <https://www.lean.org.br/o-que-e-lean.aspx> "Lean"
[108]: <https://pt.wikipedia.org/wiki/Feature_Driven_Development> "FDD"
[109]: <https://pt.wikipedia.org/wiki/Metodologia_de_desenvolvimento_de_sistemas_din%C3%A2micos> "DSDM"

