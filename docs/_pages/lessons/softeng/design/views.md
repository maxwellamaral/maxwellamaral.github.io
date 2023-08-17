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
    - [Como extrair casos de uso de requisitos funcionais?](#como-extrair-casos-de-uso-de-requisitos-funcionais)
      - [Diagrama geral de casos de uso do sistema](#diagrama-geral-de-casos-de-uso-do-sistema)
    - [Como extrair as etapas de um caso de uso?](#como-extrair-as-etapas-de-um-caso-de-uso)
      - [História de usuário](#história-de-usuário)
      - [Especificação de casos de uso](#especificação-de-casos-de-uso)
      - [Diagrama de atividades](#diagrama-de-atividades)
        - [Passos para criação de um diagrama de atividades](#passos-para-criação-de-um-diagrama-de-atividades)
        - [Diagrama de atividades UCS Manter Produtos e Garantias](#diagrama-de-atividades-ucs-manter-produtos-e-garantias)
        - [Diagrama de atividades UCS Manter Clientes](#diagrama-de-atividades-ucs-manter-clientes)
- [Visão lógica](#visão-lógica)
  - [Arquitetura do sistema](#arquitetura-do-sistema)
  - [Como extrair as classes de uma especificação de caso de uso?](#como-extrair-as-classes-de-uma-especificação-de-caso-de-uso)

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

Como você sabe, os requisitos funcionais definidos em **Documento de Requisitos** no [exemplo](https://github.com/maxwellamaral/maxwellamaral.github.io/blob/8f925f5c8882263f475162a990b5da48b6779a3d/specs/requirements/requirements.md) definem as funcionalidades que estarão presentes no sistema. E, para representar estas funcionalidades, utilizamos o diagrama de casos de uso.

O diagrama de casos de uso é um diagrama de comportamento que descreve as funcionalidades do sistema e como elas são percebidas pelos usuários enquanto atores que interagem com o sistema. Reveja o assunto relacionado ao Diagrama de Casos de Uso, se necessário.

### Como extrair casos de uso de requisitos funcionais?

Desta forma, vamos seguir as seguintes etapas para poder construir um diagrama de casos de uso:

1. Identificar os atores
   1. Dê uma olhada no **RF001** do [Documento de Requisitos](https://github.com/maxwellamaral/maxwellamaral.github.io/blob/8f925f5c8882263f475162a990b5da48b6779a3d/specs/requirements/requirements.md). Quais são os atores envolvidos?
   2. Foi identificado o Cliente, pois ele atua como usuário da funcionalidade de cadastro de produto, bem como poderá alterar, excluir e consultar os produtos cadastrados por ele. 
   3. Desenhe o ator "Cliente" no diagrama de casos de uso. 
   4. Você poderá ir desenhando os outros atores que forem identificados nos requisitos funcionais.
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

    [![Caso de Uso 02](https://tinyurl.com/26l5fywa)](https://tinyurl.com/26l5fywa)<!--![Caso de Uso 02](../../../../assets/puml/usecase_rf01_2.puml)-->
    <br>
    <small>
        Diagrama de Casos de Uso UC Manter Produto e UC Manter Garantias
    <br>
        Fonte: criação própria, em jun/2023
    </small>

#### Diagrama geral de casos de uso do sistema

Após a realização deste procedimento sobre cada requisito funcional, o diagrama de casos de uso ficará assim:

> ℹ️ **Nota**
>
> O diagrama de caso de uso abaixo modela o requisito funcional RF001 até o RF007 do [Documento de Requisitos](/lessons/softeng/requirements/req/sample/) validado junto ao cliente.

[![Caso de Uso 02](https://tinyurl.com/23rzn9nj)](https://tinyurl.com/23rzn9nj)<!--![Caso de Uso 02](../../../../assets/puml/usecase_view.puml)-->
<br>
<small>
    Diagrama de casos de uso
<br>
    Fonte: criação própria, em jun/2023
</small>

### Como extrair as etapas de um caso de uso?

Agora que temos o diagrama de casos de uso, vamos extrair as etapas de cada caso de uso. Para isto, poderemos utilizar uma ou mais das seguintes técnicas:

- Uma **história de usuário**, que é bem parecido com a especificação de casos de uso, mas é mais simples, direto e muito útil para equipes ágeis que necessitam especificar histórias para casos de testes (meu preferido!); ou,
- Uma **especificação de casos de uso**, que é um documento que detalha cada caso de uso;
- Um **diagrama de atividades**, que é um diagrama que detalha as etapas de um caso de uso. Utilizo quando realmente eu preciso detalhar as etapas de um caso de uso, mas não quero utilizar uma especificação de casos de uso ou uma história de usuário, pois um desenho poderia representar melhor o entendimento dos passos necessários para a execução de um caso de uso.

#### História de usuário

Antes de tudo, algumas observações:

- O exemplo de história de usuário poderá ser visualizado em [História de usuário da RF001](/lessons/softeng/tests/user_stories/).
- As outras duas técnicas poderão ser visualizadas a seguir.
- Em todos os casos, o objetivo é o mesmo: detalhar as etapas de um caso de uso do RF001.

#### <a id="especificao">Especificação de casos de uso</a>

Bom, vamos especificar este caso de uso, ou seja, vamos detalhar o caso de uso "Manter Produtos". Para fins de exemplificação e melhor entendimento, não irei especificar aqui o caso de uso Manter Garantias.

<table>
  <tbody>
    <tr>
      <td><strong>Caso de uso</strong></td>
      <td><a id="uc1">UC1 - Manter Produtos</a></td>
    </tr>
    <tr>
      <td><strong>Objetivo</strong></td>
      <td>Permitir que o cliente efetue o cadastro, alteração, exclusão e consulta de produtos.</td>
    </tr>
    <tr>
        <td><strong>Requisitos</strong></td>
        <td>RF001</td>
    </tr>
    <tr>
        <td><strong>Atores</strong></td>
        <td>Cliente</td>
    </tr>
    <tr>
        <td><strong>Condição de entrada</strong></td>
        <td>O ator seleciona 'Produtos' no dashboard.</td>
    </tr>
    <tr>
        <td><strong>Fluxo principal</strong></td>
        <td>
            <ol>
            <li>O ator acessa a página de cadastro de produtos. Ele verifica que o título da página na aba do navegador e na própria página é 'Cadastro de produtos'. Ele observa que existe um campo para: 
                <ul>
                <li>nome do produto</li>
                <li>data de compra</li>
                <li>data de vencimento da garantia</li>
                <li>segmento do produto</li>
                <li>marca e modelo do produto</li>
                <li>local de compra</li>
                <li>valor pago pelo produto</li>
                <li>valor da garantia</li>
                <li>modo de compra (online ou físico)</li>
                <li>opções:
                    <ul>
                    <li>cadastrar</li>
                    <li>cancelar</li>
                    </ul>
                </li>
                </ul>
            </li>
            <li>O ator preenche os campos com os dados do produto que ele deseja cadastrar e seleciona o botão para cadastrar o produto. <a id="a2">[A2]</a>, <a id="a3">[A3]</a></li>
            <li>O sistema verifica se as informações para cadastro são válidas. <a id="rn1">[RN1]</a></li>
            <li>O sistema exibe a página de cadastro de produtos novamente e mostra uma mensagem informando que o produto foi cadastrado com sucesso.</li>
            <li>O ator seleciona 'Listar produtos' no menu.</li>
            <li>O sistema exibe uma a lista de produtos cadastrados.</li>
            <li>O ator verifica que o produto cadastrado está na lista.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td><strong>Fluxos alternativos</strong></td>
        <td>
            <a id="a1">A1 - Buscar produto</a>
            <ol>
                <li>O ator necessita realizar uma busca por produtos na lista. Seleciona o campo específico para busca e digita o nome do produto.</li>
                <li>O ator selecionar 'Buscar'.</li>
                <li>O sistema exibe todos os produtos que correspondem aos termos que foram digitados.</li>
            </ol>
            <a id="a2">A2 - Editar produto</a>
            <ol>
                <li>O ator executa <a href="#a1">[A1]</a>.</li>
                <li>O ator seleciona o produto na lista e clica no botão para editar o produto.</li>
                <li>Sistema exibe a página de edição de produtos e que os campos estão preenchidos com os dados do produto.</li>
                <li>O ator altera o nome do produto e clica no botão para salvar os dados relacionados ao produto.</li>
                <li>Sistema salva os dados.</li>
                <li>O ator seleciona 'Listar produtos' no menu.</li>
                <li>O sistema exibe uma a lista de produtos cadastrados.</li>
                <li>O ator verifica que o produto cadastrado está na lista.</li>
            </ol>
            <a id="a3">A3 - Excluir produto</a>
            <ol>
                <li>O ator decide excluir o produto e executa <a href="#a1">[A1]</a>. Ele visualiza o produto e seleciona a opção 'Excluir'.</li>
                <li>O sistema pergunta se o usuário realmente deseja excluir o produto.</li>
                <li>O ator confirma a exclusão.</li>
                <li>O sistema exclui o produto.</li>
                <li>O ator seleciona 'Listar produtos' no menu.</li>
                <li>O sistema exibe uma a lista de produtos cadastrados.</li>
                <li>O ator verifica que o produto cadastrado não está na lista.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td><strong>Fluxos de exceção</strong></td>
        <td>
            <a id="rn1">RN1 - Validação de campos</a>
            <p>Todas as informações são obrigatórias, exceto o campo 'valor da garantia'</p>
        </td>
    </tr>
  </tbody>
</table>

#### Diagrama de atividades
##### Passos para criação de um diagrama de atividades

O diagrama de atividades é um diagrama de comportamento que descreve o comportamento do sistema em termos de atividades. Ele é utilizado para modelar o fluxo de trabalho de um sistema. Reveja o assunto relacionado ao Diagrama de Atividades, se necessário.

Para extrair as etapas de um caso de uso, vamos seguir as seguintes etapas:

1. Identifique o caso de uso
   1. Vamos utilizar o caso de uso "Manter Produtos" como exemplo.
2. Verifique na descrição do requisito se exitem etapas ou passos a serem realizados. Se existirem, desenhe-as no diagrama de atividades.
   1. Vamos utilizar o requisito funcional RF001 como exemplo.
   2. Durante a atividade de análise, você irá identificar que o termo "Manter", como dito anteriormente, significa que o cliente poderá cadastrar, alterar, excluir e consultar os produtos cadastrados por ele.
   3. Desenhe as etapas no diagrama de atividades.

##### Diagrama de atividades UCS Manter Produtos e Garantias

Nesta caso, estou somente representando o caso de uso Manter Produtos e Garantias.

[![Caso de uso Manter Produtos e Garantias](https://tinyurl.com/2d8zfbw9)](https://tinyurl.com/2d8zfbw9)<!--![Caso de uso Manter Produtos e Garantias](../../../../assets/puml/activity_view01.puml)-->
<br>
<small>
    Diagrama de atividades das UCS Manter Produtos e Garantias
<br>
    Fonte: criação própria, em jun/2023
</small>

##### Diagrama de atividades UCS Manter Clientes

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

---
# Visão lógica

A visão lógica exibe a estrutura do sistema e como os componentes do sistema interagem entre si.

Ela mostra **como** as funcionalidades do sistema são projetados e promovidos.

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

- Possuo documentos de requisitos ou um backlog de requisitos, e agora?
- Possuo especificações na visão de casos de uso, por onde devo começar?

Conseguimos extrair casos de usos e suas especificações através dos requisitos funcionais. Agora vamos extrair as classes, naturalmente, através das especificações de casos de usos.

## Como extrair as classes de uma especificação de caso de uso?

Vamos utilizar, para fins práticos, a [especificação de casos de uso do RF001](#especificacao) definida anteriormente. Para isto, tente colocá-lo em outra janela do seu navegador para fins de acompanhamento das explicações abaixo. Coloque as duas janelas lado-a-lado.

Heurística para identificação de classes

1. Descrição de requisitos
2. Extrair substantivos
3. Tentativa de classes
4. Eliminar classes estranhas
5. Classes identificadas

Para extrair as classes de uma especificação de caso de uso, vamos seguir as seguintes etapas:

1. **Descrição dos requisitos:** vamos identificar os substantivos da especificação <a href="uc1">UC1 - Manter Produtos</a>, pois são candidatos aos nomes de **classes** e **atributos**.
   1. Vamos nos ater somente ao fluxo principal, os fluxos alternativos e as regras de negócio da <a href="uc1">UC1</a>.
   2. Realizando a análise da <a href="uc1">UC1</a>, verificamos os seguintes substantivos:
        | Substantivo                    | Tipo |
        | ------------------------------ | ---- |
        | cliente                        |      |
        | produto                        |      |
        | nome do produto                |      |
        | data de compra                 |      |
        | data de vencimento da garantia |      |
        | segmento de produto            |      |
        | marca                          |      |
        | modelo                         |      |
        | local de compra                |      |
        | valor pago do produto          |      |
        | valor da garantia              |      |
        | modo de compra                 |      |
   3. Perceba que após a análise do caso de uso, não encontramos mais nenhum nome, mas somente ações. Em um passo posterior, iremos reler novamente o caso de uso a fim de buscar essas ações, pois elas podem ser candidatas a métodos de classes.
   4. Lembre-se que estamos realizando a análise de somente um caso de uso. Para um sistema real, você deverá analisar todos os casos de uso.
   5. Ao analisar todos os casos de usos, não se deve repetir atributos que já estão na lista.
2. **Tentativa de classes**: agora iremos, a partir da lista acima, quais são as classes e atributos do projeto.
   1. Criamos uma nova lista, ou vamos modificar a mesma lista, e iremos classificar os substantivos em classes, atributos e descartados.
      1. **cliente**: é uma entidade, portanto, é uma classe, pois através dele eu poderei realizar ações, como por exemplo, cadastrar, alterar, excluir e consultar clientes. Já temos nossa primeira classe.
      2. **produto**: é uma entidade, portanto, é uma classe, seguindo o mesmo raciocínio anterior.
      3. **nome do produto**: é um atributo, pois é uma característica do produto. O mesmo podemos observar, na sequência, para **data de compra**, **data de vencimento da garantia**.
      4. **segmento de produto** é considerado um atributo de produto, pois é uma característica do produto. Porém, podemos **também** considerar que é uma classe, pois podemos realizar ações como cadastrar, alterar, excluir e consultar segmentos de produtos. Sabemos que o segmento de produto irá se relacionar com a classe produto, portanto, podemos considerar também que é uma classe. O mesmo raciocínio podemos aplicar para **marca** e **modelo**.
      5. **local de compra** é um atributo, pois é uma característica do produto. O mesmo podemos observar, na sequência, para **valor pago do produto** e **valor da garantia**.
      6. **modo de compra** é especificado com opções: *online* e *físico*. Portanto, podemos considerar que é um atributo, pois é uma característica do produto. Porém, podemos **também** considerar que é uma classe, pois podemos realizar ações como cadastrar, alterar, excluir e consultar modos de compras. Sabemos que o modo de compra irá se relacionar com a classe produto, portanto, podemos considerar também que é uma classe.
   2. A nova lista ficará assim:
        | Substantivo                    | Tipo                |
        | ------------------------------ | ------------------- |
        | cliente                        | classe              |
        | produto                        | classe              |
        | nome do produto                | atributo de Produto |
        | data de compra                 | atributo de Produto |
        | data de vencimento da garantia | atributo de Produto |
        | segmento de produto            | classe              |
        | marca                          | classe              |
        | modelo                         | classe              |
        | local de compra                | atributo de Produto |
        | valor pago do produto          | atributo de Produto |
        | valor da garantia              | atributo de Produto |
        | modo de compra                 | classe              |
   3. Você pode perguntar: "onde estão os atributos das classes Cliente, Segmento de Produto, Marca, Modelo e Modo de Compra?". Lembre-se que não realizamos ainda a análise dos outros casos de usos neste exercício prático. Com certeza, a medida que fossemos avançando, iríamos encontrar mais classes e mais atributos para estas classes.
   4. Não temos nenhum substantivo descartado, pois todos os substantivos foram classificados.
3. **Classes identificadas**: aqui vamos desenhar as classes utilizando uma ferramenta CASE UML.
   1. Nesta primeira fase, ao termos identificados as classes e seus atributos, vamos desenhar o diagrama de classes.
   2. A primeira versão do diagrama de classes está ficando assim:
   
      [![Diagrama de classes v1](https://tinyurl.com/23yqumvp)](https://tinyurl.com/23yqumvp)<!--![Diagrama de classes v1](../../../../assets/puml/class_view02_v1.puml)-->
 
   3. Agora poderemos ir adicionando os atributos que fazem sentido para cada classe. Por exemplo:
      1. A classe **Cliente** poderá ter os atributos **nome**, **e-mail**, **telefone** e **endereço**. 
      2. As classes **Segmento de Produto**, **Marca**, **Modelo** e **Modo de Compra** poderão ter, em cada um, os atributos **nome** e **descrição**. 
      3. Desta forma, o diagrama irá evoluir como mostrado abaixo:
   
       [![Diagrama de classes v2](https://tinyurl.com/24uz36qj)](https://tinyurl.com/24uz36qj)<!--![Diagrama de classes v2](../../../../assets/puml/class_view02_v2.puml)-->

4. Nesta próxima etapa, precisamos identificar o **comportamento** através da:
    - leitura da especificação dos casos de uso;
    - extração de verbos simples ou compostos;
    - eliminação de redundâncias, generalidade, vaguidade e comportamentos que representam instâncias de classes, bem como aqueles desnecessários;
    - disposição dos comportamentos extraídos nas classes identificadas.

    1. Para isto, iremos criar outra lista para identificação de operações. 
    2. Em RF001, verificamos que o verbo empregado é "manter produto", o que abrange o cadastro, alteração, exclusão e consulta de produtos. Portanto, podemos considerar que é uma operação de mais alto nível de abstração da classe Produto. Assim temos:
        - **manter** produto
          - **cadastrar** produto
          - **alterar** produto
          - **excluir** produto
          - **buscar** produto
    3. Em <a href="uc1">UC1 - Cadastrar Produto</a>, temos os seguintes verbos:
        - **preencher** os campos com os dados dos produtos;
        - **cadastrar** o produto;
        - **verificar** se o produto foi cadastrado com sucesso;
        - **exibir** mensagem informando que o produto foi cadastrado com sucesso;
        - **selecionar** listagem de produtos;
        - **exibir** lista de produtos;
        - **verificar** se o produto está na lista.
        - **buscar** produtos na lista;
        - **selecionar** campo específico para busca;
        - **selecionar** buscar;
        - **exibir** lista de produtos encontrados;
        - **selecionar** produtos da lista;
        - **editar** dados do produto;
        - **exibir** detalhes do produto selecionado;
        - **salvar** dados alterados do produto;
        - **excluir** produto;
        - **confirmar** exclusão do produto;
        - **verificar** se o produto foi excluído com sucesso;
        - **validar** salvamento dos dados do produto.        
    4. Esta lista ficará inicialmente assim:
        | Verbos                                                                  | Tipo | Operação |
        | ----------------------------------------------------------------------- | ---- | -------- |
        | **preencher** os campos com os dados dos produtos                       |      |          |
        | **cadastrar** o produto                                                 |      |          |
        | **verificar** se o produto foi cadastrado com sucesso                   |      |          |
        | **exibir** mensagem informando que o produto foi cadastrado com sucesso |      |          |
        | **selecionar** listagem de produtos                                     |      |          |
        | **exibir** lista de produtos                                            |      |          |
        | **verificar** se o produto está na lista                                |      |          |
        | **buscar** produtos na lista                                            |      |          |
        | **selecionar** campo específico para busca                              |      |          |
        | **selecionar** buscar                                                   |      |          |
        | **exibir** lista de produtos encontrados                                |      |          |
        | **selecionar** produtos da lista                                        |      |          |
        | **editar** dados do produto                                             |      |          |
        | **exibir** detalhes do produto selecionado                              |      |          |
        | **salvar** dados alterados do produto                                   |      |          |
        | **excluir** produto                                                     |      |          |
        | **confirmar** exclusão do produto                                       |      |          |
        | **verificar** se o produto foi excluído com sucesso                     |      |          |
        | **validar** salvamento dos dados do produto                             |      |          |

    5. Vamos alterar a lista acima a fim de realizar a identificação das operações que fazem sentido para cada classe.
        | Verbos                                                                  | Tipo                | Operação        |
        | ----------------------------------------------------------------------- | ------------------- | --------------- |
        | **preencher** os campos com os dados dos produtos                       | descartar           |                 |
        | **cadastrar** o produto                                                 | operação de Produto | incluir_produto |
        | **verificar** se o produto foi cadastrado com sucesso                   | operação de Produto | validar_produto |
        | **exibir** mensagem informando que o produto foi cadastrado com sucesso | operação de Produto | exibir_mensagem |
        | **selecionar** listagem de produtos                                     | desnecessário       |                 |
        | **exibir** lista de produtos                                            | operação de Produto | listar_produto  |
        | **verificar** se o produto está na lista                                | operação de Produto | buscar_produto  |
        | **buscar** produtos na lista                                            | operação de Produto | buscar_produto  |
        | **selecionar** campo específico para busca                              | desnecessário       |                 |
        | **selecionar** buscar                                                   | descartar           |                 |
        | **exibir** lista de produtos encontrados                                | redundante          |                 |
        | **selecionar** produtos da lista                                        | descartar           |                 |
        | **editar** dados do produto                                             | operação de Produto | alterar_produto |
        | **exibir** detalhes do produto selecionado                              | operação de Produto | exibir_produto  |
        | **salvar** dados alterados do produto                                   | descartar           |                 |
        | **excluir** produto                                                     | operação de Produto | excluir_produto |
        | **confirmar** exclusão do produto                                       | redundante          |                 |
        | **verificar** se o produto foi excluído com sucesso                     | redundante          |                 |
        | **validar** salvamento dos dados do produto                             | redundante          |                 |
5. **Operações identificadas**: as operações ou métodos identificados são:
    - **Produto**
      - alterar_produto
      - buscar_produto
      - excluir_produto
      - exibir_produto
      - incluir_produto
      - listar_produto
      - validar_produto
      - exibir_mensagem     
  
6. Agora iremos incluir esses métodos na classe Produto. Sobre as outras classes, podemos decidir incluir métodos comuns de uma arquitetura CRUD. Irá ficar assim:

    [![Diagrama de classes v3](https://tinyurl.com/2cayjezw)](https://tinyurl.com/2cayjezw)<!--![Diagrama de classes v3](../../../../assets/puml/class_view02_v3.puml)-->

