---
layout: home
author_profile: true
title: BIOS e Setup de um PC
permalink: /lessons/hardware/setup/intro/
sidebar:
    nav: "hardware"
---
Criado em Junho de 2023 por *Maxwell Anderson*

<figure style="text-align:center">
    <img src="../../../../assets/images/gpt/cat_setup5.jpg" width="350" alt="Gato realizando a configuração do setup. Prompt: Crie uma imagem de um gato técnico em manutenção de computadores que está realizando a configuração do setup de BIOS, olhando para a tela de um computador.">
    <figcaption>Gato realizando a configuração do setup.</figcaption>
    <small>Prompt: crie uma imagem de um gato técnico em manutenção de computadores que está realizando a configuração do setup de BIOS, olhando para a tela de um computador.</small>
    <br>
    <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
</figure>

# Introdução

O BIOS, ou Sistema Básico de Entrada e Saída (Basic Input/Output System), é utilizado para realização da inicialização do hardware do computador, bem como fornece serviços para os sistemas operacionais e programas de aplicação. Hoje em dia são gravados em chips de memória flash, podendo ser atualizados pelo usuário. Todavia cria possibilidades para ataques de malware. Assim sendo, o BIOS é o firmware de um PC.

<figure style="text-align:center">
    <a href="https://commons.wikimedia.org/wiki/File:Elitegroup_761GX-M754_-_AMIBIOS_(American_Megatrends)_in_a_Winbond_W39V040APZ-5491.jpg#/media/File:Elitegroup_761GX-M754_-_AMIBIOS_(American_Megatrends)_in_a_Winbond_W39V040APZ-5491.jpg">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Elitegroup_761GX-M754_-_AMIBIOS_%28American_Megatrends%29_in_a_Winbond_W39V040APZ-5491.jpg" alt="Elitegroup 761GX-M754 - AMIBIOS (American Megatrends) in a Winbond W39V040APZ-5491.jpg" height="480" width="640">
    </a>
    <figcaption>Elitegroup 761GX-M754 - AMIBIOS (American Megatrends) in a Winbond W39V040APZ - memória flash</figcaption>
    <small>
        By © Raimond Spekking / CC BY-SA 4.0 (via Wikimedia Commons), <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=53826924">Link</a>
    </small>
</figure>

O Setup é um programa que localizado nessa memória flash da placa-mãe, que é executado quando o computador é ligado. Ele é responsável por fazer a configuração inicial do computador, como por exemplo, verificar se todos os componentes estão funcionando corretamente, permite ajustar parâmetros de funcionamento do computador, como por exemplo, a data e hora, a ordem de inicialização dos dispositivos de armazenamento, o gerenciamento de energia, da memória, da CPU e de outros dispositivos.

# Sequência de inicialização

A sequência de inicialização de um computador é a seguinte:

<figure style="text-align:center;">
    <a href="https://commons.wikimedia.org/wiki/File:Legacy_BIOS_boot_process_fixed.png#/media/File:Legacy_BIOS_boot_process_fixed.png">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/20/Legacy_BIOS_boot_process_fixed.png" alt="Legacy BIOS boot process fixed.png" height="152" width="640"  style="text-align:center; background-color:white; border-radius:15px; padding:10px">
    </a>
    <br>
    <figcaption>
    By Amila Ruwan 20, adapted by Marvin Borner - <a class="external free" href="https://commons.wikimedia.org/wiki/File:Legacy_BIOS_boot_process.png"></a><a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=127392282">Link</a>
    </figcaption>
</figure>

1. O computador é ligado e o BIOS é executado;
2. Verifica os dados armazenados e configurados no CMOS através do Setup;
3. É realizado o autoteste de inicialização (POST - Power-On Self-Test);

    <figure style="text-align:center;">
        <a href="https://commons.wikimedia.org/wiki/File:POST_P5KPL.jpg#/media/Ficheiro:POST_P5KPL.jpg">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/92/POST_P5KPL.jpg" alt="POST P5KPL.jpg" height="480" width="606">
        </a>
        <figcaption>
            Por AMI - <span class="int-own-work" lang="pt">Obra do próprio</span>, domínio público, <a href="https://commons.wikimedia.org/w/index.php?curid=4938576">Link</a>
        </figcaption>
    </figure>

   1. Vale a pena observar que é neste momento que todos os componentes do computador são testados, como por exemplo, memória, processador, placa-mãe etc., e se algum componente não estiver funcionando corretamente, o computador não irá inicializar.
   2. Desta forma, é possível verificar qual componente não funcionou corretamente, pois o BIOS emite um código de erro, que pode ser um beep sonoro, um código numérico no monitor ou em uma placa de diagnóstico apropriada.

    <figure style="text-align:center">
        <a href="https://commons.wikimedia.org/wiki/File:POST2.png#/media/Ficheiro:POST2.png">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/POST2.png" alt="POST2.png" height="413" width="660">
        </a>
        <figcaption>
            Segundo estágio de um POST (BIOS AMI)
        </figcaption>
        <small>
            Por Oona Räisänen/<a href="https://en.wikipedia.org/wiki/User:Mysid" class="extiw" title="w:User:Mysid">Mysid</a>, domínio público, <a href="https://commons.wikimedia.org/w/index.php?curid=14718137">link</a>
        </small>
    </figure>

4. Alguns dados de configuração são transferidos para a memória RAM;
5. Realização da leitura do MBR (Master Boot Record) do disco rígido.
   1. Aqui são carregados os arquivos necessários para a inicialização do sistema operacional, no setor de boot do disco rígido. Ali contém o bootloader.
   2. A configuração do boot vai depender do sistema operacional instalado, podendo ser o Windows, Linux, Mac OS, Android etc.
6. O sistema operacional é carregado na memória RAM, começando pelo seu kernel.

    <figure style="text-align:center">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/VOC83aZy_NI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        <figcaption>Demonstração de carregamento do Windows 11 - com problemas</figcaption>
    </figure>