---
author_profile: true
title: Projeto 03 - Giroflex
permalink: /lessons/iot/project03/
sidebar:
    nav: "iot"
layout: single
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_arduino03.jpg
    caption: "Gato estudando IOT | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos."
---

# Conceitos

{% 
  include figure 
  image_path="/assets/images/gpt/cat_arduino03.jpg" 
  alt="Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos" 
  caption="Fonte: gerado por IA com Bing por Maxwell Anderson (2023)<br>Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos." 
%}
{: .align-center} 

# Introdução

Vamos construir um giroflex de ambulância.

Agora iremos aprender como usar uma saída analógica.

Para isso, iremos utilizar a seguinte lista de materiais:

|  ID   | Descrição              | Quantidade |
| :---: | :--------------------- | :--------: |
|   1   | Arduino Uno            |     1      |
|  D1   | LED Vermelho           |     1      |
|  R1   | Resistor 270 Ohms 1/4W |     1      |

# Implementação

Este exemplo mostra como usar uma saída analógica para controlar o brilho de um LED. Vamos usar o pino 9 para controlar o LED utilizando a função `analogWrite()`.

Ele utiliza PWM (Pulse Width Modulation) para controlar a intensidade do brilho do LED. Caso queira utilizar outro pino, sempre utilize os pinos que contêm o til (~).

Vamos começar montando o circuito e depois iremos programar o Arduino.

## Simulador Tinkercad

Para a implementação do projeto, iremos utilizar o simulador Tinkercad. Para isso, crie um novo projeto e adicione os componentes conforme a imagem abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project03_led01.png"
    alt="Projeto 03 - Giroflex"
    caption="Fonte: TinkerCad (2023)"
%}
{: .align-center}

Lembre-se: 

|  Pino  | Descrição       | Observação |
| :----: | :-------------- | :--------: |
| cátodo | pino mais curto |  ➖ (GND)   |
| ânodo  | pino mais longo |   ➕ (5V)   |

Insira os blocos conforme ilustrado abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project03_led02.png"
    alt="Código do Projeto 03 - Giroflex"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center}

Veja que o código deve ter ficado como o abaixo:

```c++
int brilho = 0;

void setup()
{
  pinMode(9, OUTPUT);
}

void loop()
{
  for (brilho = 0; brilho <= 255; brilho += 5) {
    analogWrite(9, brilho);
    delay(30); // Wait for 30 millisecond(s)
  }
  for (brilho = 255; brilho >= 0; brilho -= 5) {
    analogWrite(9, brilho);
    delay(30); // Wait for 30 millisecond(s)
  }
}
```

Agora, clique no botão `▶️ Iniciar simulação` e veja o resultado. Cada LED deve piscar a cada 1s de maneira sequencial.

Funciona! Por que você não tenta fazer outra coisa? 😉

Este projeto está também disponível em [TinkerCad: Projeto 03 - Giroflex](https://www.tinkercad.com/things/gVLSE5gQ1JC-magnificent-kieran/editel?sharecode=zXEw_kqFUTMId7A-V1eELK-ca-E1-ffdm2G7LO4cuvg)
