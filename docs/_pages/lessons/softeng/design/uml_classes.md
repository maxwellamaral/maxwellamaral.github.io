---
title: Diagrama de classes
permalink: /lessons/softeng/design/uml_classes/
sidebar:
    nav: "softeng-design"

layout: single
author_profile: true
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_design04.png
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) "
---

<center>
    <figure>
        <img src="../../../../assets/images/gpt/cat_design04.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um diagrama de classes UML. O gato deve estar usando roupas formais.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

# Introdução

> **Nota**
>
> Para compreender esta lição, é necessário ter conhecimento prévio sobre o paradigma de programação orientada a objetos. Se você não tem conhecimento sobre o assunto, recomendo que estude antes de prosseguir.

É um dos mais utilizados e importantes da UML. Ele permite visualizar as classes que irão compor o sistema.

Veja o caso de uso `Abrir conta comum` na [lição anterior](uml_usecase.md#especificação-descritiva-de-casos-de-uso). Nele, temos que o ator `Cliente` irá interagir com o sistema para realizar a abertura de uma conta comum. 

Um caso de uso irá gerar uma classe. Um ator também gera classe. Desta forma, teremos:

[![Exemplo de classe com atributos privados e métodos públicos](https://tinyurl.com/2b8orcz6)](https://tinyurl.com/2b8orcz6)<!--![Exemplo de classe com atributos privados e métodos públicos](../../../../assets/puml/uml_class01.puml)-->
<br>
<small>Exemplo de classe com atributos privados e métodos públicos</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

# Elementos

Um classe é desenhada como um retângulo com três divisões:

- Nome da classe
- Atributos
- Métodos

## Atributos e métodos

Os atributos são escritos com o nome do atributo seguido de `:` e o tipo do atributo. Se não existirem atributos, então o retângulo que contém os atributos contém espaço vazio.

Os métodos são escritos com o nome do método seguido de `()` e o tipo de retorno do método. Os métodos que:

- não retornam nada são escritos como `void`.
- não possuem parâmetros são escritos como `()`.
- possuem parâmetros são escritos como `(nome_atributo1: tipoA, nome_atributo2: tipoB, ..., nome_atributoN: tipoC)`.

Se não existirem métodos, então a divisão de métodos não é desenhada.

> **Nota**
>
> Se você assume o papel de analista de sistemas e você irá necessitar modelar um sistema, ao término do seu trabalho, esses diagramas serão enviados aos desenvolvedores em forma de projeto. Os desenvolvedores irão implementar o sistema com base nos diagramas que você criou.
>
> Lembre-se também que as classes foram desenvolvidas a partir dos casos de usos que o analista também criou anteriormente.
>
> Faz sentido para você essa lógica de trabalho?

Assim, para o desenvolvedor, como ele criaria o código Java para a classe acima?

```java
class Conta {
    private Date data_abertura;
    private Date data_encerramento;
    private String numero_conta;
    private double saldo;
    private String senha;
    private int situacao;
    
    public void abrirConta(String conta) {
        // Implementação do método aqui
    }
    
    public Bool consultarConta(String agencia, String conta) {
        // Implementação do método aqui
    }

    public float saldoConta(String agencia, String conta) {
        // Implementação do método aqui
    }

    public Bool validarSenha() {
        // Implementação do método aqui
    }
}
```

E como seria a implementação em Python?

```python
class Conta:
  def __init__(self):
    self.data_abertura: datetime = None 
    self.data_encerramento: datetime = None
    self.numero_conta: str = ''
    self.saldo: float = 0.0
    self.senha: str = ''
    self.situacao: int = 0
  
  def abrirConta(self, conta: str) -> None:
    # Implementação do método aqui
  
  def consultarConta(self, agencia: str, conta: str) -> bool:
    # Implementação do método aqui

  def saldoConta(self, agencia: str, conta: str) -> float:
    # Implementação do método aqui

  def validarSenha(self) -> bool:
    # Implementação do método aqui
```

> Note que as anotações de tipo são apenas sugestões e não forçam o Python a usar esses tipos. Se você atribuir um valor de um tipo diferente a um desses atributos, o Python não irá parar você. As anotações de tipo são principalmente para documentação e para ferramentas de análise de código.

## Visibilidade

Os atributos e métodos podem ser públicos, privados ou protegidos. Lembra das aulas de programação orientada a objetos?

- **Público**: pode ser acessado por qualquer classe.
- **Privado**: só pode ser acessado pela própria classe.
- **Protegido**: só pode ser acessado pela própria classe e pelas classes filhas.

A visibilidade é representada por um símbolo antes do nome do atributo ou método:

- `+` para público
- `-` para privado
- `#` para protegido

Assim, temos:

[![Exemplo de classe com associação binária com multiplicidade](https://tinyurl.com/yr2784b6)](https://tinyurl.com/yr2784b6)<!--![Exemplo de classe com associação binária com multiplicidade](../../../../assets/puml/uml_class08.puml)-->
<br>
<small>Exemplo de diagrama de classes com elementos privados, públicos e protegidos</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

## Associações

São relacionamentos entre classes. Podem ser:

- Unária ou reflexiva
- Binária
- Binária com multiplicidade
- Generalização e especialização

### Unária ou reflexiva

Temos abaixo um exemplo de classe com associação unária ou reflexiva:

[![Exemplo de classe com associação unária ou reflexiva](https://tinyurl.com/yq9tk88t)](https://tinyurl.com/yq9tk88t)<!--![Exemplo de classe com associação unária ou reflexiva](../../../../assets/puml/uml_class02.puml)-->
<br>
<small>Exemplo de classe com associação unária ou reflexiva</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Veja que a associação reflexiva é uma associação entre objetos da mesma classe. No exemplo acima, temos que um funcionário pode ter vários colegas de trabalho. Desta forma, podemos podemos visualizar como ficaria o diagrama de classes e o código relacionado:

> ℹ️ **Nota**
>
> Não se concentre em interpretar todo o código, mas se concentre como as relações entre as classes são implementadas. 
> 
> Quem vai ter que se preocupar em implementar as classes são os desenvolvedores. A não ser que você é o cara que faz tudo. 😂

```java
import java.util.List;
import java.util.ArrayList;

class Funcionario {
    private String nome;
    private String cargo;
    private List<Funcionario> colegasDeTrabalho;

    // Construtor
    public Funcionario(String nome, String cargo) {
        this.nome = nome;
        this.cargo = cargo;
        this.colegasDeTrabalho = new ArrayList<>();
    }

    // Métodos de acesso para os atributos privados
    public String getNome() {
        return nome;
    }

    public String getCargo() {
        return cargo;
    }

    // Método para adicionar um colega de trabalho
    public void adicionarColega(Funcionario colega) {
        colegasDeTrabalho.add(colega);
        colega.colegasDeTrabalho.add(this); // Estabelece a associação bidirecional
    }

    // Método para obter a lista de colegas de trabalho
    public List<Funcionario> getColegasDeTrabalho() {
        return colegasDeTrabalho;
    }
}
```

Em Python, o código ficaria assim:

```python
class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
        self.colegas_de_trabalho = []

    # Método para adicionar um colega de trabalho
    def adicionar_colega(self, colega):
        self.colegas_de_trabalho.append(colega)
        colega.colegas_de_trabalho.append(self)  # Estabelece a associação bidirecional
```

Exemplo de uso:

```python
funcionario1 = Funcionario("Alice", "Gerente")
funcionario2 = Funcionario("Bob", "Analista")
funcionario3 = Funcionario("Charlie", "Desenvolvedor")

funcionario1.adicionar_colega(funcionario2)
funcionario1.adicionar_colega(funcionario3)

# Obtendo os colegas de trabalho de funcionario1
for colega in funcionario1.colegas_de_trabalho:
    print(colega.nome, colega.cargo)
```

### Binária

Genericamente, aqui podemos visualizar como ficaria o diagrama de classes e o código relacionado:

[![Exemplo de diagrama de classes com associação binária](https://tinyurl.com/ynremjvp)](https://tinyurl.com/ynremjvp)<!--![Exemplo de diagrama de classes com associação binária](../../../../assets/puml/uml_class04.puml)-->
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

Temos abaixo um exemplo de classe com associação binária:

[![Exemplo de classe com associação binária](https://tinyurl.com/ysbkrm5g)](https://tinyurl.com/ysbkrm5g)<!--![Exemplo de classe com associação binária](../../../../assets/puml/uml_class03.puml)-->
<br>
<small>Exemplo de classe com associação binária</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Na associação binária, temos que um sócio pode **possuir** vários dependentes.

Segue exemplos de código em Java para as classes Socio e Dependente:

```java
import java.util.Date;
import java.util.List;
import java.util.ArrayList;

class Socio {
    private Date data;
    private String endereco;
    private String nome;
    private String telefone;
    private List<Dependente> dependentes;

    public Socio(Date data, String endereco, String nome, String telefone) {
        this.data = data;
        this.endereco = endereco;
        this.nome = nome;
        this.telefone = telefone;
        this.dependentes = new ArrayList<>();
    }

    public void adicionarDependente(Dependente dependente) {
        dependentes.add(dependente);
    }

    public List<Dependente> getDependentes() {
        return dependentes;
    }
}

class Dependente {
    private Date data;
    private String nome;

    public Dependente(Date data, String nome) {
        this.data = data;
        this.nome = nome;
    }
}
```
Em Python, o código ficaria assim:

```python
from datetime import date

class Socio:
    def __init__(self, data, endereco, nome, telefone):
        self.data = data
        self.endereco = endereco
        self.nome = nome
        self.telefone = telefone
        self.dependentes = []

    def adicionar_dependente(self, dependente):
        self.dependentes.append(dependente)

    def get_dependentes(self):
        return self.dependentes

class Dependente:
    def __init__(self, data, nome):
        self.data = data
        self.nome = nome
```

Exemplo de uso em Python

```python
socio1 = Socio(date(1990, 1, 15), "Rua A, 123", "João", "123-456-789")
dependente1 = Dependente(date(2010, 5, 20), "Maria")
dependente2 = Dependente(date(2012, 8, 10), "Pedro")

socio1.adicionar_dependente(dependente1)
socio1.adicionar_dependente(dependente2)

# Obtendo os dependentes do sócio
for dependente in socio1.get_dependentes():
    print("Dependente:", dependente.nome, "- Data de Nascimento:", dependente.data)
```

Segue um outro exemplo de aplicação de associação binária, porém com uso de atributo privado:

[![Aplicação de associação binária com uso de atributo privado](https://tinyurl.com/28r56edy)](https://tinyurl.com/28r56edy)<!--![Aplicação de associação binária com uso de atributo privado](../../../../assets/puml/uml_class05.puml)-->
<br>
<small>Aplicação de associação binária com uso de atributo privado</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Veja que o atributo `fone` é privado e recebe um único valor.

O código em Java:

```java
class Fone {
    private String codigo;
    private String numero;
    private boolean celular;

    public void setFone(String codigo, String numero, boolean celular) {
        this.codigo = codigo;
        this.numero = numero;
        this.celular = celular;
    }

    public String getFone() {
        return codigo + numero;
    }

    public boolean isCelular() {
        return celular;
    }
}

class Pessoa {
    private String nome;
    private String sobrenome;
    private Fone fone;

    public void setPessoa(String nome, String sobrenome, Fone fone) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.fone = fone;
    }

    public Pessoa getPessoa() {
        return this;
    }
}
```

Em Python, o código ficaria assim:

```python
class Fone:
    def __init__(self):
        self.codigo = ""
        self.numero = ""
        self.celular = False

    def setFone(self, codigo, numero, celular):
        self.codigo = codigo
        self.numero = numero
        self.celular = celular

    def getFone(self):
        return self.codigo + self.numero

    def isCelular(self):
        return self.celular

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.fone = Fone()

    def setPessoa(self, nome, sobrenome, fone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.fone = fone

    def getPessoa(self):
        return self
```

Exemplo de uso em Python

```python
fone = Fone()
fone.setFone("55", "123456789", True)

pessoa = Pessoa()
pessoa.setPessoa("Alice", "Silva", fone)

# Obtendo informações da pessoa e seu telefone
print("Nome:", pessoa.nome, pessoa.sobrenome)
print("Telefone:", pessoa.fone.getFone())
print("É celular?", pessoa.fone.isCelular())
```

### Binária com multiplicidade

Temos abaixo um exemplo de classe com associação binária com multiplicidade:

[![Exemplo de classe com associação binária com multiplicidade](https://tinyurl.com/2bogo4rx)](https://tinyurl.com/2bogo4rx)<!--![Exemplo de classe com associação binária com multiplicidade](../../../../assets/puml/uml_class06.puml)-->
<br>
<small>Exemplo de classe com associação binária com multiplicidade</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Em `0..1` temos que uma pessoa pode não ter nenhum telefone (`0`) ou até um telefone (`1`). Neste caso, o desenvolvedor terá que implementar a restrição sobre a quantidade de objetos que podem ser criados (nenhum telefone ou um único telefone).

Outros exemplos poderiam ser:

- Em `0..*` temos que uma pessoa pode não ter nenhum telefone (`0`) ou até vários telefones (`*`).
- Em `1..*` temos que uma pessoa pode ter pelo menos um telefone (`1`) ou até vários telefones (`*`).

Um quadro geral para representar a multiplicidade é:

| Nome             | Simbologia | Descrição                 |
| ---------------- | ---------- | ------------------------- |
| Um               | `1`        | Um único objeto           |
| Vários           | `*`        | Vários objetos            |
| Um ou vários     | `1..*`     | Um ou vários objetos      |
| Nenhum ou um     | `0..1`     | Nenhum ou um único objeto |
| Nenhum ou vários | `0..*`     | Nenhum ou vários objetos  |


No primeiro caso, o código ficaria assim:

```java
class Pessoa {
    private Fone[] fone;
}

class Fone {
  
}
```

O segundo caso, onde um telefone poderá ser vinculado a várias pessoas, ficaria assim:

[![Exemplo de classe com associação binária com multiplicidade](https://tinyurl.com/2b3uma6o)](https://tinyurl.com/2b3uma6o)<!--![Exemplo de classe com associação binária com multiplicidade](../../../../assets/puml/uml_class07.puml)-->
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

"Oxente! Mas se uma pessoa pode ter nenhum ou um único telefone e um telefone pode ser vinculado a várias pessoas, por que o código aparenta ser uma relação muitos para muitos?"

Porque o desenvolvedor terá que implementar "na mão" a restrição sobre a quantidade de objetos que podem ser criados (nenhum telefone ou um único telefone). Ele vai dar um jeito de implementar isso. 😁

> ℹ️ **Nota**
>
> Um telefone vinculado a várias pessoas? Consegue imaginar um exemplo de aplicação? ;)

### Generalização e especialização

A generalização/especialização de classes é um relacionamento entre classes tal como visto entre casos de uso e atores. Desta forma, podemos ter:

[![Exemplo de classe com associação binária com multiplicidade](https://tinyurl.com/yr2784b6)](https://tinyurl.com/yr2784b6)<!--![Exemplo de classe com associação binária com multiplicidade](../../../../assets/puml/uml_class08.puml)-->
<br>
<small>Exemplo de diagrama de classes com generalização/especialização</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

O código em Java ficara assim:

```java
import java.util.Date;

class ContaComum {
    private Date dataAbertura;
    private Date dataEncerramento;
    private String numeroConta;
    private float saldo;
    private String senha;
    private int situacao;

    public void abrirConta(String conta) {
        // Lógica para abrir uma conta
    }

    public boolean consultarConta(String agencia, String conta) {
        // Lógica para consultar uma conta
        return true;
    }

    public float saldoConta(String agencia, String conta) {
        // Lógica para verificar o saldo de uma conta
        return saldo;
    }

    public boolean validarSenha() {
        // Lógica para validar a senha
        return true;
    }
}

class ContaEspecial extends ContaComum {
    private double limite;
}

class ContaPoupanca extends ContaComum {
    private Date dataAniversario;
}
```

Em Python, o código ficaria assim:

```python
from datetime import date

class ContaComum:
    def __init__(self):
        self.data_abertura = date.today()
        self.data_encerramento = None
        self.numero_conta = ""
        self.saldo = 0.0
        self.senha = ""
        self.situacao = 0

    def abrir_conta(self, conta):
        # Lógica para abrir uma conta
        pass

    def consultar_conta(self, agencia, conta):
        # Lógica para consultar uma conta
        return True

    def saldo_conta(self, agencia, conta):
        # Lógica para verificar o saldo de uma conta
        return self.saldo

    def validar_senha(self):
        # Lógica para validar a senha
        return True

class ContaEspecial(ContaComum):
    def __init__(self):
        super().__init__()
        self.limite = 0.0

class ContaPoupanca(ContaComum):
    def __init__(self):
        super().__init__()
        self.data_aniversario = date.today()
```

Exemplo de uso em Python

```python
conta_especial = ContaEspecial()
conta_especial.abrir_conta("123456")

conta_poupanca = ContaPoupanca()
conta_poupanca.abrir_conta("789012")

print("Conta Especial:")
print("Saldo:", conta_especial.saldo_conta("agencia", conta_especial.numero_conta))

print("Conta Poupança:")
print("Saldo:", conta_poupanca.saldo_conta("agencia", conta_poupanca.numero_conta))
```

### Agregação

A agregação é um tipo de associação onde um objeto é composto por outros objetos. Guardam uma relação *todo-parte* entre si.

Como assim? Pense na seguinte situação: se um jogador **faz parte** de uma equipe, isso pode ser considerado uma relação de associação? Sim, sim! E não só uma associação simples, mas uma agregação. O jogador é um "agregado" da equipe. Ou seja, a equipe é composta por jogadores.

Com isso, existe uma regra para verificar a relação de agregação entre duas classes. Se uma das perguntas abaixo for verdadeira, então temos uma agregação:

- B é parte de A?
- A tem um ou mais B?

[![Exemplo de classe com agregação](https://tinyurl.com/ynqw6pyg)](https://tinyurl.com/ynqw6pyg)<!--![Exemplo de classe com agregação](../../../../assets/puml/uml_class09.puml)-->
<br>
<small>Exemplo de classe com agregação</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

A agregação é representada por uma linha com um losango vazado na ponta que aponta para a classe que representa o todo.

Neste exemplo, `Jogador` é **parte** e `Equipe` é **todo**. 

Cada equipe possui um ou mais jogadores. E cada jogador faz parte de uma equipe. Se a equipe deixar de existir, os jogadores poderão fazer parte de outras equipes. Se um jogador deixar de existir, a equipe continuará existindo. Nessa relação, um jogador também poderá fazer parte de mais de uma equipe. A ideia é que se a equipe deixar de existir, ninguém vai ser demitido! 😁

### Composição 

A composição é um tipo de agregação mais **forte**. 

Aqui a história muda! Se a equipe deixar de existir, os jogadores serão demitidos! 😱

Assim, os objetos-parte (jogadores) não podem existir sem o objeto-todo (equipe). Os objetos-parte são sempre criados e destruídos pelo objeto-todo. Se o **todo** deixa de existir, as **partes** também deixarão de existir. 

[![Exemplo de classe com composição](https://tinyurl.com/ylgmyal6)](https://tinyurl.com/ylgmyal6)<!--![Exemplo de classe com composição](../../../../assets/puml/uml_class10.puml)-->
<br>
<small>Exemplo de classe com composição</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

A composição é representada por uma linha com um losango preenchido na ponta que aponta para a classe que representa o todo.

### Exemplo completo

Veja um exemplo completo de diagrama de classes com todas as associações apresentadas até aqui.

[![Exemplo de diagrama completo](https://tinyurl.com/ypa2zgce)](https://tinyurl.com/ypa2zgce)<!--![Exemplo de diagrama completo](../../../../assets/puml/uml_class11.puml)-->
<br>
<small>Exemplo de diagrama completo</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Quando eu devo usar uma simples associação, uma relação de agregação ou de composição? Tudo depende da análise subjetiva do analista de sistemas. Se vai usar multiplicidade ou não, se vai usar associação unária ou binária, etc.

## Classes e métodos abstratos

Uma classe abstrata é uma classe que não pode ser instanciada. Ela é usada apenas para ser herdada por outras classes. Classes abstratas só existem para serem herdadas.

A classe abstrata é representada por um nome em itálico.

[![Exemplo de classe abstrata](https://tinyurl.com/yuln4xd6)](https://tinyurl.com/yuln4xd6)<!--![Exemplo de classe abstrata](../../../../assets/puml/uml_class12.puml)-->
<br>
<small>Exemplo de classe abstrata</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Um método abstrato é um método que não possui implementação. Ele é usado apenas para ser sobrescrito por outras classes. Métodos abstratos só existem para serem sobrescritos.

O método abstrato é representado por um nome em itálico, assim como a classe.

## Interfaces

Uma interface é um conjunto de métodos abstratos. Ela é usada para definir um contrato que deve ser implementado por outras classes.

A interface é representada por um nome em itálico e com o nome precedido por um `<<interface>>` ou símbolo correspondente.

[![Exemplo de interface](https://tinyurl.com/yrs3c84f)](https://tinyurl.com/yrs3c84f)<!--![Exemplo de interface](../../../../assets/puml/uml_class13.puml)-->
<br>
<small>Exemplo de interface</small>
<br>
<small>Fonte: elaboração própria (2023)</small>


# Referências

---. Aula 03 UML Parte01. Universidade Salvador.

Guedes, G. T. A. UML 2 Uma abordagem prática. 1ª edição. São Paulo: Novatec Editora, 2009.

Marco Tulio Valente. Engenharia de Software Moderna: Princípios e Práticas para Desenvolvimento de Software com Produtividade, Editora: Independente, 395 páginas, 2020.

Pressman, S. R. Engenharia de Software. 6ª edição. São Paulo: McGraw-Hill, 2006.

Tonsig, S. L. Engenharia de Software. Análise e Projeto de Sistemas. 1ª edição. São Paulo: Futura, 2003.

---
Criado em Junho de 2023 por *Maxwell Anderson*