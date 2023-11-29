---
title: Visão de Casos de Uso
permalink: /lessons/softeng/design/views_usecase/
sidebar:
    nav: "softeng-design"


layout: single
author_profile: true
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_design06.png
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: create an image of a cat studying software engineering"
---

<center>
    <figure>
        <img src="/assets/images/gpt/cat_design06.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um projeto de software em UML. O gato deve estar usando roupas formais.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

# Introdução

A visão de casos de uso exibe as funcionalidades do sistema e como elas são percebidas pelos usuários enquanto atores que interagem com o sistema.

Os principais modelos a serem utilizados são:

- [Diagrama de casos de uso](uml_usecase.md)
- [Diagrama de atividades](uml_activities.md)
- [Diagrama de sequência](uml_sequences.md)
- Diagrama de comunicação
- Protótipos visuais de baixo ou alto nível de fidelidade

Deve ser entendida por:

- Clientes¹
- Designers
- Desenvolvedores
- Gerentes de projeto

¹ Embora os clientes possam não ter acesso ao diagrama de casos de uso - por algum motivo, hipoteticamente falando -, é crucial projetá-lo como se fosse destinado a ser visualizado por eles. Portanto, o diagrama de casos de uso deve ser concebido de maneira simples e facilmente compreensível, especialmente para esse contexto específico de visualização na UML.

## Utilização do Diagrama de Casos de Uso

