---
author_profile: true
title: Introdução
permalink: /lessons/iot/intro/
sidebar:
    nav: "iot"
layout: single
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_arduino01.jpg
    caption: "Gato estudando Engenharia de Software | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino."
---

{%
    include figure
    image_path="/assets/images/gpt/cat_arduino01.jpg"
    alt="Imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino."
    caption="Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023)<br>Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino."
%}
{: .align-center}


# Introdução

## O que é Internet das Coisas?

Aproximadamente 5,16 bilhões de pessoas (64,4%) usam a Internet em todo o mundo (WE ARE SOCIAL[^1], 2023), mas esse número é pequeno em comparação com o número de dispositivos conectados à Internet. Estima-se que existam mais de 27 bilhões de dispositivos conectados à Internet em todo o mundo, e esse número deve chegar a 75,44 bilhões até 2025 (FORBES apud ABINC[^2], 2022).

A Internet das Coisas (do inglês, Internet of Things, IoT) é um conceito que se refere à interconexão digital de objetos cotidianos com a internet. A IoT permite que objetos físicos sejam acessados remotamente através de uma rede de sensores e atuadores, permitindo que os mesmos sejam monitorados e controlados remotamente.

Enquanto pessoas acessam a Internet em busca de informação e entretenimento, as "coisas" ou dispositivos acessam a Internet para transmitir informações sobre o ambiente em que estão inseridas. Essas informações podem ser utilizadas para monitorar e controlar o ambiente, permitindo que as coisas sejam mais eficientes e autônomas.

Lembram da arquitetura básica de Von Neumann? 

Um processador centraliza o processamento de dados que entram. A saída é o resultado desse processamento.

