---
title: Visão Lógica
permalink: /lessons/softeng/design/views_logic/
sidebar:
    nav: "softeng-design"


layout: single
author_profile: true
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_design05.png
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: create an image of a cat studying software engineering"
---

<center>
    <figure>
        <img src="/assets/images/gpt/cat_design05.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um projeto de software em UML. O gato deve estar usando roupas formais.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

# Introdução

A visão lógica exibe a estrutura do sistema e como os componentes do sistema interagem entre si.

Ela mostra **COMO** as funcionalidades do sistema são projetadas e promovidas.

Os principais modelos que podem ser utilizados são:

- Para análise de estrutura estática
  - [Diagrama de classes](uml_classes.md)
  - Diagrama de objetos
- Para análise de comportamento dinâmico
  - Diagrama de máquina de estados
  - [Diagrama de atividades](uml_activities.md)

Deve ser entenda por:

- Designers
- Desenvolvedores

> ℹ️ **Nota**
>
> 1. Percebe que estou mencionando o uso de um diagrama de atividades aqui? Ele não foi utilizado na visão de casos de uso? Sim, ele foi utilizado na visão de casos de uso, mas ele também pode ser utilizado na visão lógica. Porém, ele será utilizado de uma forma diferente.
> 2. Na **visão de casos de us**o, ele foi utilizado para mostrar o fluxo de eventos de um caso de uso.
> 3. Na **visão lógica**, ele será utilizado para mostrar o fluxo de eventos de uma operação ou método de uma classe.
> 4. Portanto, ele será utilizado de uma forma diferente e com um propósito diferente, agora, **na visão do desenvolvedor!** E isso é o que você irá aprender aqui. Isso é muito legal! 😎
>
> Entendeu agora por que fazemos análise baseada em visões?

Você pode estar se perguntando:

- Possuo documentos de requisitos ou um backlog de requisitos, e agora?
- Fiz a pouco as especificações na visão de casos de uso, por onde devo começar?

Conseguimos extrair casos de usos e suas especificações através dos requisitos funcionais. Agora vamos extrair as classes, naturalmente, através das especificações de casos de usos.

# Como extrair as classes de uma especificação de caso de uso?

