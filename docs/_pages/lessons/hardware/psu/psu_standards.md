---
layout: home
author_profile: true
title: Padrões de fontes de alimentação
permalink: /lessons/hardware/psu/psu_standards/
sidebar:
  nav: "hardware"
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>

Criado em Março de 2023 por _Maxwell Anderson_

<figure style="text-align:center">
    <img src="../../../../assets/images/gpt/cat_hardware3.jpg" width="350" alt="Gato estudando com óculos. Prompt: Create an image of a computer maintenance technician cat repairing computer power supply">
    <figcaption>Gato técnico em manutenção de computadores consertando uma fonte de alimentação</figcaption>
    <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
</figure>

Conteúdo
--------

- [Padrões de fontes de alimentação](#padrões-de-fontes-de-alimentação)
  - [O padrão AT](#o-padrão-at)
  - [O padrão ATX](#o-padrão-atx)
    - [Pinos](#pinos)

# Padrões de fontes de alimentação

## O padrão AT

O padrão AT (Advanced Technology) foi desenvolvido nos anos 80 pela IBM e foi utilizada até meados dos anos 90. Possuía dois conectores de 6 pinos cada. Essa fonte não possibilitava que o computador operasse em modo de baixa potência, ou _standby_. Ou ele ficava totalmente ligado ou totalmente desligado. Não permitia o desligamento automático do computador, como é possível fazer hoje em dia.

Naquela época, era necessário solicitar ao sistema operacional o "estacionamento" das cabeças de leitura e escrita dos discos rígidos, o que era feito através de um comando específico. Caso o usuário não executasse esse comando, as cabeças de leitura e escrita dos discos rígidos ficariam em movimento, o que poderia danificar o disco rígido. Após isto, o computador era desligado.

Com o tempo, os sistemas operacionais realizam este procedimento ao selecionar a opção "desligar" ou "power off" no menu de opções do sistema operacional. Ao final, o sistema operacional exibia uma mensagem informando que era possível desligar o computador com segurança. Só depois disto, você poderia apertar o interruptor de desligamento do computador que ficava na parte frontal do gabinete.

## O padrão ATX

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/ATX-Netzteil.jpg" alt="ATX-Netzteil.jpg" height="469" width="640">
    <figcaption>Fonte de alimentação típica ATX 1.3</figcaption>
    <small>Fonte: <a href="https://commons.wikimedia.org/wiki/File:ATX-Netzteil.jpg">Wikipedia</a> Acessado em abril de 2023. Licença: <a href="https://creativecommons.org/licenses/by-sa/2.0/de/deed.en" title="Creative Commons Attribution-Share Alike 2.0">CC BY-SA 2.0</a> de <a href="https://commons.wikimedia.org/w/index.php?curid=33037977">Hiperligação</a></small>
</figure>

<figure style="text-align:center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/ATX_power_supply_interior.jpg" alt="ATX power supply interior.jpg" height="720" width="733">
    <figcaption>Vista interna em uma fonte de alimentação ATX</figcaption>
    <small>
        Por <a href="//commons.wikimedia.org/wiki/User:Alan_Liefting" title="User:Alan Liefting">Alan Liefting</a> - <span class="int-own-work" lang="pt">Obra do próprio</span>, domínio público, <a href="https://commons.wikimedia.org/w/index.php?curid=3519966">Hiperligação</a>
    </small>
</figure>

O padrão ATX (Advanced Technology Extended) foi desenvolvido nos anos 90 pela Intel e foi utilizada até meados dos anos 2000, sucedendo o padrão AT. Possuía dois conectores de 20 pinos cada. Essa fonte possibilitava que o computador operasse em modo de baixa potência, ou _standby_.

Possui um interruptor de desligamento automático do computador, que é conectado diretamente à placa-mãe, enviando um sinal de pedido de desligamento para o sistema operacional. O sistema operacional, por sua vez, solicita o fechamento dos aplicativos e arquivos abertos, bem como solicita ao sistema de arquivos que estacione as cabeças de leitura e escrita dos discos rígidos, "desligando" a fonte e o computador. Todavia, a fonte não é desligada totalmente, pois o computador ainda está em modo de baixa potência, ou _standby_, aguardando o pedido de ligamento do usuário.

Para desligar totalmente esta fonte, é necessário apertar o interruptor de desligamento que fica na parte traseira do gabinete ou retirando o cabo de alimentação da tomada.

### Pinos

Segue foto do plugue ATX 2.x de 24 pinos:

<figure style="text-align: center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/24-pin_ATX_power_plug_from_a_Seasonic_PSU_20131105.jpg" alt="24-pin ATX power plug from a Seasonic PSU 20131105.jpg" height="593" width="800">
    <figcaption>Plugue de alimentação da placa-mãe ATX de 24 pinos; os pinos 11, 12, 23 e 24 formam um plugue de quatro pinos separado destacável, tornando-o compatível com receptáculos ATX de 20 pinos</figcaption>
    <small>
        Fonte: <a href="https://en.wikipedia.org/wiki/User:Dsimic" class="extiw" title="wikipedia:User:Dsimic">Dsimic</a> em <a href="https://en.wikipedia.org/wiki/" class="extiw" title="wikipedia:">Wikipédia em inglês</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=31269900">Hiperligação</a>
    </small>
</figure>

| Pino | Cor | Cor | Pino |
| :--: | :-: | :-: | :--: |
|  1   | 🟧  | 🟧  |  13  |
|  2   | 🟧  | 🟦  |  14  |
|  3   | ⬛  | ⬛  |  15  |
|  4   | 🟥  | 🟩  |  16  |
|  5   | ⬛  | ⬛  |  17  |
|  6   | 🟥  | ⬛  |  18  |
|  7   | ⬛  | ⬛  |  19  |
|  8   | CZ  | RV  |  20  |
|  9   | 🟪  | 🟥  |  21  |
|  10  | 🟨  | 🟥  |  22  |
|  --  | --  | --  |  --  |
|  11  | 🟨  | 🟥  |  23  |
|  12  | 🟧  | ⬛  |  24  |

<small>Pinagem dos conectores ATX 2.x</small><br>
<small>Fonte: autoria própria (2023)</small>

Possui 3 tensões principais de saída: 3,3V, 5V e 12V. A tensão de 12V é a mais importante, pois é a que fornece energia para os componentes mais potentes do computador, como o processador e a placa de vídeo. A tensão de 5V é a que fornece energia para os componentes menos potentes, como a placa de som e o circuito do HD. A tensão de 3,3V é a que fornece energia para os componentes menos potentes, como a memória RAM e o SSD. Existem fontes de baixa potência, como -12V e +5V<sub>SB</sub>, sendo que este último fornece tensão para o circuito de alimentação do computador, que é responsável por alimentar o computador quando ele está em modo de baixa potência, ou _standby_, e para alimentar o relógio interno do computador.

Segue a tabela de pinos do conector ATX 2.x de 24 pinos:

| Pino |    Cor    |   Sinal    | Descritivo                                                                          |
| :--: | :-------: | :--------: | :---------------------------------------------------------------------------------- |
|  1   |    🟧     |   +3,3V    |                                                                                     |
|  2   |    🟧     |   +3,3V    |                                                                                     |
|  3   |    ⬛     |    GND     |                                                                                     |
|  4   |    🟥     |    +5V     |                                                                                     |
|  5   |    ⬛     |    GND     |                                                                                     |
|  6   |    🟥     |    +5V     |                                                                                     |
|  7   |    ⬛     |    GND     |                                                                                     |
|  8   |   Cinza   | Power good | Quando as outras saídas estão prontas para fornecer energia. É um sinal de controle |
|  9   |    🟪     |    +5V     | Stand by                                                                            |
|  10  |    🟨     |    12V     |                                                                                     |
|  11  |    🟨     |    12V     | Somente no conector de 24 pinos                                                     |
|  12  |    🟧     |   +3,3V    | Somente no conector de 24 pinos                                                     |
|  13  |    🟧     |   +3,3V    |                                                                                     |
|  14  |    🟦     |    -12V    |                                                                                     |
|  15  |    ⬛     |    GND     |                                                                                     |
|  16  |    🟩     |  Power on  | Quando jampeado com um pino de GND, a fonte é ligada.                               |
|  17  |    ⬛     |    GND     |                                                                                     |
|  18  |    ⬛     |    GND     |                                                                                     |
|  19  |    ⬛     |    GND     |                                                                                     |
|  20  | Reservado |            | Anteriormente era -5V. Fora de uso.                                                 |
|  21  |    🟥     |    +5V     |                                                                                     |
|  22  |    🟥     |    +5V     |                                                                                     |
|  23  |    🟥     |    +5V     | Somente no conector de 24 pinos                                                     |
|  24  |    ⬛     |    GND     | Somente no conector de 24 pinos                                                     |

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/ATX-Netzteil.jpg" alt="ATX-Netzteil.jpg" height="469" width="640">
    <figcaption>Fonte de alimentação típica ATX 1.3</figcaption>
    <small>Fonte: <a href="https://commons.wikimedia.org/wiki/File:ATX-Netzteil.jpg">Wikipedia</a> Acessado em abril de 2023. Licença: <a href="https://creativecommons.org/licenses/by-sa/2.0/de/deed.en" title="Creative Commons Attribution-Share Alike 2.0">CC BY-SA 2.0</a> de <a href="https://commons.wikimedia.org/w/index.php?curid=33037977">Hiperligação</a></small>
</figure>

Existem padrões menores, como o microATX e o miniATX.

