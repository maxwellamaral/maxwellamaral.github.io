---
author_profile: true
title: Projeto 05 - Micro servomotor
permalink: /lessons/iot/project05/
sidebar:
    nav: "iot"
layout: single
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_arduino01.jpg
    caption: "Gato estudando IOT | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos."
---

# Conceitos

{% 
  include figure 
  image_path="/assets/images/gpt/cat_arduino01.jpg" 
  alt="Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos" 
  caption="Fonte: gerado por IA com Bing por Maxwell Anderson (2023)<br>Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos." 
%}
{: .align-center} 

# Introdução

Servomotores são motores que podem ser controlados com precisão em uma determinada posição. Eles são usados em robótica, controle de rádio, dentro outros. Eles são pequenos, leves e podem ser conectados diretamente ao Arduino.

Para isso, iremos utilizar a seguinte lista de materiais[^1]:

|   ID   | Descrição         | Quantidade |
| :----: | :---------------- | :--------: |
|   1    | Arduino Uno       |     1      |
| SERVO1 | Micro Servo Motor |     1      |

# Implementação

Este exemplo mostra como usar um servomotor para controlar a posição de um objeto. Vamos usar o pino 9 para controlar o servomotor. Em suma, o Arduino envia um sinal PWM para o servomotor, que gira para a posição desejada. Veja os comentários do código de exemplo para obter uma boa compreensão de seu funcionamento.

Vamos começar montando o circuito e depois iremos programar o Arduíno.

## Simulador Tinkercad

Para a implementação do projeto, iremos utilizar o simulador Tinkercad. Para isso, crie um novo projeto e adicione os componentes conforme a imagem abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project05_led01.png"
    alt="Projeto 05 - Micro servomotor"
    caption="Fonte: TinkerCad (2023)"
%}
{: .align-center}

Insira os blocos conforme ilustrado abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project05_led02.png"
    alt="Código do Projeto 05 - Micro servomotor"
    caption="Fonte: TinkerCad (2023)"
%}
{: .align-center}

Veja como fica o código abaixo:

```c++
#include <Servo.h>

int pos = 0;

Servo servo_9;

void setup()
{
  // anexar o servo no pino 9 ao objeto servo_9
  servo_9.attach(9, 500, 2500);
}

void loop()
{
  // girar o servo de 0 a 180 graus em passos de 1 grau
  for (pos = 0; pos <= 180; pos += 1) {
    // diga ao servo para ir para a posição na variável 'pos'
    servo_9.write(pos);
    // espere 15 ms para o servo atingir a posição
    delay(15); 
  }
  for (pos = 180; pos >= 0; pos -= 1) {
    // diga ao servo para ir para a posição na variável 'pos'
    servo_9.write(pos);
    // espere 15 ms para o servo atingir a posição
    delay(15); 
  }
}
```

Agora, clique no botão `▶️ Iniciar simulação` e veja o resultado. Cada LED deve piscar a cada 1s de maneira sequencial.

Funciona! Por que você não tenta fazer outra coisa, como por exemplo colocar um potenciômetro para controlar a velocidade do giro? 😉

Este projeto está também disponível em [TinkerCad: Projeto 06 - Sensor de umidade](https://www.tinkercad.com/things/5ufTPU6dx7p-powerful-waasa/editel?sharecode=sem3OcAbqZL19E8umhQy7rfl_WXbgOgm5saRQR0xB88)

# Referências

[^1]: Este projeto foi criado por [Barragan](http://barraganstudio.com. O exemplo de código é de domínio público. Modificado em 8 de nov. de 2013 por Scott Fitzgerald. Disponível em <http://www.arduino.cc/en/Tutorial/Sweep>