[![Arquitetura de Von Neumann](http://tinyurl.com/2bt5kyss)](http://tinyurl.com/2bt5kyss)<!--![Arquitetura de Von Neumann](../../../assets/puml/iot_von_neumann.puml)-->
<br>
<small>Crédito da imagem: autoria própria (2023)</small>

A IoT é uma arquitetura distribuída, onde cada dispositivo possui um processador e uma memória própria. Os dados de entrada do dispositivo são compostos por sensores e os dados de saída são compostos por atuadores ou, simplesmente, transmitem os dados para outro dispositivo.

[![Arquitetura simplificada de IoT](http://tinyurl.com/2yqp82q2)](http://tinyurl.com/2yqp82q2)<!--![Arquitetura simplificada de IoT](../../../assets/puml/iot_architecture.puml)-->
<br>
<small>Crédito da imagem: autoria própria (2023)</small>

## Microcontroladores

Um microcontrolador é um "computador" em um chip. Ele possui um processador, memória e periféricos de entrada e saída. O microcontrolador é um computador completo, mas com recursos limitados. Ele é projetado para executar uma tarefa específica, como controlar um motor, acender um LED ou lâmpada, um interruptor, uma tomada etc.

Assim, um microcontrolador tem tudo os que os primeiros computadores tinham.

Vamos estudar o Arduíno, um microcontrolador de código aberto. O Arduíno é uma plataforma de prototipagem eletrônica de hardware livre e de placa única, projetada com um microcontrolador Atmel AVR com suporte de entrada/saída embutido, uma linguagem de programação padrão, a qual tem origem em Wiring, e é essencialmente C/C++.

# Arduíno

O Arduíno Uno R3, por exemplo, tem:

- Um microcontrolador ATmega328P
- 2KB de memória RAM ou mais
- 32KB de memória Flash ou mais
- 14 pinos de entrada/saída digital
- 6 pinos de entrada analógica
- 6 pinos de saída PWM
- 1 porta USB
- 1 porta serial
- 1 botão de reset
- 1 LED de status 
- 1 LED de TX
- 1 LED de RX
- 1 LED de Power
- 1 conector de alimentação

{%
    include figure
    image_path="/assets/images/lessons/iot/iot_arduino_uno.png"
    alt="Arduino Uno"
    caption="Crédito da imagem: ThinkerCad (2023)"
%}
{: .align-center}

A entrada digital pode verificar se um interruptor ou chave está ligado ou desligado. Uma entrada analógica pode medir a tensão de uma bateria ou a intensidade de luz. 

Uma saída digital pode ligar ou desligar um LED ou um motor. Uma saída analógica pode controlar a velocidade de um motor ou a intensidade de uma lâmpada.

### Fonte de alimentação

O Arduíno pode ser alimentado por uma fonte de alimentação externa ou por uma porta USB. A fonte de alimentação externa pode ser uma bateria ou uma fonte de alimentação AC/DC. A porta USB pode ser utilizada para alimentar o Arduíno e para enviar e receber dados.

Se for utilizar uma fonte de alimentação externa AC/DC ou baterias, o valor da tensão deve estar entre 7V e 12V. 

Quando o Arduíno está ligado, um LED "ON" acende. 

### Conexões do Arduíno

Vamos entender para quê serve cada pino do Arduíno? 

{%
    include figure
    image_path="/assets/images/lessons/iot/iot_arduino_uno.png"
    alt="Arduino Uno"
    caption="Crédito da imagem: ThinkerCad (2023)"
%}
{: .align-center}

| Pino  | Descrição                            | Observações                                           |
| ----- | ------------------------------------ | ----------------------------------------------------- |
| IOREF | Tensão que o Arduíno está utilizando | -                                                     |
| RESET | Botão de reset                       | Reinicializa o Arduíno                                |
| 3.3V  | Tensão de saída de 3.3V              | Corrente nominal de 50mA                              |
| 5V    | Tensão de saída de 5V                | Corrente nominal de 300mA                             |
| GND   | Tensão 0V                            | -                                                     |
| Vin   | Tensão de entrada                    | Varia de acordo com a alimentação                     |
| A0-A5 | Pinos de entrada analógica           | Usamos para medir tensão                              |
| 0-13  | Pinos de entrada/saída digital       | Usamos para ligar/desligar LEDs e outras coisas       |
| AREF  | Tensão de referência analógica       | Utilizada para calibrar a tensão de entrada analógica |

Nós poderemos configurar esses pinos como entrada digital. Se o pino estiver acima de 2,5V (HIGH), ele será considerado como 1. Se o pino estiver abaixo de 2,5V (LOW), ele será considerado como 0.

Os pinos que contêm um sinal de til (~) podem ser configurados como saída analógica. Nós poderemos controlar a intensidade de uma lâmpada ou a velocidade de um motor, variando de 0V a 5V. Eles são chamados de PWM (Pulse Width Modulation). São os pinos 3, 5, 6, 9, 10 e 11.

O pino 13 está ligado ao LED L da placa. O LED L acende quando o pino 13 está em HIGH e apaga quando o pino 13 está em LOW.

Os pinos 0 e 1 são utilizados para comunicação serial. O pino 0 é RX (Receber) e o pino 1 é TX (Transmitir). Eles são utilizados para enviar e receber dados para outros dispositivos.

Para programar no Arduíno, utilizaremos a linguagem C. Veja um código de exemplo:

```c++
    // Código C++ 

    int pinoLed = 12;

    void setup()
    {
        pinMode(pinoLed, OUTPUT);
    }

    void loop()
    {
        digitalWrite(pinoLed, HIGH);
        delay(1000);    // Espera por 1000 milissegundos
        digitalWrite(pinoLed, LOW);
        delay(1000);    
    }
```

# Referências

[^1]: WE ARE SOCIAL. Digital 2023: Global Overview Report. Disponível em: <https://wearesocial.com/uk/blog/2023/01/digital-2023/>. Acesso em: 04 de set. de 2023.

[^2]: FORBES. IoT: até 2025, mais de 27 bilhões de dispositivos estarão conectados. Disponível em: <https://forbes.com.br/forbes-tech/2022/08/iot-ate-2025-mais-de-27-bilhoes-de-dispositivos-estarao-conectados/>. Acesso em: 04 de set. de 2023.