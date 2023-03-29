---
layout: home
author_profile: true
title: Prototipação em impressoras 3D
permalink: /lessons/prototype/3dprinter/
---

- [Introdução](#introdução)
- [Processos para prototipação e de impressão 3D](#processos-para-prototipação-e-de-impressão-3d)
  - [Modelagem utilizando Thinkercad](#modelagem-utilizando-thinkercad)
  - [Fatiamento utilizando Cura](#fatiamento-utilizando-cura)
  - [Impressão](#impressão)
    - [Preparação](#preparação)
- [Cuidados com filamentos](#cuidados-com-filamentos)

# Introdução

Impressão 3D é um ótimo recurso para prototipagem rápida e barata. Aqui você irá aprender a utilizar o software de modelagem 3D [Blender](https://www.blender.org/) para criar modelos 3D e o software de impressão 3D [Cura](https://ultimaker.com/software/ultimaker-cura) para gerar os arquivos de impressão.

# Processos para prototipação e de impressão 3D

A impressão 3D é um processo de fabricação aditiva, ou seja, o material é adicionado camada por camada até que o objeto seja construído. A impressão 3D é feita por uma impressora 3D, que é composta por um extrusor, um leitor de cartão SD, um painel de controle e um motor de passo.

O extrusor é responsável por extrair o material e depositá-lo na camada. O leitor de cartão SD é responsável por ler o arquivo de impressão. O painel de controle é responsável por controlar a impressora 3D. O motor de passo é responsável por mover o extrusor.

As etapas para a impressão 3D são:

1. Criar ou utilizar modelo 3D
   1. Criação
      1. [SketchUp](https://www.sketchup.com/)
      2. Solid Works
      3. [Thinkercad](https://www.tinkercad.com/)
   2. Repositórios de arquivos 3D
      * [Thingiverse](https://www.thingiverse.com/)
2. Fatiar o modelo 3D
   1. Ultimate Cura
   2. _Específico do fabricante_
3. Realizar impressão 3D
   1. Utilização do modelo *.gcode gerado pelo Cura
   2. Imprimir utilizando filamento PLA, ABS ou Resina

## Modelagem utilizando Thinkercad

O Thinkercad é um software de modelagem 3D online, gratuito e sem necessidade de cadastro. Ele permite a criação de modelos 3D e a impressão 3D. Para utilizar o Thinkercad, basta acessar o site [https://www.tinkercad.com/](https://www.tinkercad.com/). O Thinkercad possui uma interface intuitiva e fácil de utilizar. Para criar um novo projeto, basta clicar em "New Project" e selecionar o tipo de projeto que deseja criar. Para criar um modelo 3D, basta selecionar "3D Design".

![Thinkercad - New Project](/assets/images/lessons/prototype/3dprinter/thinkercad-new-project.png)

![Thinkercad - 3D Design](/assets/images/lessons/prototype/3dprinter/thinkercad-3d-design.png)

Para criar um modelo 3D, basta clicar em "Add a 3D Model" e selecionar o modelo que deseja utilizar. Para criar um modelo 3D, basta clicar em "Add a 3D Model" e selecionar o modelo que deseja utilizar. Para criar um modelo 3D, basta clicar em "Add a 3D Model" e selecionar o modelo que deseja utilizar.

![Thinkercad - Add a 3D Model](/assets/images/lessons/prototype/3dprinter/thinkercad-add-3d-model.png)

## Fatiamento utilizando Cura

O Cura é um software de modelagem 3D que permite a criação de modelos 3D e a impressão 3D. Para utilizar o Cura, basta acessar o site [https://ultimaker.com/software/ultimaker-cura](https://ultimaker.com/software/ultimaker-cura). O Cura possui uma interface intuitiva e fácil de utilizar. Para criar um novo projeto, basta clicar em "New Project" e selecionar o tipo de projeto que deseja criar. Para criar um modelo 3D, basta selecionar "3D Design".

![Cura - New Project](/assets/images/lessons/prototype/3dprinter/cura-new-project.png)

![Cura - 3D Design](/assets/images/lessons/prototype/3dprinter/cura-3d-design.png)

- Deverá realizar o preenchimento para suporte das peças "soltas".
- Para realizar o fatiamento...
- Flashforge é um aplicativo que permite o a fatiamento da impressora Flashforge Finder.
- Exportar o arquivo para o formato *.gcode

## Impressão

Para realizar a impressão, basta utilizar o arquivo *.gcode gerado pelo Cura e inseri-lo na impressora 3D.

### Preparação

- Verificar temperatura da mesa
- Composição e estrutura do modelo
- Duração e quantidade de filamento
- Alinhamento da mesa
- Aquecer bico extrusor para inserir/retirar filamento
- Preenchimento do bico extrusor
  
# Cuidados com filamentos

- PLA é sensível à umidade, deve estar guardada em local seco e fechado.
- ABS é sensível à temperatura.
- 