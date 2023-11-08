---
title: Diagrama de pacotes
permalink: /lessons/softeng/design/uml_packages/
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
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023)"
---

<center>
    <figure>
        <img src="../../../../assets/images/gpt/cat_design05.png" width=500 alt="Gato engenheiro de software que está criando um projeto de software em UML">
        <figcaption>
            Gato engenheiro de software que está criando um projeto de software em UML.<br>
            <em>Prompt: crie uma imagem de um gato engenheiro de software usando óculos criando um diagrama de pacotes UML.</em>
        </figcaption>
        <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
    </figure>
</center>

# Introdução

O diagrama de pacotes descreve **como** os elementos de um sistema estão organizados ou agrupados.

Eles podem ser usados para organizar elementos de um sistema em diferentes níveis de abstração e permitem representar:

- um sistema
- um subsistema
- uma biblioteca (lembra das bibliotecas do C++ e do Java?)
- uma etapa
- dentre outros

![Exemplo de diagrama de pacotes](../../../../assets/images/lessons/design06.png)
<br>
<small>Exemplo de diagrama de pacotes</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

No exemplo abaixo não definimos atributos, métodos ou associações.

[![Exemplo de diagrama de pacotes com elementos](https://tinyurl.com/ykwnkogq)](https://tinyurl.com/ykwnkogq)<!--![Exemplo de diagrama de pacotes com elementos](../../../../assets/puml/uml_package01.puml)-->
<br>
<small>Exemplo de diagrama de pacotes com elementos</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

E podemos ter pacotes dentro de outros pacotes.

[![Exemplo de diagrama de pacotes com pacotes dentro de pacotes](https://tinyurl.com/ywomlmlj)](https://tinyurl.com/ywomlmlj)<!--![Exemplo de diagrama de pacotes com pacotes dentro de pacotes](../../../../assets/puml/uml_package02.puml)-->
<br>
<small>Exemplo de diagrama de pacotes com pacotes dentro de pacotes</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Também existem relacionamentos entre pacotes:

[![Exemplo de diagrama de pacotes com relacionamentos](https://tinyurl.com/ykdexf3w)](https://tinyurl.com/ykdexf3w)<!--![Exemplo de diagrama de pacotes com relacionamentos](../../../../assets/puml/uml_package03.puml)-->
<br>
<small>Exemplo de diagrama de pacotes com relacionamentos</small>
<br>
<small>Fonte: elaboração própria (2023)</small>

Os pacotes em Java são representados da seguinte forma:

```java
package br.com.maxwellanderson;
```

E em C++:

```cpp
namespace br {
    namespace com {
        namespace maxwellanderson {
        }
    }
}
```

Em Python não temos pacotes, mas podemos criar módulos:

```python
import br.com.maxwellanderson
```

Assim sendo, o diagrama ficaria assim:

[![Exemplo de diagrama de pacotes com relacionamentos](https://tinyurl.com/yq842svu)](https://tinyurl.com/yq842svu)<!--![Exemplo de diagrama de pacotes com relacionamentos](../../../../assets/puml/uml_package04.puml)-->
<br>
<small>Exemplo de diagrama de pacotes com relacionamentos</small>
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
