---
layout: home
author_profile: true
title: BIOS - Beep Codes
permalink: /lessons/hardware/setup/beep_codes/
sidebar:
    nav: "hardware-setup"
---
Criado em Junho de 2023 por *Maxwell Anderson*

<figure style="text-align:center">
    <img src="../../../../assets/images/gpt/cat_setup5.jpg" width="350" alt="Gato realizando a configuração do setup. Prompt: Crie uma imagem de um gato técnico em manutenção de computadores que está realizando a configuração do setup de BIOS, olhando para a tela de um computador.">
    <figcaption>Gato realizando a configuração do setup.</figcaption>
    <small>Prompt: crie uma imagem de um gato técnico em manutenção de computadores que está realizando a configuração do setup de BIOS, olhando para a tela de um computador.</small>
    <br>
    <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
</figure>

- [Introdução](#introdução)
- [Tabela de códigos de erro](#tabela-de-códigos-de-erro)
  - [BIOS  POST  Beep  code  (AMI  standard)](#bios--post--beep--code--ami--standard)
    - [PEI  Beep  Codes](#pei--beep--codes)
    - [DXE  Beep  Codes](#dxe--beep--codes)

# Introdução

BIOS Beep Codes são códigos de erro emitidos pelo BIOS durante a inicialização do computador. Esses códigos são emitidos através de beeps. Cada fabricante de BIOS possui uma tabela de códigos de erro, que pode ser encontrada no manual da placa-mãe ou no site do fabricante.  

# Tabela de códigos de erro

Fonte: [Gygabyte Technology, 2017](https://download.gigabyte.com/FileList/Manual/server_manual_bios_e_purley_bmc_10.pdf)

## BIOS  POST  Beep  code  (AMI  standard)

### PEI  Beep  Codes

| **#  de  Beeps** | **Descrição**                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------- |
| 1                | Memória não instalada.                                                                        |
| 1                | A memória foi instalada duas vezes (o PEI Core instalou a rotina InstallPeiMemory duas vezes) |
| 2                | Recuperação iniciada                                                                          |
| 3                | DXEIPL  não foi encontrado                                                                    |
| 3                | DXE Core Firmware Volume não foi encontrado                                                   |
| 4                | Recuperação falhou                                                                            |
| 4                | S3 Resume falhou                                                                              |
| 7                | Reset  PPI  não está  disponível                                                              |

### DXE  Beep  Codes

| **#  de  Beeps** | **Descrição**                                                       |
| ---------------- | ------------------------------------------------------------------- |
| 1                | Senha  inválida                                                     |
| 4                | Alguns dos  protocolos arquiteturais não estão disponíveis          |
| 5                | Nenhum Dispositivo de Saída de Console é encontrado                 |
| 5                | Nenhum Dispositivo de Entrada de Console é encontrado               |
| 6                | A atualização de Flash falhou                                       |
| 7                | O protocolo Reset não está disponível                               |
| 8                | Os requisitos de recursos PCI da plataforma não podem ser atendidos |
