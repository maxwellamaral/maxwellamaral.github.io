---
layout: home
author_profile: true
title: UML
permalink: /lessons/softeng/design/uml/
sidebar:
    nav: "softeng-design"
---
Criado em Junho de 2023 por *Maxwell Anderson*

<center>
    <figure>
        <img src="../../../../assets/images/gpt/cat_design03.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um projeto de software em UML. O gato deve estar usando roupas formais.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

## Conteúdo

- [Introdução a UML](#introdução-a-uml)
- [Diagrama de casos de uso](#diagrama-de-casos-de-uso)
  - [Atores](#atores)
  - [Caso de uso](#caso-de-uso)
  - [Diagrama completo](#diagrama-completo)
    - [O caso de uso (elipse)](#o-caso-de-uso-elipse)
      - [Como identificar?](#como-identificar)
      - [Como diagramar?](#como-diagramar)
        - [Relacionamentos](#relacionamentos)
          - [Relacionamento entre atores e casos de uso](#relacionamento-entre-atores-e-casos-de-uso)
          - [Relacionamento entre atores e atores](#relacionamento-entre-atores-e-atores)
        - [Relacionamento entre casos de uso e casos de uso](#relacionamento-entre-casos-de-uso-e-casos-de-uso)
      - [Especificação de caso de uso](#especificação-de-caso-de-uso)
- [Diagrama de classes](#diagrama-de-classes)
  - [Associações](#associações)
    - [Unária ou reflexiva](#unária-ou-reflexiva)
    - [Binária](#binária)
    - [Binária com multiplicidade](#binária-com-multiplicidade)
    - [Generalização e especialização](#generalização-e-especialização)


# Introdução a UML

A Unified Modeling Language (UML) é uma linguagem de modelagem de software que permite que os engenheiros representem o sistema de várias formas, sob várias perspectivas. Ela é composta por vários diagramas que podem ser usados para modelar diferentes aspectos do sistema.

<center>
    <figure>
        <img src="../../../../assets/images/lessons/design03.png" width=500 alt="Diagramas UML">
        <figcaption>
            Diagramas UML
        </figcaption>
        <small>Fonte: elaboração própria (2010)</small>
    </figure>
</center>

É a linguagem padrão para modelagem de software e é usada por engenheiros de software em todo o mundo. Ela é composta por vários diagramas que podem ser usados para modelar diferentes aspectos do sistema.

Surgiu da união de três linguagens de modelagem de software: Booch, OMT e OOSE. A UML foi criada por Grady Booch, Ivar Jacobson e James Rumbaugh na década de 1990. 

A documentação pode ser encontrada em [https://www.uml.org/](https://www.uml.org/)

# Diagrama de casos de uso

O diagrama de casos de uso é um dos diagramas mais importantes da UML. Ele é usado para modelar os requisitos funcionais do sistema. Ele mostra os atores e os casos de uso do sistema e como eles interagem entre si.

## Atores

Um ator é uma pessoa ou sistema que interage com o sistema. Ele pode ser um usuário, um sistema externo ou um dispositivo externo. Os atores são representados por ícones de pessoas ou sistemas externos.

Exemplos de atores:

- Cliente
- Funcionário
- Vendedor
- Administrador
- Usuário comum
- Sistema de emissão de notas fiscais
- Sistema de pagamento

Diagramando atores:

[![Exemplo de atores](http://tinyurl.com/2y7zr9hr)](http://tinyurl.com/2y7zr9hr)<!--![Exemplo de atores](../../../../assets/puml/uml_usecase01.puml)-->
<br>
<small>Exemplo de atores</small>
<br>
<small>Fonte: elaboração própria (2023)</small>


As setas representam uma relação de generalização/especialização. Por exemplo, o ator `Operador de programação da afiliada` é um tipo de `Operador de sistema` e `Conselho de programação` também é um tipo de `Operador de sistema`.

[![Exemplo de atores](http://tinyurl.com/2cx9jf3g)](http://tinyurl.com/2cx9jf3g)<!--![Exemplo de atores](../../../../assets/puml/uml_usecase02.puml)-->
<br>
<small>Exemplo de atores</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Aqui, o ator `Cliente` é um tipo de `Usuário comum`. O ator `Funcionário` é um tipo de `Usuário comum`. Este tipo de representação é bem comum em arquitetura de sistemas de software em geral.

## Caso de uso

Um caso de uso é uma funcionalidade do sistema. Ele representa uma ação que o sistema pode realizar. Ele é representado por uma elipse.

Exemplos de casos de uso:

- Cadastrar cliente
- Alterar cliente
- Excluir cliente
- Buscar cliente

> ℹ️ **Nota**
>
> Os casos de uso devem iniciar com verbos no infinitivo.
>
> No exemplo acima temos os verbos `Cadastrar`, `Alterar`, `Excluir` e `Buscar`. É um CRUD clássico. CRUD é um acrônimo para Create, Read, Update e Delete. Em português: Criar, Ler, Atualizar e Excluir.
>
> Assim sendo, é comum que os quatro casos de uso sejam um só representados como `Manter cliente`.

Diagramando casos de uso:

[![Exemplo de casos de uso](http://tinyurl.com/28y3k424)](http://tinyurl.com/28y3k424)<!--![Exemplo de casos de uso](../../../../assets/puml/uml_usecase03.puml)-->
<br>
<small>Exemplo de casos de uso/small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Aqui temos um exemplo de casos de uso `Cadastrar cliente`, `Alterar cliente`, `Excluir cliente` e `Buscar cliente`.

[![Exemplo de casos de uso](http://tinyurl.com/2y2ar3n8)](http://tinyurl.com/2y2ar3n8)<!--![Exemplo de casos de uso](../../../../assets/puml/uml_usecase04.puml)-->
<br>
<small>Exemplo de casos de uso</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Conforme nota acima, alteramos os casos de uso para `Manter cliente`.

## Diagrama completo

Agora que já sabemos como representar atores e casos de uso, podemos criar um diagrama completo.

Ele serve para identificar a fronteira do sistema, ou seja, o seu escopo:

- Identificando atores
- Identificando casos de uso
- Descrevendo casos de uso
- Relacionando os casos de uso
- Especificando partes ou módulos do sistema

Vamos ver tudo isto com mais detalhes agora.

### O caso de uso (elipse)

Regras:

- O caso de uso é representado por uma elipse. 
- Pode representar um serviço, uma funcionalidade ou uma ação que o sistema pode realizar.
- Pode ser utilizado por um mais atores.
- Pode também ser utilizado por outros casos de usos.

#### Como identificar?

Para identificar casos de uso, devemos ler os requisitos funcionais levantados em etapas anteriores e fazer as seguintes perguntas:

- **Quais os serviços ou funcionalidades** que os atores querem do sistema?
- O sistema **armazena informações**?
- Quais atores **utilizam** o sistema, de forma a **criar**, **ler**, **atualizar** ou **excluir** informações?
- Qual ator **inicia** o caso de uso?
- Qual ator **informa** os dados para o caso de uso? (lembre-se que o ator pode ser um sistema externo ou um dispositivo externo)
- O sistema necessita **informar** algo para o ator?
- Existe algum **processamento** de dados externo que o sistema deva saber?

#### Como diagramar?

Após identificado os atores e os casos de uso, para diagramar casos de uso, devemos fazer o seguinte:

1. Desenhar os atores
2. Desenhar os casos de uso

  [![Exemplo de atores e casos de uso](http://tinyurl.com/29vzcy6t)](http://tinyurl.com/29vzcy6t)<!--![Exemplo de atores e casos de uso](../../../../assets/puml/uml_usecase05.puml)-->
  <br>
  <small>Exemplo de atores e casos de uso</small>
  <br>
  <small>Fonte: elaboração própria (2023)</small>

3. Estabelecer os relacionamentos entre:
   - atores e casos de uso
   - atores e atores
   - casos de uso e casos de uso
  
Vamos ver como estabelecer os relacionamentos entre esses componentes.

##### Relacionamentos

Podemos organizar os relacionamentos em três grupos de forma lógica e incremental:

- **Relacionamento entre atores e casos de uso**
  - O ator **utiliza** o caso de uso
  - O ator **inicia** o caso de uso
  - O ator **informa** dados para o caso de uso
  - O caso de uso **informa** algo para o ator
- **Relacionamento entre atores e atores**
  - O ator é um **tipo** de outro ator
- **Relacionamento entre casos de uso e casos de uso**
  - O caso de uso **utiliza** outro caso de uso
  - O caso de uso **estende** outro caso de uso
  - O caso de uso **inclui** outro caso de uso
  - O caso de uso é um **tipo** de outro caso de uso

###### Relacionamento entre atores e casos de uso

Demonstra que o ator utiliza (ou *"usa"*) a funcionalidade do sistema (caso de uso). Ficaria estranho dizer que o "ator usa o caso de uso", mas é assim que funciona.

Utilizamos uma linha "cheia" para representar este relacionamento.

Utilizamos um retângulo em volta dos casos de uso para representar o escopo do sistema - delimitando suas fronteiras ou mesmo pode ser utilizado para representar um módulo do sistema.

[![Relacionamento entre atores e casos de uso](http://tinyurl.com/2bbe328p)](http://tinyurl.com/2bbe328p)<!--![Relacionamento entre atores e casos de uso](../../../../assets/puml/uml_usecase06.puml)-->
<br>
<small>Relacionamento entre atores e casos de uso</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

###### Relacionamento entre atores e atores

Entre atores, um pode ser um tipo de outro. 

As setas representam uma relação de generalização/especialização. Por exemplo, o ator `Operador de programação da afiliada` é um tipo de `Operador de sistema` e `Conselho de programação` também é um tipo de `Operador de sistema`.

[![Relacionamento entre atores e atores](http://tinyurl.com/22aypusa)](http://tinyurl.com/22aypusa)<!--![Relacionamento entre atores e atores](../../../../assets/puml/uml_usecase07.puml)-->
<br>
<small>Relacionamento entre atores e atores</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

##### Relacionamento entre casos de uso e casos de uso

- **Relacionamento de inclusão**: um caso de uso pode incluir outro caso de uso.
  - É um relacionamento de obrigatoriedade.
  - Exemplos:
    - O caso de uso `Manter cliente` inclui o caso de uso `Manter cidade`. O caso de uso `Manter cidade` não pode ser utilizado sem o caso de uso `Manter cliente`. Consegue perceber?
      - Digamos que foi solicitado que o sistema permita que o usuário cadastre um cliente. Para cadastrar um cliente, o usuário precisa informar a cidade do cliente. Então, o caso de uso `Manter cliente` inclui o caso de uso `Manter cidade`.
    - O caso de uso - dos diagramas que utilizamos aqui - `Incluir vídeo na base compartilhada` **deve** ser utilizado quando o ator desejar `Ofertar conteúdo para afiliada`. Preste atenção no **DEVE**. O caso de uso `Incluir vídeo na base compartilhada` não pode ser utilizado sem o caso de uso `Ofertar conteúdo para afiliada`.
  - No diagrama, utilizamos uma linha tracejada com uma seta para representar este relacionamento com `<<include>>`.
  - A seta **aponta** para o caso de uso que deve ser incluído. O diagrama será evoluído para o seguinte:

    [![Relacionamento entre casos de uso e casos de uso com inclusão](http://tinyurl.com/24oldtxf)](http://tinyurl.com/24oldtxf)<!--![Relacionamento entre casos de uso e casos de uso com inclusão](../../../../assets/puml/uml_usecase08.puml)-->
    <br>
    <small>Relacionamento entre casos de uso e casos de uso com inclusão</small>
    <br>
    <small>Fonte: elaboração própria (2023)</small>

- **Relacionamento de extensão**: um caso de uso pode estender outro caso de uso.
  - É um relacionamento de ação opcional. A ação é executada se o ator desejar.
  - Segue um exemplo para tornar clara a ideia:

    <center>
        <figure>
            <img src="../../../../assets/images/lessons/design04.png" width=400 alt="Tela de login do sistema">
            <figcaption>
                Tela de login do sistema
            </figcaption>
            <small>Fonte: elaboração própria (2010)</small>
        </figure>
    </center>

    - Percebe que a funcionalidade "cadastre-se" é uma ação opcional? O usuário pode ou não clicar no link "cadastre-se". 
    - Uma funcionalidade com ação semelhante seria "esqueci minha senha".
    - O diagrama seria:
    
      [![Relacionamento entre casos de uso e casos de uso com extensão](http://tinyurl.com/24s2jmkb)](http://tinyurl.com/24s2jmkb)<!--![Relacionamento entre casos de uso e casos de uso com extensão](../../../../assets/puml/uml_usecase09.puml)-->
      <br>
      <small>Relacionamento entre casos de uso e casos de uso com extensão</small>
      <br>
      <small>Fonte: elaboração própria (2023)</small>

    - Aqui o ator `Usuário` realiza a ação `Fazer login`. Perceba que se ele quiser, ele poderá realizar a ação `Esqueci minha senha`. O caso de uso `Esqueci minha senha` estende o caso de uso `Fazer login`. O mesmo se dá com o caso de uso `Cadastre-se`. O caso de uso `Cadastre-se` também estende o caso de uso `Fazer login`.
    - Perceba ainda que existe um relacionamento entre `Cadastra-se` e o ator `Usuário`. O ator `Usuário` pode  utilizar diretamente o caso de uso `Cadastre-se`. Ou não pode? Imagina ele acessando diretamente essa funcionalidade em uma página principal do sistema, o que é bem comum. 
  - O caso de uso - dos diagramas que utilizamos aqui - `Consultar base local` é uma ação opcional a ser executada quando o ator desejar `Ofertar conteúdo para afiliada`. Preste atenção no **PODE**. O caso de uso `Consultar base local` pode ser utilizado quando o ator desejar `Ofertar conteúdo para afiliada`. O mesmo ocorre com `Publicar e incluir vídeo na base compartilhada`.
    - Veja que a seta fica no sentido contrário ao relacionamento de inclusão. Ela indica que o caso de uso `Ofertar conteúdo para afiliada` pode ser estendido pelos casos de uso `Consultar base local` e `Publicar e incluir vídeo na base compartilhada`. Assim, a execução da funcionalidade **partirá** destes.
    - O diagrama ficará assim:
  
      [![Relacionamento entre casos de uso e casos de uso com extensão](http://tinyurl.com/27yeyt2k)](http://tinyurl.com/27yeyt2k)<!--![Relacionamento entre casos de uso e casos de uso com extensão](../../../../assets/puml/uml_usecase10.puml)-->
      <br>
      <small>Relacionamento entre casos de uso e casos de uso com extensão</small>
      <br>
      <small>Fonte: elaboração própria (2023)</small>
    
- **Relacionamento de generalização/especialização**
  - É um relacionamento de generalização/especialização entre casos de uso tal como visto entre atores.
  - No exemplo abaixo, o caso de uso `Abrir conta comum` pode ser **especializado** em `Abrir conta poupança` e `Abrir conta corrente`. O caso de uso `Abrir conta comum` é um caso de uso genérico, enquanto `Abrir conta poupança` e `Abrir conta corrente` são casos de uso específicos.
  - O diagrama ficará assim:
  
    [![Relacionamento entre casos de uso e casos de uso com generalização/especialização](http://tinyurl.com/2as4godb)](http://tinyurl.com/2as4godb)<!--![Relacionamento entre casos de uso e casos de uso com generalização/especialização](../../../../assets/puml/uml_usecase11.puml)-->
    <br>
    <small>Relacionamento entre casos de uso e casos de uso com generalização/especialização</small>
    <br>
    <small>Fonte: elaboração própria (2023)</small>

#### Especificação de caso de uso

- A especificação de caso de uso é um documento que descreve o caso de uso.
- Para entender como descrever uma especificação de casos de uso, veja o exemplo em [Especificação de casos de uso](/lessons/softeng/design/views/#especificao) na lição de [Visões](/lessons/softeng/design/views/).

# Diagrama de classes

É um dos mais utilizados e importantes da UML. Ele permite visualizar as classes que irão compor o sistema.

[![Exemplo de classe com atributos privados e métodos públicos](http://tinyurl.com/2b8orcz6)](http://tinyurl.com/2b8orcz6)<!--![Exemplo de classe com atributos privados e métodos públicos](../../../../assets/puml/uml_class01.puml)-->
<br>
<small>Exemplo de classe com atributos privados e métodos públicos</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

## Associações

É um relacionamento entre classes. Podem ser:

- Unárias ou reflexivas
- Binárias

### Unária ou reflexiva

Temos abaixo um exemplo de classe com associação unária ou reflexiva:

[![Exemplo de classe com associação unária ou reflexiva](http://tinyurl.com/2a5ofu7f)](http://tinyurl.com/2a5ofu7f)<!--![Exemplo de classe com associação unária ou reflexiva](../../../../assets/puml/uml_class02.puml)-->
<br>
<small>Exemplo de classe com associação unária ou reflexiva</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

### Binária

Temos abaixo um exemplo de classe com associação binária:

[![Exemplo de classe com associação binária](http://tinyurl.com/2csuysta)](http://tinyurl.com/2csuysta)<!--![Exemplo de classe com associação binária](../../../../assets/puml/uml_class03.puml)-->
<br>
<small>Exemplo de classe com associação binária</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Aqui podemos visualizar como ficaria o diagrama de classes e o código relacionado:

[![Exemplo de diagrama de classes com associação binária](http://tinyurl.com/2bvyfkfd)](http://tinyurl.com/2bvyfkfd)<!--![Exemplo de diagrama de classes com associação binária](../../../../assets/puml/uml_class04.puml)-->
<br>
<small>Exemplo de diagrama de classes com associação binária</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

```java
class A {
    private B b;
}

class B {
  
}
```

Aplicação de associação binária com uso de atributo privado:

[![Aplicação de associação binária com uso de atributo privado](http://tinyurl.com/28r56edy)](http://tinyurl.com/28r56edy)<!--![Aplicação de associação binária com uso de atributo privado](../../../../assets/puml/uml_class05.puml)-->
<br>
<small>Aplicação de associação binária com uso de atributo privado</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

### Binária com multiplicidade

Temos abaixo um exemplo de classe com associação binária com multiplicidade:

[![Exemplo de classe com associação binária com multiplicidade](http://tinyurl.com/2bogo4rx)](http://tinyurl.com/2bogo4rx)<!--![Exemplo de classe com associação binária com multiplicidade](../../../../assets/puml/uml_class06.puml)-->
<br>
<small>Exemplo de classe com associação binária com multiplicidade</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Em `0..1` temos que uma pessoa pode não ter nenhum telefone (`0`) ou até um telefone (`1`).

Outros exemplos poderiam ser:
- Em `0..*` temos que uma pessoa pode não ter nenhum telefone (`0`) ou até vários telefone (`*`).
- Em `1..*` temos que uma pessoa pode ter pelo menos um telefone (`1`) ou até vários telefones (`*`).

No primeiro caso, o código ficaria assim:

```java
class Pessoa {
    private Fone[] fone;
}

class Fone {
  
}
```

[![Exemplo de classe com associação binária com multiplicidade](http://tinyurl.com/2b3uma6o)](http://tinyurl.com/2b3uma6o)<!--![Exemplo de classe com associação binária com multiplicidade](../../../../assets/puml/uml_class07.puml)-->
<br>
<small>Exemplo de classe com associação binária com multiplicidade</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Desta forma, o código ficará assim:

```java
class Pessoa {
    private Fone[] fone;
}

class Fone {
    private Pessoa[] dono;
}
```

### Generalização e especialização

A generalização/especialização de classes é um relacionamento entre classes tal como visto entre casos de uso e atores. Desta forma, podemos ter:

[![Exemplo de classe com associação binária com multiplicidade](http://tinyurl.com/26ejpy36)](http://tinyurl.com/26ejpy36)<!--![Exemplo de classe com associação binária com multiplicidade](../../../../assets/puml/uml_class08.puml)-->
<br>
<small>Exemplo de diagrama de classes com generalização/especialização</small>
<br>
<small>Fonte: elaboração própria (2023)</small>
