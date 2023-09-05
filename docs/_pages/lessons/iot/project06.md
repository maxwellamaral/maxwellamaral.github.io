---
author_profile: true
title: Projeto 06 - Sensor de umidade
permalink: /lessons/iot/project06/
sidebar:
    nav: "iot"
layout: single
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_arduino06.jpg
    caption: "Gato estudando IOT | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: Prompt: crie uma imagem de um gato usando gravata e que está aprendendo a usar um Arduíno. Faça o gato utilizar uma chave de fenda no Arduino. Faça com que ele use óculos."
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

Sensores de umidade são usados para detectar a umidade do solo em torno das raízes das plantas. Eles podem ser usados para alertar quando as plantas precisam ser regadas e, portanto, quando a umidade do solo está muito baixa. Eles podem ser usados em um sistema de irrigação automático, em que o solo é regado quando a umidade cai abaixo de um determinado nível ou quando a umidade é mantida em um nível definido.

Para isso, iremos utilizar a seguinte lista de materiais[^1]:

| Nome | Componente                | Quantidade |
| ---- | ------------------------- | ---------- |
| U1   | Arduino Uno R3            | 1          |
| SEN1 | Sensor de umidade do solo | 1          |
| D1   | Vermelho LED              | 1          |
| D2   | Laranja LED               | 1          |
| D3   | Amarelo LED               | 1          |
| D4   | Verde LED                 | 1          |
| R1   | 220 Ω Resistor            | 1          |
| D5   | Azul LED                  | 1          |

# Implementação

Este exemplo mostra como usar um servomotor para controlar a posição de um objeto. Vamos usar o pino 9 para controlar o servomotor. Em suma, o Arduino envia um sinal PWM para o servomotor, que gira para a posição desejada. Veja os comentários do código de exemplo para obter uma boa compreensão de seu funcionamento.

Vamos começar montando o circuito e depois iremos programar o Arduíno.

## Simulador Tinkercad

Para a implementação do projeto, iremos utilizar o simulador Tinkercad. Para isso, crie um novo projeto e adicione os componentes conforme a imagem abaixo:

{%
    include figure
    image_path="/assets/images/lessons/iot/project06_led01.png"
    alt="Projeto 06 - Controle de umidade do solo"
    caption="Fonte: TinkerCad (2023)"
%}
{: .align-center}

O sensor de humidade possui 3 pinos:

- Potência (VCC): 3,3V a 5V
- Terra (GND): GND
- Sinal (S): Pino analógico

O pino de potência (VCC) é conectado ao pino A0 do Arduíno. O pino de terra (GND) é conectado ao pino GND do Arduíno e pino de sinal (S) é conectado ao pino A1 do Arduíno.

Veja como fica o código abaixo:

```c++
int umidade = 0;

void setup()
{
  pinMode(A0, OUTPUT);
  pinMode(A1, INPUT);
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop()
{
  // Aplique energia ao sensor de umidade do solo
  digitalWrite(A0, HIGH);
  delay(10); 
  umidade = analogRead(A1);
  // Desligue o sensor para reduzir a corrosão do metal ao longo do tempo
  digitalWrite(A0, LOW);
  Serial.println(umidade);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  if (umidade < 200) {
    digitalWrite(12, HIGH);
  } else {
    if (umidade < 400) {
      digitalWrite(11, HIGH);
    } else {
      if (umidade < 600) {
        digitalWrite(10, HIGH);
      } else {
        if (umidade < 800) {
          digitalWrite(9, HIGH);
        } else {
          digitalWrite(8, HIGH);
        }
      }
    }
  }
  delay(100); 
}
```
Após ligar o sensor de umidade, o Arduíno irá ler o valor do pino A1 e irá imprimir no monitor serial. Após isso, o Arduíno irá desligar o sensor e irá acender um LED de acordo com o valor lido.

Para abrir o monitor serial, clique no botão `🔌 Monitor serial` no canto inferior esquerdo da janela de código.

Agora, clique no botão `▶️ Iniciar simulação` e veja o resultado. 

Este projeto está também disponível em [TinkerCad: Projeto 06 - Sensor de umidade](https://www.tinkercad.com/things/5ufTPU6dx7p-powerful-waasa/editel?sharecode=sem3OcAbqZL19E8umhQy7rfl_WXbgOgm5saRQR0xB88)

# Referências

[^1]: Este projeto foi criado por TinkerCad. O exemplo de código é de domínio público. Modificado em 04 de set. de 2023 pelo autor. 