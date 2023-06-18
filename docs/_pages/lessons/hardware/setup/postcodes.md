---
layout: home
author_profile: true
title: BIOS - Post Codes
permalink: /lessons/hardware/setup/post_codes/
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

## Conteúdo

- [Introdução](#introdução)
- [Tabela de códigos de erro](#tabela-de-códigos-de-erro)
  - [Códigos BIOS  POST](#códigos-bios--post)
    - [AMI  Standard  -  PEI](#ami--standard-----pei)
    - [AMI  Standard  -  DXE](#ami--standard-----dxe)
    - [AMI  Standard  -  ERROR](#ami--standard-----error)
    - [Intel  UPI  POST  Codes](#intel--upi--post--codes)
    - [Intel  UPI  Error  Codes](#intel--upi--error--codes)
    - [Intel  MRC  POST  Codes](#intel--mrc--post--codes)
    - [Intel  MRC  Error  Codes](#intel--mrc--error--codes)
    - [Intel  PM  POST  Codes](#intel--pm--post--codes)

# Introdução

BIOS Post Codes são códigos de erro emitidos pelo BIOS durante a inicialização do computador. Esses códigos são emitidos através de beeps ou através de um display de LED na placa-mãe. Cada fabricante de BIOS possui uma tabela de códigos de erro, que pode ser encontrada no manual da placa-mãe ou no site do fabricante.  

# Tabela de códigos de erro

Fonte: [Gygabyte Technology, 2017](https://download.gigabyte.com/FileList/Manual/server_manual_bios_e_purley_bmc_10.pdf)

## Códigos BIOS  POST

### AMI  Standard  -  PEI

| Descrição                     | Código |
| ----------------------------- | ------ |
| PEI\_CORE\_STARTED            | 0x10   |
| PEI\_CAR\_CPU_INIT            | 0x11   |
| PEI\_CAR\_NB_INIT             | 0x15   |
| PEI\_CAR\_SB_INIT             | 0x19   |
| PEI\_MEMORY\_SPD_READ         | 0x2B   |
| PEI\_MEMORY\_PRESENCE_DETECT  | 0x2C   |
| PEI\_MEMORY\_TIMING           | 0x2D   |
| PEI\_MEMORY\_CONFIGURING      | 0x2E   |
| PEI\_MEMORY\_INIT             | 0x2F   |
| PEI\_MEMORY\_INSTALLED        | 0x31   |
| PEI\_CPU\_INIT                | 0x32   |
| PEI\_CPU\_CACHE_INIT          | 0x33   |
| PEI\_CPU\_AP_INIT             | 0x34   |
| PEI\_CPU\_BSP_SELECT          | 0x35   |
| PEI\_CPU\_SMM_INIT            | 0x36   |
| PEI\_MEM\_NB_INIT             | 0x37   |
| PEI\_MEM\_SB_INIT             | 0x3B   |
| PEI\_DXE\_IPL_STARTED         | 0x4F   |
| DXE\_CORE\_STARTED            | 0x60   |
| //Recovery                    |        |
| PEI\_RECOVERY\_AUTO           | 0xF0   |
| PEI\_RECOVERY\_USER           | 0xF1   |
| PEI\_RECOVERY\_STARTED        | 0xF2   |
| PEI\_RECOVERY\_CAPSULE_FOUND  | 0xF3   |
| PEI\_RECOVERY\_CAPSULE_LOADED | 0xF4   |
| //S3                          |        |
| PEI\_S3\_STARTED              | 0xE0   |
| PEI\_S3\_BOOT_SCRIPT          | 0xE1   |
| PEI\_S3\_VIDEO_REPOST         | 0xE2   |
| PEI\_S3\_OS_WAKE              | 0xE3   |

### AMI  Standard  -  DXE

| Descrição                            | Código |
| ------------------------------------ | ------ |
| DXE\_CORE\_STARTED                   | 0x60   |
| DXE\_NVRAM\_INIT                     | 0x61   |
| DXE\_SBRUN\_INIT                     | 0x62   |
| DXE\_CPU\_INIT                       | 0x63   |
| DXE\_NB\_HB_INIT                     | 0x68   |
| DXE\_NB\_INIT                        | 0x69   |
| DXE\_NB\_SMM_INIT                    | 0x6A   |
| DXE\_SB\_INIT                        | 0x70   |
| DXE\_SB\_SMM_INIT                    | 0x71   |
| DXE\_SB\_DEVICES_INIT                | 0x72   |
| DXE\_ACPI\_INIT                      | 0x78   |
| DXE\_CSM\_INIT                       | 0x79   |
| DXE\_BDS\_STARTED                    | 0x90   |
| DXE\_BDS\_CONNECT_DRIVERS            | 0x91   |
| DXE\_PCI\_BUS_BEGIN                  | 0x92   |
| DXE\_PCI\_BUS\_HPC\_INIT             | 0x93   |
| DXE\_PCI\_BUS_ENUM                   | 0x94   |
| DXE\_PCI\_BUS\_REQUEST\_RESOURCES    | 0x95   |
| DXE\_PCI\_BUS\_ASSIGN\_RESOURCES     | 0x96   |
| DXE\_CON\_OUT_CONNECT                | 0x97   |
| DXE\_CON\_IN_CONNECT                 | 0x98   |
| DXE\_SIO\_INIT                       | 0x99   |
| DXE\_USB\_BEGIN                      | 0x9A   |
| DXE\_USB\_RESET                      | 0x9B   |
| DXE\_USB\_DETECT                     | 0x9C   |
| DXE\_USB\_ENABLE                     | 0x9D   |
| DXE\_IDE\_BEGIN                      | 0xA0   |
| DXE\_IDE\_RESET                      | 0xA1   |
| DXE\_IDE\_DETECT                     | 0xA2   |
| DXE\_IDE\_ENABLE                     | 0xA3   |
| DXE\_SCSI\_BEGIN                     | 0xA4   |
| DXE\_SCSI\_RESET                     | 0xA5   |
| DXE\_SCSI\_DETECT                    | 0xA6   |
| DXE\_SCSI\_ENABLE                    | 0xA7   |
| DXE\_SETUP\_VERIFYING_PASSWORD       | 0xA8   |
| DXE\_SETUP\_START                    | 0xA9   |
| DXE\_SETUP\_INPUT_WAIT               | 0xAB   |
| DXE\_READY\_TO_BOOT                  | 0xAD   |
| DXE\_LEGACY\_BOOT                    | 0xAE   |
| DXE\_EXIT\_BOOT_SERVICES             | 0xAF   |
| RT\_SET\_VIRTUAL\_ADDRESS\_MAP_BEGIN | 0xB0   |
| RT\_SET\_VIRTUAL\_ADDRESS\_MAP_END   | 0xB1   |
| DXE\_LEGACY\_OPROM_INIT              | 0xB2   |
| DXE\_RESET\_SYSTEM                   | 0xB3   |
| DXE\_USB\_HOTPLUG                    | 0xB4   |
| DXE\_PCI\_BUS_HOTPLUG                | 0xB5   |
| DXE\_NVRAM\_CLEANUP                  | 0xB6   |
| DXE\_CONFIGURATION\_RESET            | 0xB7   |

### AMI  Standard  -  ERROR

| Descrição                           | Código |
| ----------------------------------- | ------ |
| PEI\_MEMORY\_INVALID_TYPE           | 0x50   |
| PEI\_MEMORY\_INVALID_SPEED          | 0x50   |
| PEI\_MEMORY\_SPD_FAIL               | 0x51   |
| PEI\_MEMORY\_INVALID_SIZE           | 0x52   |
| PEI\_MEMORY\_MISMATCH               | 0x52   |
| PEI\_MEMORY\_NOT_DETECTED           | 0x53   |
| PEI\_MEMORY\_NONE_USEFUL            | 0x53   |
| PEI_MEMORY_ERROR                    | 0x54   |
| PEI\_MEMORY\_NOT_INSTALLED          | 0x55   |
| PEI\_CPU\_INVALID_TYPE              | 0x56   |
| PEI_CPU_INVALID_SPEED               | 0x56   |
| PEI\_CPU\_MISMATCH                  | 0x57   |
| PEI\_CPU\_SELF\_TEST\_FAILED        | 0x58   |
| PEI\_CPU\_CACHE_ERROR               | 0x58   |
| PEI\_CPU\_MICROCODE\_UPDATE\_FAILED | 0x59   |
| PEI\_CPU\_NO_MICROCODE              | 0x59   |
| PEI\_CPU\_INTERNAL_ERROR            | 0x5A   |
| PEI\_CPU\_ERROR                     | 0x5A   |
| PEI\_RESET\_NOT_AVAILABLE           | 0x5B   |
| //Recovery                          |        |
| PEI\_RECOVERY\_PPI\_NOT\_FOUND      | 0xF8   |
| PEI\_RECOVERY\_NO_CAPSULE           | 0xF9   |
| PEI\_RECOVERY\_INVALID_CAPSULE      | 0xFA   |
| //S3  Resume                        |        |
| PEI\_MEMORY\_S3\_RESUME\_FAILED     | 0xE8   |
| PEI\_S3\_RESUME\_PPI\_NOT_FOUND     | 0xE9   |
| PEI\_S3\_BOOT\_SCRIPT\_ERROR        | 0xEA   |
| PEI\_S3\_OS\_WAKE\_ERROR            | 0xEB   |
| DXE\_CPU\_ERROR                     | 0xD0   |
| DXE\_NB\_ERROR                      | 0xD1   |
| DXE\_SB\_ERROR                      | 0xD2   |
| DXE\_ARCH\_PROTOCOL\_NOT\_AVAILABLE | 0xD3   |
| DXE\_PCI\_BUS\_OUT\_OF_RESOURCES    | 0xD4   |
| DXE\_LEGACY\_OPROM\_NO\_SPACE       | 0xD5   |
| DXE\_NO\_CON_OUT                    | 0xD6   |
| DXE\_NO\_CON_IN                     | 0xD7   |
| DXE\_INVALID\_PASSWORD              | 0xD8   |
| DXE\_BOOT\_OPTION\_LOAD\_ERROR      | 0xD9   |
| DXE\_BOOT\_OPTION_FAILED            | 0xDA   |
| DXE\_FLASH\_UPDATE_FAILED           | 0xDB   |
| DXE\_RESET\_NOT_AVAILABLE           | 0xDC   |

### Intel  UPI  POST  Codes

| Descrição                                                                                                                                                                                                                                                                                                                                                  | Código |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Inicializar os valores padrão da estrutura de entrada do KTIRC                                                                                                                                                                                                                                                                                             | 0xA0   |
| Coletar informações como SBSP, Modo de Inicialização, tipo de Reset, etc.                                                                                                                                                                                                                                                                                  | 0xA1   |
| Configurar os SADs de IO no SBSP para acessar o espaço de configuração                                                                                                                                                                                                                                                                                     | 0xA2   |
| Configurar o caminho mínimo entre o SBSP e outros soquetes. Adicionar o nó à árvore.<br><br>Analisar o LEP do soquete descoberto.<br><br>Verificar se o sistema tem a topologia suportada. Configurar o caminho de inicialização para o pai que não está diretamente conectado à CPU antiga.<br><br>Configurar o caminho do SBSP para o novo nó descoberto | 0xA3   |
| Configurar os SADs de IO no PBSP para acessar o espaço de configuração                                                                                                                                                                                                                                                                                     | 0xA4   |
| Configurações do sistema que requerem algum tipo de reset                                                                                                                                                                                                                                                                                                  | 0xA5   |
| Sincronizar com os PBSPs                                                                                                                                                                                                                                                                                                                                   | 0xA6   |
| Descoberta de topologia e cálculo de rota                                                                                                                                                                                                                                                                                                                  | 0xA7   |
| Programar rota final                                                                                                                                                                                                                                                                                                                                       | 0xA8   |
| Configurar as definições finais de IO SAD                                                                                                                                                                                                                                                                                                                  | 0xA9   |
| Configurações da camada de protocolo e outras configurações Uncore                                                                                                                                                                                                                                                                                         | 0xAA   |
| Transição de links para operação em velocidade total                                                                                                                                                                                                                                                                                                       | 0xAB   |
| Configurações da camada física                                                                                                                                                                                                                                                                                                                             | 0xAC   |
| Configurações da camada de link                                                                                                                                                                                                                                                                                                                            | 0xAD   |
| Configurações de coerência                                                                                                                                                                                                                                                                                                                                 | 0xAE   |
| O KTIRC está concluído                                                                                                                                                                                                                                                                                                                                     | 0xAF   |

### Intel  UPI  Error  Codes

| Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Código |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| Quando o BSP do sistema tenta configurar o caminho para soquetes remotos ou envia um comando Boot_Go para um soquete remoto em SetupSbspPathToAllSockets() ou SyncUpPbspForReset(). Se o(s) soquete(s) remoto(s) não fizer(em) check-in, ocorrerá um assert; é uma condição fatal, esse erro será registrado. Sem nova tentativa.<br><br>Comportamento do RC: Parar o sistema                                                                                                              | 0xD8   |
| Quando o SBSP tenta adicionar esse soquete remoto à árvore de topologia do sistema em SetupSbspPathToAllSockets(), ocorrem alguns erros na estrutura de dados.<br><br>Sem nova tentativa.<br><br>Comportamento do RC: O soquete atual não é adicionado à árvore.<br><br>Quando o SBSP configura o caminho de inicialização para o pai que não está diretamente conectado à CPU antiga em SetupSbspPathToAllSockets(). O filho não é um vizinho imediato do pai.<br><br>Sem nova tentativa. | 0xDA   |
| Erro na configuração do SAD.<br><br>Comportamento do RC: Parar o sistema                                                                                                                                                                                                                                                                                                                                                                                                                   | 0xDB   |
| Topologia não suportada.<br><br>Comportamento do RC: Parar o sistema                                                                                                                                                                                                                                                                                                                                                                                                                       | 0xDC   |
| O SBSP não consegue encontrar os parâmetros TXEQ do KPIRC para esse link em GetSocketLinkEparams(). Sem nova tentativa.<br><br>Comportamento do RC: Parar o sistema                                                                                                                                                                                                                                                                                                                        | 0xDD   |

### Intel  MRC  POST  Codes

| Descrição                                              | Código |
| ------------------------------------------------------ | ------ |
| Detectar a população de módulos DIMM                   | 0xB0   |
| Configurar a frequência DDR                            | 0xB1   |
| Coletar os dados restantes do SPD                      | 0xB2   |
| Programar registros no nível do controlador de memória | 0xB3   |
| Avaliar os modos RAS e salvar informações de bancos    | 0xB4   |
| Programar registros no nível do canal                  | 0xB5   |
| Inicialização DDRIO                                    | 0xB6   |
| Treinar DDR                                            | 0xB7   |
| Inicializar CLTT/OLTT                                  | 0xB8   |
| Teste e inicialização de memória em hardware           | 0xB9   |
| Executar inicialização de memória                      | 0xBA   |
| Programar mapa de memória e interleaving               | 0xBB   |
| Programar configuração RAS                             | 0xBC   |
| Ferramenta de margem de bancos                         | 0xBD   |
| MRC está concluído                                     | 0xBF   |

### Intel  MRC  Error  Codes

| Descrição                                                                                  | Código |
| ------------------------------------------------------------------------------------------ | ------ |
| Nenhuma memória foi detectada                                                              | 0xE8   |
| Falha no teste de memória                                                                  | 0xEB   |
| Diferentes tipos de módulos DIMM foram detectados instalados no sistema                    | 0xED   |
| Número de HAs encontrados no sistema é maior do que o MAX_HA definido na compilação do MRC | 0xEE   |
| Indica um erro na estrutura da tabela CLTT                                                 | 0xEF   |
| Modo VR inválido, impossível definir VDD do DRAM                                           | 0xF0   |
| Falha ao reservar memória para IOT                                                         | 0xF1   |
| Assert do código de referência                                                             | 0xF2   |
| Frequência do MC não suportada definida                                                    | 0xF3   |
| Não foi possível obter a frequência atual do MC                                            | 0xF4   |

### Intel  PM  POST  Codes

| Descrição                                      | Código |
| ---------------------------------------------- | ------ |
| Início da inicialização da estrutura PPM       | 0xD0   |
| Programação do PPM CSR                         | 0xD1   |
| Programação do PPM MSR                         | 0xD2   |
| Início da inicialização da transição do PState | 0xD3   |
| Saída do PPM                                   | 0xD4   |
| Evento PPM On pronto para inicialização        | 0xD5   |
| Início da inicialização antecipada do IIO      | 0xE0   |
| Pré-treinamento de link                        | 0xE1   |
| Início do treinamento EQ Gen3                  | 0xE2   |
| Início da inicialização da transição do PState | 0xE3   |
| Substituição de parâmetros Gen3                | 0xE4   |
| Fim da inicialização antecipada do IIO         | 0xE5   |
| Início da inicialização tardia do IIO          | 0xE6   |
| Inicialização da porta PCIE                    | 0xE7   |
| Inicialização do IOAPIC                        | 0xE8   |
| Inicialização do VTD                           | 0xE9   |
| Inicialização do IOAT                          | 0xEA   |
| Inicialização do DFX                           | 0xEB   |
| Inicialização do NTB                           | 0xEC   |
| Inicialização de segurança                     | 0xED   |
| Inicialização tardia do IIO                    | 0xEE   |
| Evento IIO On pronto para inicialização        | 0xEF   |