Vamos utilizar, para fins práticos, a [especificação de casos de uso do RF001](/lessons/softeng/design/views_usecase/#especificação-de-casos-de-uso) definida anteriormente. Para isto, tente colocá-lo em outra janela do seu navegador para fins de acompanhamento das explicações abaixo. Coloque as duas janelas lado a lado.

A heurística para identificação de classes é a seguinte:

1. Descrição de requisitos
2. Extrair substantivos
3. Tentativa de classes
4. Eliminar classes estranhas
5. Classes identificadas

Para extrair as classes de uma especificação de caso de uso, vamos seguir as seguintes etapas:

## Descrição de requisitos e extração de substantivos

Vamos identificar os substantivos da especificação <a href="/lessons/softeng/design/views_usecase/#uc1">UC1 - Manter Produto</a>, pois são candidatos aos nomes de **classes** e **atributos**.

1. Vamos nos ater somente ao fluxo principal, os fluxos alternativos e as regras de negócio da <a href="/lessons/softeng/design/views_usecase/#uc1">UC1</a>.
2. Realizando a análise da <a href="/lessons/softeng/design/views_usecase/#uc1">UC1</a>, verificamos os seguintes substantivos:

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
4. Lembre-se que estamos realizando a análise de um único caso de uso. Para um sistema real, você deverá analisar todos os casos de uso.
5. Ao analisar todos os casos de usos, não se deve repetir atributos que já estão na lista acima.

## Tentativa de classes e eliminação de classes estranhas

Agora iremos, a partir da lista acima, analisar quais são as classes e atributos do projeto.

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

## Classes identificadas

Aqui desenhe as classes utilizando uma ferramenta CASE UML de sua preferência.

1. Nesta primeira fase, ao termos identificados as classes e seus atributos, vamos desenhar o diagrama de classes.
2. A primeira versão do diagrama de classes está ficando assim:

   [![Diagrama de classes v1](https://tinyurl.com/23yqumvp)](https://tinyurl.com/23yqumvp)<!--![Diagrama de classes v1](../../../../assets/puml/class_view02_v1.puml)-->

  > ℹ️ **Nota**
  >
  > Os tipos dos atributos devem ser definidos pelo analista de acordo com seu entendimento sobre o domínio do problema, conforme a linguagem de programação que será utilizada e a arquitetura adotada do sistema, se existir. Caso não exista, deverá definir um padrão arquitetural.

3. Vamos realizar as análises dos outros casos de usos. 
4. Ao fim, poderemos ir adicionando os atributos para cada classe. O analista poderá, na ausência de um atributo, adicionar aqueles que fazem sentido. Por exemplo:

   1. A classe **Cliente** poderá ter os atributos **nome**, **email**, **telefone** e **endereço**. 
   1. As classes **Segmento de Produto**, **Marca**, **Modelo** e **Modo de Compra** poderão ter, em cada um, os atributos **nome** e **descrição**. 
   2. Desta forma, o diagrama irá evoluir como mostrado abaixo:

    [![Diagrama de classes v2](https://tinyurl.com/24uz36qj)](https://tinyurl.com/24uz36qj)<!--![Diagrama de classes v2](../../../../assets/puml/class_view02_v2.puml)-->

# Como identificar os métodos de uma classe?

Nesta próxima etapa, precisamos identificar o **comportamento** através da:

- leitura da especificação dos casos de uso;
- extração de verbos simples ou compostos;
- eliminação de redundâncias, generalidade, vaguidade e comportamentos que representam instâncias de classes, bem como aqueles desnecessários;
- disposição dos comportamentos extraídos nas classes identificadas

## Lista de identificação de operações ou métodos

Para isto, iremos criar outra lista para identificação de operações ou métodos:

1. Em RF001, verificamos que o verbo empregado é "manter produto", o que abrange o cadastro, alteração, exclusão e consulta de produtos. Portanto, podemos considerar que é uma operação de mais alto nível de abstração da classe Produto. Assim temos:

   - **manter** produto
     - **cadastrar** produto
     - **alterar** produto
     - **excluir** produto
     - **buscar** produto

2. Em <a href="/lessons/softeng/design/views_usecase/#uc1">UC1 - Cadastrar Produto</a>, temos os seguintes verbos:

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

5. Vamos alterar a lista acima a fim de realizar a identificação das operações que fazem sentido para cada classe, determinando o tipo de cada operação como *descartar, operação, desnecessário, redundante etc. Depois dê um nome à operação. A lista ficará assim:

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

## Determinação de operações ou métodos

1. As operações ou métodos identificados são:

- **Produto**
  - alterar_produto
  - buscar_produto
  - excluir_produto
  - exibir_produto
  - incluir_produto
  - listar_produto
  - validar_produto
  - exibir_mensagem     

2. Agora iremos incluir esses métodos na classe Produto. Sobre as outras classes, podemos decidir incluir métodos comuns de uma arquitetura CRUD. 
3. Os tipos de operações ou métodos e dos seus parâmetros devem ser definidos pelo analista de acordo com seu entendimento sobre o domínio do problema, conforme a linguagem de programação que será utilizada e a arquitetura adotada do sistema, se existir. Caso não exista, deverá definir um padrão arquitetural.
4. Irá ficar assim:

[![Diagrama de classes v3](https://tinyurl.com/2cayjezw)](https://tinyurl.com/2cayjezw)<!--![Diagrama de classes v3](../../../../assets/puml/class_view02_v3.puml)-->

<!-- # Como identificar os relacionamentos entre as classes?

Agora iremos identificar os relacionamentos entre as classes.

## Lista de identificação de relacionamentos

 -->


---
Criado em Janeiro de 2020 por *Maxwell Anderson*
