---
layout: home
author_profile: true
title: BIOS - Manutenação Corretiva
permalink: /lessons/hardware/setup/corrective/
sidebar:
    nav: "hardware-setup"
---
Criado em Junho de 2023 por *Maxwell Anderson*

<figure style="text-align:center">
    <img src="../../../../assets/images/gpt/cat_setup4.jpg" width="350" alt="Gato realizando a configuração do setup. Prompt: Crie uma imagem de um gato técnico em manutenção de computadores que está realizando a configuração do setup de BIOS, olhando para a tela de um computador.">
    <figcaption>Gato realizando a configuração do setup.</figcaption>
    <small>Prompt: crie uma imagem de um gato técnico em manutenção de computadores que está realizando a configuração do setup de BIOS, olhando para a tela de um computador.</small>
    <br>
    <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
</figure>

# Introdução

A manutenção corretiva de computadores é realizada quando o computador apresenta algum problema. Nesse caso, é necessário identificar a causa do problema e realizar a manutenção adequada.

# Problemas comuns

Os problemas mais comuns que podem ocorrer com o BIOS são:

- O computador não liga;
- O computador liga, mas não inicia o sistema operacional;
- O computador liga, mas apresenta erros durante a inicialização;
- O computador liga, mas apresenta erros durante a execução do sistema operacional.
- O computador liga, mas apresenta erros durante a execução de um programa.

# Uso das placas de diagnóstico POST

As placas de diagnóstico POST são utilizadas para identificar problemas de inicialização do computador. Essas placas são conectadas à placa-mãe e exibem códigos de erro durante a inicialização do computador. Esses códigos de erro podem ser utilizados para identificar o problema e realizar a manutenção adequada. 

<figure style="text-align:center">
    <a href="https://commons.wikimedia.org/wiki/File:POST_card_3usd.jpg#/media/File:POST_card_3usd.jpg">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/49/POST_card_3usd.jpg" alt="POST card 3usd.jpg" width="500">
    </a>
    <figcaption>
        Placa de diagnóstico POST.
    </figcaption>
    <small>By <a href="//commons.wikimedia.org/w/index.php?title=User:Rumlin&amp;amp;action=edit&amp;amp;redlink=1" class="new" title="User:Rumlin (page does not exist)">Rumlin</a> - <span class="int-own-work" lang="en">own work</span>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=8974635">link</a>
    </small>
</figure>

> ℹ️ **Dica**
>
> O código gerado deverá ser comparada com a tabela de códigos POST conforme pode ser observado em [BIOS - Post Codes](/lessons/hardware/setup/post_codes/).

<figure style="text-align:center">
    <a href="https://commons.wikimedia.org/wiki/File:BIOS_POST_card_for_PCI,_PCIe_and_LPC_bus.jpg#/media/File:BIOS_POST_card_for_PCI,_PCIe_and_LPC_bus.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/4/42/BIOS_POST_card_for_PCI%2C_PCIe_and_LPC_bus.jpg" alt="BIOS POST card for PCI, PCIe and LPC bus.jpg" width="500"></a>
    <figcaption>
        Placa de diagnóstico POST para PCI.
    </figcaption>
    <small>By <a href="//commons.wikimedia.org/wiki/User:Markus_Kuhn" title="User:Markus Kuhn">Markus Kuhn</a> - I took this photo using my smartphone camera, <a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en" title="Creative Commons Zero, Public Domain Dedication">CC0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=80926198">Link</a>
    </small>
</figure>

# Solução de problemas

## O computador não liga

Quando o computador não liga, deve-se seguir os seguintes passos:

1. Verifique a fonte de alimentação conforme descrito no assunto relacionado à [manutenção corretiva de **Fonte de Alimentação**](/lessons/hardware/psu/corrective/).
2. Se a fonte está funcionando corretamente, verifique se o computador emite beeps durante a inicialização. Caso emita, verifique as tabelas BIOS Post Codes conforme o modelo da BIOS da placa-mãe.

    > ℹ️ **Dica**
    >
    > Esta informação poderá ser encontradas no manual da placa-mãe ou no site do fabricante, bem como algumas tabelas poderão ser encontradas em [BIOS - Post Codes](/lessons/hardware/setup/post_codes/).

## O computador liga, mas apresenta erros durante a inicialização

Quando o computador liga, mas apresenta erros durante a inicialização, deve-se seguir os seguintes passos:

1. Verifique se o computador emite beeps durante a inicialização. Caso emita, verifique as tabelas BIOS Post Codes conforme o modelo da BIOS da placa-mãe.

    > ℹ️ **Dica**
    >
    > Esta informação poderá ser encontradas no manual da placa-mãe ou no site do fabricante, bem como algumas tabelas poderão ser encontradas em [BIOS - Post Codes](/lessons/hardware/setup/post_codes/).

2. Verifique se o sistema operacional está instalado corretamente. Caso não esteja, reinstale o sistema operacional e siga os passos abaixo.

## O computador liga, mas não inicia o sistema operacional

Quando o computador liga, mas não inicia o sistema operacional, deve-se seguir os seguintes passos:

1. Verifique se o disco rígido está sendo reconhecido pelo BIOS. Caso não esteja, verifique a conexão do cabo SATA ou IDE e a alimentação do disco rígido.
2. Verifique se o disco rígido está sendo reconhecido pelo sistema operacional. Caso não esteja, verifique se o disco rígido está formatado e se o sistema de arquivos é compatível com o sistema operacional.
3. Verifique se o disco rígido está com problemas. Caso esteja, substitua o disco rígido.
4. Verifique se o sistema operacional está instalado corretamente. Caso não esteja, reinstale o sistema operacional.
5. Se verificado mais outros erros no sistema operacional, realize os passos abaixo.

## O computador liga, mas apresenta erros durante a execução do sistema operacional

Quando o computador liga, mas apresenta erros durante a execução do sistema operacional, deve-se seguir os seguintes passos:

1. Verifique se o sistema operacional está atualizado. Caso não esteja, atualize o sistema operacional.
2. Verifique se o sistema operacional está infectado por vírus. Caso esteja, remova o vírus do sistema operacional.
3. Verifique se o sistema operacional está corrompido. Caso esteja, reinstale o sistema operacional.