Como você sabe, os requisitos funcionais definidos em [**Documento de Requisitos** de exemplo](https://github.com/maxwellamaral/maxwellamaral.github.io/blob/8f925f5c8882263f475162a990b5da48b6779a3d/specs/requirements/requirements.md) definem as funcionalidades que estarão presentes no sistema. E, para representar estas funcionalidades, utilizamos o diagrama de casos de uso.

O diagrama de casos de uso é um diagrama de comportamento que descreve as funcionalidades e como elas são percebidas pelos usuários enquanto atores que interagem com o sistema.

> ℹ️ **Nota**
>
> É muito importante que você compreenda o que eu disse acima. Quando eu mencionar a palavra **funcionalidade**, tente imaginar, hipoteticamente, que você está utilizando o sistema como usuário e que você vendo uma página. O que você poderá fazer? O que você poderá ver, alterar, adicionar, excluir, por exemplo?
>
> Você é o **ator** que interage com o sistema através dessa funcionalidade. Assim sendo, você é o **ator** que interage com o sistema através do **caso de uso**.
>
> Entender isto, vai trazer compreensão para o que o desenvolvedor irá fazer, pois ele irá implementar **o que** e **como o usuário irá interagir com o sistema**.

> ⚠️ **Atenção**
>
> Reveja o assunto relacionado a [Elicitação de Requisitos](/lessons/softeng/requirements/elicitation/) e ao [Diagrama de Casos de Uso](/lessons/softeng/design/uml_usecase/), se necessário. Não continue se ainda não tiver entendido estes assuntos.

### Como extrair casos de uso de requisitos funcionais?

Desta forma, vamos seguir as seguintes etapas para poder construir um diagrama de casos de uso:

1. **Identificar os atores**
   1. Dê uma olhada no **RF001** do [Documento de Requisitos](https://github.com/maxwellamaral/maxwellamaral.github.io/blob/8f925f5c8882263f475162a990b5da48b6779a3d/specs/requirements/requirements.md). Ele menciona o seguinte:

        >  *[RF001] - Como um cliente, eu gostaria de poder manter os produtos que eu compro e controlar as garantias, para que eu possa saber quando o produto estará fora de garantia. Os produtos devem ser cadastrados com os seguintes dados: nome do produto, data de compra, data de vencimento da garantia, segmento do produto, marca e modelo do produto, local de compra, valor pago pelo produto, valor da garantia e modo de compra (online ou físico).*

   2. Pergunte-se: quais são os atores envolvidos? 
   3. Uma forma de verificar os atores é identificando os **substantivos** presentes no requisito funcional. Alguns analistas preferem utilizar esta técnica, pois é mais fácil de identificar os atores. Eles leem cada requisito e anota ao lado os substantivos que aparecem. Depois, eles verificam se estes substantivos são atores ou não. Por que você não tenta isso agora? 😀
         
        Olhando este requisito, temos os substantivos:

        - Cliente
        - Produto
        - Garantia
        - Nome do produto
        - Data de compra
        - Data de vencimento da garantia
        - Segmento do produto
        - Marca e modelo do produto
        - Local de compra
        - Valor pago pelo produto
        - Valor da garantia
        - Modo de compra (online ou físico)
        
        Destes substantivos, quais são aqueles que são atores que interagem com a funcionalidade do sistema? Percebeu que somente o *Cliente* é o ator que interage com o sistema? Os demais substantivos são **dados** que o ator irá informar para o sistema. Assim sendo, o diagrama de casos de uso não irá representar estes substantivos, mas somente o ator *Cliente*.

        Foi identificado o *Cliente*, pois ele atua como usuário da funcionalidade de cadastro de produto, bem como poderá alterar, excluir e consultar os produtos cadastrados por ele, não é verdade? 

   5. Desenhe o ator *Cliente* no diagrama de casos de uso. Veja como o ator foi desenhado na próxima figura.

        [![Caso de Uso 01](https://tinyurl.com/2mszgurt)](https://tinyurl.com/2mszgurt)<!--![Caso de Uso 01](../../../../assets/puml/usecase_rf01.puml)-->
        <br>
        <small>
            Diagrama de Casos de Uso UC Manter Produto
        <br>
            Fonte: criação própria, em jun/2023
        </small>

   6. Você poderá ir desenhando os outros atores que forem identificados nos requisitos funcionais.

2. **Identifique o caso de uso**
   1. Uma forma de verificar os casos de uso é através da busca por **verbos** no requisito funcional que possam representar ações. Alguns analistas preferem utilizar esta técnica, pois é mais fácil de identificar os casos de uso. Eles leem cada requisito e anota ao lado os verbos que aparecem. Depois, eles verificam se estes verbos são casos de uso ou não. Por que você não tenta isso agora? 😀

        Olhando este requisito, temos os verbos:

        - Manter
        - Controlar
        - Saber
        - Ser
        - Estar
        - Dever

        Destes verbos, quais são aqueles que são candidatos a casos de uso? Faça a seguinte pergunta sobre o **RF001**: o verbo "Manter" é uma **funcionalidade** (**ação**) do sistema ou uma **etapa** de uma ação ou processo maior? Pode ser que não seja nenhum dos dois, mas uma **condição**, **regra** ou é somente um verbo auxiliar ou de ligação para tornar o texto mais compreensível.

        Aqui posso identificar que os verbos *manter* e *controlar* são candidatos a casos de uso, pois eles representam ações que o ator irá realizar no sistema. Assim sendo, o diagrama de casos de uso irá representar estes verbos. Os outros verbos não são candidatos a casos de uso, pois eles representam **etapas de uma ação** ou processo maior. Assim sendo, o diagrama de casos de uso não irá representar estes verbos, mas somente os verbos *manter* e *controlar*.


   2. Como mencionado, o Cliente poderá cadastrar, alterar, excluir e consultar os produtos cadastrados por ele. Assim sendo, "Manter" significa que o cliente poderá realizar todas estas ações. Assim sendo, a ação nos remete à funcionalidade e, por isto, é candidato a ser um caso de uso. Se fosse uma etapa de uma ação ou processo maior, seria descrito no fluxo principal, alternativo ou fluxo de exceção de um caso de uso descritivo.
   3. Desenhe o caso de uso "Manter Produto".
3. Identifique os relacionamentos entre os atores e os casos de uso
   1. O *Cliente* é o ator que interage com o caso de uso "Manter Produto".
   2. Desenhe o relacionamento entre o ator *Cliente* e o caso de uso "Manter Produtos".
4. O diagrama, inicialmente, deverá ficar assim:

    [![Caso de Uso 01](https://tinyurl.com/2mszgurt)](https://tinyurl.com/2mszgurt)<!--![Caso de Uso 01](../../../../assets/puml/usecase_rf01.puml)-->
    <br>
    <small>
        Diagrama de Casos de Uso UC Manter Produto
    <br>
        Fonte: criação própria, em jun/2023
    </small>

5. Continuando a análise sobre o mesmo requisito funcional **RF001**, o ator deverá "controlar as garantias, para que eu possa saber quando o produto estará fora de garantia".
   1. O ator *Cliente* interage com uma funcionalidade à parte. Com isso entendemos que um produto poderá possuir várias garantias, o que é verdade, pois temos a garantia normal, definida por lei, a garantia dada pelo fabricante e a garantia estendida.
   2. Assim sendo, o verbo "controlar" não é uma etapa adicional, mas uma funcionalidade que, inclusive, poderá ser executada por outras funcionalidades dentro do mesmo sistema. Como "controlar as garantias" se refere também a incluir, alterar, excluir e consultar as garantias do produto, podemos dizer que o correto é "manter garantias".
6. Desenhe o caso de uso "Manter garantia".
7. Identifique os relacionamentos entre atores e casos de usos, bem como entre casos de usos e casos de usos.
   1. Até o momento o ator não realiza uma ação direta, ou acessa diretamente a ação "Manter garantia", pois tem que passar pela ação "Manter produto" quando ele necessita realizar uma consulta ao produto antes de adicionar, alterar ou excluir uma garantia.
   2. Assim, podemos identificar uma ação **opcional** do ator *Cliente* para com o caso de uso "Manter Garantia". 
   3. Por que opcional? Porque o ator pode ou não realizar a ação de "Manter Garantia" agora, assim que ele executa a ação de "Manter Produtos".
   4. Desta forma, o relacionamento será entre os casos de usos "Manter Produto" e "Manter Garantia", como sendo uma **opcionalidade**. Desenhe o relacionamento com o estereótipo `<<extend>>`.
8. O diagrama, inicialmente, deverá ficar assim:

    [![Caso de Uso 02](https://tinyurl.com/26l5fywa)](https://tinyurl.com/26l5fywa)<!--![Caso de Uso 02](../../../../assets/puml/usecase_rf01_2.puml)-->
    <br>
    <small>
        Diagrama de Casos de Uso UC Manter Produto e UC Manter Garantia
    <br>
        Fonte: criação própria, em jun/2023
    </small>

### Diagrama geral de casos de uso do sistema

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

## Especificação dos Casos de Usos

A especificação dos casos de uso é uma descrição detalhada de cada caso de uso. Ela é utilizada para descrever os casos de uso que serão implementados. 

Assim, iremos descrever os detalhes de cada caso de uso, como o objetivo, os requisitos, os atores, as condições de entrada, o fluxo principal, os fluxos alternativos e os fluxos de exceção e, para isto, precisamos entender as **etapas** de um caso de uso.

> ℹ️ **Nota**
>
> Lembra que eu disse que um verbo encontrado em um requisito pode ser uma funcionalidade (ação) ou uma etapa de uma ação e que você deverá descobrir se é um ou outro? Pois bem, já que descobrimos quais são as ações e desenhamos as funcionalidades, agora iremos descrever as etapas de cada ação!

### Como extrair as etapas de um caso de uso?

Agora que temos o diagrama de casos de uso, vamos extrair as etapas de cada caso de uso. Para isto, poderemos utilizar uma das seguintes técnicas:

- Uma [especificação de casos de uso](#especificação-de-casos-de-uso), que é um documento que detalha cada caso de uso de maneira textual;
- Uma [história de usuário](#história-de-usuário), também textual, é bem parecido com a especificação de casos de uso, mas é mais simples, direto e muito útil para equipes ágeis que necessitam especificar histórias para casos de testes (meu preferido!); ou,
- Um [diagrama](#diagrama-de-atividades), que é um elemento visual que detalha as etapas de um caso de uso. Utilizo quando realmente eu preciso detalhar utilizando gráficos ou desenhos e não quero utilizar uma especificação textual, pois um desenho poderia representar melhor o entendimento dos passos necessários para a execução de um caso de uso.

Qual escolher? Depende do que você precisa. Se você precisa de uma especificação textual, utilize a especificação de casos de uso ou a história de usuário. Se você precisa de uma especificação visual, utilize o diagrama de atividades, de sequência ou comunicação.

> ℹ️ **Nota**
>
> Eu prefiro as histórias de usuário e, quando ela não é suficiente, substituo por um diagrama. Nunca deixe os dois (duas representações), pois se você precisar alterar uma, terá que alterar a outra também. E, se você não alterar, poderá ter problemas de inconsistência entre as duas representações. Evite redundâncias e faça somente aquilo que for útil para você e para os outros. 

#### <a id="especificacao">Especificação de casos de uso</a>

Bom, vamos especificar este caso de uso, ou seja, vamos detalhar o caso de uso "Manter Produto". Para fins de exemplificação e melhor entendimento, não irei especificar aqui o caso de uso "Manter Garantia".

>  *[RF001] - Como um cliente, eu gostaria de poder manter os produtos que eu compro e controlar as garantias, para que eu possa saber quando o produto estará fora de garantia. Os produtos devem ser cadastrados com os seguintes dados: nome do produto, data de compra, data de vencimento da garantia, segmento do produto, marca e modelo do produto, local de compra, valor pago pelo produto, valor da garantia e modo de compra (online ou físico).*

Veja que ao ler o requisito funcional RF001, podemos identificar as seguintes etapas contidas no fluxo principal:

<table>
  <tbody>
    <tr>
      <td><strong>Caso de uso</strong></td>
      <td><a id="uc1">UC1 - Manter Produto</a></td>
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

> ℹ️ **Nota**
>
> 1. Perceba que eu utilizei o termo "ator" e não "cliente" no passo a passo. Caso o nome do ator mude, não precisarei alterar a toda especificação do caso de uso (não queria fazer isto, vá por mim), pois o ator é um conceito abstrato. O que importa é o papel que o ator desempenha no sistema.
> 2. Veja que o título começa com um identificador "UC1". Este identificador é utilizado para referenciar o caso de uso em outros documentos, como por exemplo, em um documento de especificação de requisitos, de outros casos de uso, especificação de testes, textos de *commits* em repositórios de controle de versão etc. Assim, se eu quiser referenciar este caso de uso, basta eu escrever "UC1" e todos saberão que estou me referindo ao caso de uso "Manter Produto".

#### História de usuário

O exemplo de história de usuário poderá ser visualizado em [História de usuário da RF001](/lessons/softeng/tests/user_stories/).

Em todos os casos, o objetivo é o mesmo: detalhar as etapas de um caso de uso do RF001.

Este é o meu preferido, pois como gosto de usar o método TDD (veremos esse assunto depois), posso assim unir o útil ao agradável. 😁

> ℹ️ **Nota**
>
> Algumas empresas não necessitam de um documento de requisitos como visto anteriormente. Elas utilizam somente as histórias de usuário para especificar os requisitos. Assim sendo, para estes, a história de usuário é o documento de requisitos, podendo ser validado junto ao cliente, possuindo valor jurídico, legal e contratual.

#### Diagrama de atividades

Aqui estarei demonstrando como extrair as etapas de um caso de uso utilizando um diagrama de atividades.

##### Passos para criação de um diagrama de atividades

O diagrama de atividades é uma representação gráfica do comportamento do sistema, descrevendo suas ações em termos de atividades. Sua aplicação é na modelagem do fluxo de trabalho de um sistema. 

Caso necessário, recomenda-se revisar o conteúdo relacionado ao [Diagrama de Atividades](uml_activities.md).

Para extrair as etapas de um caso de uso, vamos seguir as seguintes etapas:

1. Identifique o caso de uso
   1. Vamos utilizar o caso de uso "Manter Produto" e "Manter garantia" como exemplos.
2. Verifique na descrição do requisito se existem etapas ou passos a serem realizados. Se existirem, desenhe-as no diagrama de atividades.
   1. Vamos utilizar o requisito funcional RF001 como exemplo.

        >  *[RF001] - Como um cliente, eu gostaria de poder manter os produtos que eu compro e controlar as garantias, para que eu possa saber quando o produto estará fora de garantia. Os produtos devem ser cadastrados com os seguintes dados: nome do produto, data de compra, data de vencimento da garantia, segmento do produto, marca e modelo do produto, local de compra, valor pago pelo produto, valor da garantia e modo de compra (online ou físico).*

   2. Durante a atividade de análise, você irá identificar que o verbo "manter", como dito anteriormente, significa que o cliente poderá cadastrar, alterar, excluir e consultar os produtos cadastrados por ele.
   3. Desenhe as etapas no diagrama de atividades. Tente fazer sozinho e depois veja o exemplo abaixo.

##### Diagrama de atividades UCS Manter Produto e Garantia

Nesta caso, estou somente representando o caso de uso "Manter Produto" e Garantias.

[![Caso de uso Manter Produtos e Garantias](https://tinyurl.com/2d8zfbw9)](https://tinyurl.com/2d8zfbw9)<!--![Caso de uso Manter Produtos e Garantias](../../../../assets/puml/activity_view01.puml)-->
<br>
<small>
    Diagrama de atividades das UCS Manter Produtos e Garantias
<br>
    Fonte: criação própria, em jun/2023
</small>

##### Diagrama de atividades UCS Manter Cliente

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
Criado em Janeiro de 2020 por *Maxwell Anderson*
