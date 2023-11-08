---
title: Diagrama de atividades
permalink: /lessons/softeng/design/uml_activities/
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
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023)"
---

<center>
    <figure>
        <img src="../../../../assets/images/gpt/cat_design06.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um diagrama de atividades UML.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

# Introdução

São utilizados para representar um fluxo de atividades, ou seja, um fluxo de trabalho. Simplesmente pode-se dizer que é uma sequência de atividades ou um passo a passo.

Visualmente são representados por um retângulo com bordas arredondadas e com o nome da atividade dentro. O nome da atividade é composto por um verbo no infinitivo e um ou mais substantivos.

[![Exemplo de diagrama de atividades](https://tinyurl.com/yn87rqu8)](https://tinyurl.com/yn87rqu8)<!--![Exemplo de diagrama de atividades](../../../../assets/puml/uml_activity01.puml)-->
<br>
<small>Exemplo de diagrama de atividades</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

# Elementos

Como podemos ver, o diagrama de atividades é composto por:

- **Start**: é representado por um círculo com um ponto dentro. O start é utilizado para representar o início do fluxo de atividades.
- **Atividades**: são representadas por um retângulo com bordas arredondadas e com o nome da atividade dentro. O nome da atividade é composto por um verbo no infinitivo e um ou mais substantivos.
- **Fluxo de controle**: é representado por uma seta que sai de uma atividade e vai para outra atividade. O fluxo de controle indica a ordem em que as atividades devem ser executadas.
- **Decisão**: é representada por um losango. A decisão é utilizada para representar uma condição que deve ser avaliada para decidir qual atividade deve ser executada em seguida.
- **Final**: é representado por um círculo com um círculo dentro. O final é utilizado para representar o fim do fluxo de atividades.

Quando um analista de sistemas envia um diagrama de atividades para o desenvolvedor, ele deve implementar o fluxo de atividades utilizando uma linguagem de programação. 

Assim sendo, como você implementaria o fluxo de atividades do exemplo acima utilizando a linguagem de programação Java?

```java
import java.util.HashMap;
import java.util.Map;

class Conta {
    private String numeroConta;
    private String senha;
    private double saldo;

    // Construtor
    public Conta(String numeroConta, String senha) {
        this.numeroConta = numeroConta;
        this.senha = senha;
        this.saldo = 1000.0; // Saldo inicial para ilustração
    }

    // Método para consultar saldo
    public double consultarSaldo(String senhaDigitada) {
        if (senhaDigitada.equals(senha)) {
            return saldo;
        } else {
            System.out.println("Senha inválida. Operação cancelada.");
            return -1; // Retorna -1 para indicar senha inválida
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Simulação de consulta de saldo
        String numeroConta = "12345";
        String senhaCorreta = "senha123";
        String senhaIncorreta = "senha456";

        Conta conta = new Conta(numeroConta, senhaCorreta);

        // Consulta de saldo com senha correta
        double saldo = conta.consultarSaldo(senhaCorreta);
        if (saldo >= 0) {
            System.out.println("Saldo disponível: R$" + saldo);
        }

        // Consulta de saldo com senha incorreta (simulando o fluxo do diagrama de atividades)
        saldo = conta.consultarSaldo(senhaIncorreta);
        if (saldo == -1) {
            System.out.println("Operação não autorizada devido à senha incorreta.");
        }
    }
}

```

Em Python:

```python
class Conta:
    def __init__(self, numero_conta, senha):
        self.numero_conta = numero_conta
        self.senha = senha
        self.saldo = 1000.0  # Saldo inicial para ilustração

    # Método para consultar saldo
    def consultar_saldo(self, senha_digitada):
        if senha_digitada == self.senha:
            return self.saldo
        else:
            print("Senha inválida. Operação cancelada.")
            return -1  # Retorna -1 para indicar senha inválida

# Simulação de consulta de saldo
numero_conta = "12345"
senha_correta = "senha123"
senha_incorreta = "senha456"

conta = Conta(numero_conta, senha_correta)

# Consulta de saldo com senha correta
saldo = conta.consultar_saldo(senha_correta)
if saldo >= 0:
    print("Saldo disponível: R$", saldo)

# Consulta de saldo com senha incorreta (simulando o fluxo do diagrama de atividades)
saldo = conta.consultar_saldo(senha_incorreta)
if saldo == -1:
    print("Operação não autorizada devido à senha incorreta.")
```

Acompanhe o fluxo de atividades no diagrama abaixo:

[![Exemplo de diagrama de atividades](https://tinyurl.com/yvuky474)](https://tinyurl.com/yvuky474)<!--![Exemplo de diagrama de atividades](../../../../assets/puml/uml_activity02.puml)-->
<br>
<small>Exemplo de diagrama de atividades</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Agora temos mais elementos no diagrama de atividades:

- **Fork**: é representado por uma barra horizontal. O fork é utilizado para representar a separação de um fluxo de controle em dois ou mais fluxos de controle. O fork é utilizado quando uma atividade deve ser executada em paralelo com outra atividade. No exemplo acima, a atividade "Enviar email de compra" é executada em paralelo com a atividade "Enviar SMS com dados da compra". 
- **Join**: é representado por uma barra horizontal. O join é utilizado para representar a junção de dois ou mais fluxos de controle em um único fluxo de controle. O join é o contrário do fork. No exemplo acima, a atividade "Enviar email de compra" é executada em paralelo com a atividade "Enviar SMS com dados da compra". Após a execução dessas duas atividades, o fluxo de controle é unificado novamente na atividade "Gerar nota fiscal".

Os forks possuem um único ponto de entrada e vários fluxos de saída. Assim sendo, existem múltiplos processos sendo executados de forma paralela. Esse mecanismo é implementado pelo desenvolvedor em forma de *threads*. Quando as *threads* terminam de executar, o fluxo de controle é unificado novamente no join.

Os diagramas de atividades podem possuir raias. As raias são utilizadas para representar os responsáveis por cada atividade. No exemplo abaixo, temos um diagrama de atividades com raias:

[![Exemplo de diagrama de atividades com raias](https://tinyurl.com/ykcuglbj)](https://tinyurl.com/ykcuglbj)<!--![Exemplo de diagrama de atividades com raias](../../../../assets/puml/uml_activity03.puml)-->
<br>
<small>Exemplo de diagrama de atividades com raias</small>
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
