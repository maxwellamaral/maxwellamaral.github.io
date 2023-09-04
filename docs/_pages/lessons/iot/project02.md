---
author_profile: true
title: Projeto 01 - LED
permalink: /lessons/iot/project01/
sidebar:
    nav: "iot"
layout: single
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_arduino06.jpg
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos."
---

# Conceitos

{% 
  include figure 
  image_path="/assets/images/gpt/cat_arduino06.jpg" 
  alt="Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos" 
  caption="Fonte: gerado por IA com Bing por Maxwell Anderson (2023)<br>Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos." 
%}
{: .align-center} 

# Introdução

Nosso primeiro projeto irá tem como objetivo acender um LED e fazê-lo piscar a cada 1s. Para isso, iremos utilizar o Arduino Uno, um LED e um resistor de 270 Ohms e 1/4W.

{%
    include figure
    image_path="/assets/images/lessons/iot/project01_led01.png"
    alt="Placa de ensaio com LED e resistor"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center} 

Para isso, iremos utilizar a seguinte lista de materiais:

|  ID   | Descrição                     | Quantidade |
| :---: | :---------------------------- | :--------: |
|   1   | Arduino Uno                   |     1      |
|  D1   | LED Vermelho                  |     1      |
|  R1   | Resistor 270 Ohms 1/4W        |     1      |
|  B1   | Protoboard ou placa de ensaio |     1      |

# Implementação

Vamos começar montando o circuito e depois iremos programar o Arduino para acender o LED.

## Simulador Tinkercad

Para a implementação do projeto, iremos utilizar o simulador Tinkercad. Para isso, crie um novo projeto e adicione os componentes conforme a imagem abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project01_led02.png"
    alt="Projeto 01 - LED"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center}

Um LED possui um cátodo e um ânodo. O cátodo é o pino mais curto e o ânodo é o pino mais longo. O cátodo deve ser conectado ao GND e o ânodo ao pino digital 12 do Arduino. 

O resistor deve ser conectado ao cátodo do LED e o ânodo ao pino digital 12 do Arduino. 

Lembre-se: 

|  Pino  | Descrição       | Observação |
| :----: | :-------------- | :--------: |
| cátodo | pino mais curto |  ➖ (GND)   |
| ânodo  | pino mais longo |   ➕ (5V)   |

O resistor serve para evitar que o LED queime, já que possuem resistências baixas. Já que o Arduíno possui uma corrente muito elevada, o resistor é necessário para limitar a corrente que passa para o LED. Ele precisa de 10mA para brilhar de forma razoável, e já que o Arduíno oferece uma corrente de 40mA, o resistor é necessário para limitar a corrente para 10mA.

De forma prática, como poderemos realizar o cálculo do resistor?

1. Primeiro, precisamos saber a tensão de alimentação do LED. Para isso, consulte o datasheet do LED. Para o LED que estamos utilizando, a tensão de alimentação é de 2V.
2. Agora, precisamos saber a tensão de alimentação do Arduíno. Para isso, consulte o datasheet do Arduíno. Para o Arduíno Uno, a tensão de alimentação é de 5V.
3. A queda de tensão no resistor é de 3V (5V - 2V).
4. A corrente que passa pelo resistor é de 10mA.
5. Utilizando a Lei de Ohm, podemos calcular o valor do resistor: R = V / I = 3V / 0,01A = 300 Ohms. Como não temos um resistor de 300 Ohms, iremos utilizar um resistor de 270 Ohms.
6. Isso significa que o resistor irá limitar a corrente em 11,111mA (3V / 270 Ohms). Como não é uma corrente alta para o LED, podendo funcionar entre 5mA e 30mA, o LED irá funcionar normalmente.

Agora, vamos programar o Arduíno para acender o LED. Para isso, clique no botão `Código`. Você poderá escolher entre as opções `Bloco`, `Texto` ou `Bloco + texto`. Para este projeto, iremos utilizar a opção `Bloco + texto`.

Insira os blocos conforme ilustrado abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project01_led03.png"
    alt="Código do Projeto 01 - LED"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center}

Veja que o código deve ter ficado como o abaixo:

```c++
    // C++ code
    //

    void setup()
    {
        pinMode(12, OUTPUT);
    }

    void loop()
    {
        digitalWrite(12, HIGH);
        delay(1000);    // Wait for 1000 millisecond(s)
        digitalWrite(12, LOW);
        delay(1000);    // Wait for 1000 millisecond(s)
    }
```

Agora, clique no botão `▶️ Iniciar simulação` e veja o resultado. O LED deve piscar a cada 1s.

{%
    include figure
    image_path="/assets/images/lessons/iot/project01_led01.gif"
    alt="Projeto 01 - LED"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center}

Parabéns, agora você já sabe como acender um LED utilizando o Arduino Uno.

Este projeto está também disponível em [ThinkerCad: Projeto 01 - LED ](https://www.tinkercad.com/things/g4HwEwSwOGp-brave-blorr/editel?sharecode=PBwumkFznbt7maPbyqybi-40uBAvfjPorB-2DX_9URw)
