---
author_profile: true
title: Projeto 01 - Semáforo
permalink: /lessons/iot/project02/
sidebar:
    nav: "iot"
layout: single
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_arduino05.jpg
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos."
---

# Conceitos

{% 
  include figure 
  image_path="/assets/images/gpt/cat_arduino05.jpg" 
  alt="Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos" 
  caption="Fonte: gerado por IA com Bing por Maxwell Anderson (2023)<br>Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos." 
%}
{: .align-center} 

# Introdução

Vamos construir um semáforo? Vai que seu Ferrorama precise de um. 😂

Podemos utilizar um botão para controlar a sequência de acionamento! Vamos lá?

Para isso, iremos utilizar a seguinte lista de materiais:

|  ID   | Descrição                     | Quantidade |
| :---: | :---------------------------- | :--------: |
|   1   | Arduino Uno                   |     1      |
|  D1   | LED Vermelho                  |     1      |
|  D2   | LED Amarelo                   |     1      |
|  D3   | LED Verde                     |     1      |
| R*n*  | Resistor 270 Ohms 1/4W        |     3      |
|  B1   | Botão de pressão              |     1      |
|  B1   | Protoboard ou placa de ensaio |     1      |
|  J1   | Jumpers                       |     8      |

*n = 1, 2, 3*

# Implementação

Vamos começar montando o circuito e depois iremos programar o Arduino para acender os LEDs.

## Simulador Tinkercad

Vamos implementar o projeto em duas versões, de maneira iterativa e incremental.

### Versão 1

Para a implementação do projeto, iremos utilizar o simulador Tinkercad. Para isso, crie um novo projeto e adicione os componentes conforme a imagem abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project02_led01.png"
    alt="Projeto 02 - Semáforo"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center}

Esta é a primeira versão do projeto. Veja que é bem básica e semelhante ao (Projeto 01)[/lessons/iot/projeto01]

Lembre-se: 

|  Pino  | Descrição       | Observação |
| :----: | :-------------- | :--------: |
| cátodo | pino mais curto |  ➖ (GND)   |
| ânodo  | pino mais longo |   ➕ (5V)   |

Insira os blocos conforme ilustrado abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project02_led02.png"
    alt="Código do Projeto 02 - Semáforo"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center}

Veja que o código deve ter ficado como o abaixo:

```c++
    // C++ code
    //

void setup()
{
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
}

void loop()
{
  digitalWrite(4, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(4, LOW);
  digitalWrite(3, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(3, LOW);
  digitalWrite(2, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(2, LOW);
}
```

Agora, clique no botão `▶️ Iniciar simulação` e veja o resultado. Cada LED deve piscar a cada 1s de maneira sequencial.

Vamos agora adicionar o botão?

### Versão 2

{%
    include figure
    image_path="/assets/images/lessons/iot/project02_led03.png"
    alt="Projeto 02 - Semáforo"
    caption="Fonte: próprio autor (2023)"
%}
{: .align-center}

Adicione um botão. Veja que o botão possui 4 pinos. Os pinos laterais 1a e 2a são conectados ao GND e ao 5V, respectivamente. O pino 1b é conectado ao pino 5 do Arduino.

> Preste atenção na posição do botão na placa de ensaio.
{: .notice--warning}

Agora, vamos adicionar o código para controlar o botão. Veja que o código deve ficar como o abaixo:

```c++
// C++ code
int pinoVermelho = 4;
int pinoAmarelo = 3;
int pinoVerde = 2;
int pinoBotao = 5;

int estado = 0;

void setup()
{
    pinMode(pinoVermelho, OUTPUT);
    pinMode(pinoAmarelo, OUTPUT);
    pinMode(pinoVerde, OUTPUT);
    pinMode(pinoBotao, INPUT_PULLUP);
}

void loop()
{
    int botao = digitalRead(pinoBotao);

    if (botao == HIGH)
    {
        if (estado == 0)
        {
            digitalWrite(pinoVermelho, HIGH);
            digitalWrite(pinoAmarelo, LOW);
            digitalWrite(pinoVerde, LOW);
            estado = 1;
        }
        else if (estado == 1)
        {
            digitalWrite(pinoVermelho, LOW);
            digitalWrite(pinoAmarelo, HIGH);
            digitalWrite(pinoVerde, LOW);       
            estado = 2;
        }
        else if (estado == 2)
        {
            digitalWrite(pinoVermelho, LOW);
            digitalWrite(pinoAmarelo, LOW);
            digitalWrite(pinoVerde, HIGH);       
            estado = 0;
        }
        delay(1000);
    }
}
```

Vamos simplificar o código acima?

### Versão 3

Sem alterar o circuito, vamos simplificar o código. Veja que o código deve ficar como o abaixo:

```c++
int pinoVermelho = 4;
int pinoAmarelo = 3;
int pinoVerde = 2;
int pinoBotao = 5;

int estado = 0;

void setup()
{
    pinMode(pinoVermelho, OUTPUT);
    pinMode(pinoAmarelo, OUTPUT);
    pinMode(pinoVerde, OUTPUT);
    pinMode(pinoBotao, INPUT_PULLUP);
}

void loop()
{
    if (digitalRead(pinoBotao))
    {
        if (estado == 0)
        {
            acionarSemaforo(HIGH, LOW, LOW);
            estado = 1;
        }
        else if (estado == 1)
        {
            acionarSemaforo(LOW, HIGH, LOW);     
            estado = 2;
        }
        else if (estado == 2)
        {
            acionarSemaforo(LOW, LOW, HIGH);
            estado = 0;
        }
        delay(1000);
    }
}

void acionarSemaforo(int vermelho, int amarelo, int verde)
{
    digitalWrite(pinoVermelho, vermelho);
    digitalWrite(pinoAmarelo, amarelo);
    digitalWrite(pinoVerde, verde);   
}
```

Show! Funciona! Você faria diferente?

Este projeto está também disponível em [ThinkerCad: Projeto 02 - Semáforo](https://www.tinkercad.com/things/exnWppanIAK-bodacious-rottis-jofo/editel?sharecode=Xv2lPeTS_GRd-w3Kfv6nVVWKTa8BUHVcq3fuEPaKo6A)
