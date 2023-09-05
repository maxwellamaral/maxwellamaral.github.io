---
author_profile: true
title: Projeto 04 - Giroflex com ajuste
permalink: /lessons/iot/project04/
sidebar:
    nav: "iot"
layout: single
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_arduino02.jpg
    caption: "Gato estudando IOT | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos."
---

# Conceitos

{% 
  include figure 
  image_path="/assets/images/gpt/cat_arduino02.jpg" 
  alt="Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos" 
  caption="Fonte: gerado por IA com Bing por Maxwell Anderson (2023)<br>Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos." 
%}
{: .align-center} 

# Introdução

Vamos construir um novo giroflex de ambulância, só que agora com ajustes.

Agora iremos aprender como usar potenciômetro.

Para isso, iremos utilizar a seguinte lista de materiais:

|  ID   | Descrição              | Quantidade |
| :---: | :--------------------- | :--------: |
|   1   | Arduino Uno            |     1      |
|  D1   | LED Vermelho           |     1      |
|  R1   | Resistor 270 Ohms 1/4W |     1      |
|  R2   | Potenciômetro 250kOhms |     1      |

# Implementação

Este exemplo mostra como usar uma saída digital e uma entrada analógica para controlar o tempo de pulsação de brilho de um LED. Vamos usar o pino 13 para controlar o LED.

Uma entrada analógica lê um sensor analógico (potenciômetro) em um pino analógico 0. Este valor pode ser usado para controlar a intermitência do brilho de um LED, por exemplo.

Vamos começar montando o circuito e depois iremos programar o Arduino.

## Simulador Tinkercad

Para a implementação do projeto, iremos utilizar o simulador Tinkercad. Para isso, crie um novo projeto e adicione os componentes conforme a imagem abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project04_led01.png"
    alt="Projeto 04 - Giroflex com ajuste"
    caption="Fonte: TinkerCad (2023), adaptado pelo autor"
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
    image_path="/assets/images/lessons/iot/project04_led02.png"
    alt="Código do Projeto 04 - Giroflex com ajustes"
    caption="Fonte: TinkerCad (2023), adaptado pelo autor"
%}
{: .align-center}

Veja que o código deve ter ficado como o abaixo:

```c++
int valorSensor = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  valorSensor = analogRead(A0);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(valorSensor); 
  digitalWrite(LED_BUILTIN, LOW);
  delay(valorSensor); 
}
```

- `LED_BUILTIN` é uma constante que contém o número do pino do LED embutido no Arduino. No Arduino Uno, é o pino 13.
- `analogRead(A0)` lê o valor do pino analógico A0 e armazena-o na variável `valorSensor`.
- `valorSensor` é o valor que conterá o tempo de delay do LED.


Agora, clique no botão `▶️ Iniciar simulação` e veja o resultado. Cada LED deve piscar a cada 1s de maneira sequencial.

Funciona! Por que você não tenta fazer outra coisa? 😉

Este projeto está também disponível em [TinkerCad: Projeto 04 - Giroflex com ajuste](https://www.tinkercad.com/things/6iqYZk1Cgls-glorious-wluff-esboo/editel?sharecode=7YWI_ATZT2XYTHHUjRDrcYTqNRo8zWkfQ_i2UBKlqyY)
