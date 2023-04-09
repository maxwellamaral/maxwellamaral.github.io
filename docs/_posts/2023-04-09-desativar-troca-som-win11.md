---
layout: posts
title:  "Como impedir que o Windows 11 realize a troca de saída de som ao conectar novo dispositivo de som"
---

<figure>
    <img src="../assets/images/gpt/cat_studying_glasses3.jpg" width="350" alt="Gato estudando usando óculos. Prompt: Create an image of a cat studying software engineering">
    <figcaption>Gato estudando.</figcaption>
    <br>
    <small>Fonte: gerado por IA com Bing por Maxwell Anderson (2023)</small>
</figure>

# Introdução

Ao utilizar um aplicativo de mesa de som, como por exemplo o VoiceMeeter, o Windows 11 realiza a troca de saída de som ao conectar um novo dispositivo de som, como por exemplo um fone de ouvido.

Isso pode ser um problema para quem utiliza o VoiceMeeter para realizar a gravação de áudio, pois o Windows 11 irá trocar a saída de som para o fone de ouvido, e o VoiceMeeter não irá mais gravar o áudio.

# Solução

Para impedir que o Windows 11 realize a troca de saída de som ao conectar um novo dispositivo de som, siga os passos abaixo:

1. Pressione a tecla ‘Windows’ + ‘R’ para abrir a caixa de diálogo ‘Executar’.
2. Digite _‘regedit’_ e pressione **‘Enter’** para abrir o Editor do Registro.
3. Navegue até a seguinte chave: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Render`
4. Clique com o botão direito do mouse em ‘Render’ e selecione **‘Novo’** > **‘Valor DWORD (32 bits)’**.
5. Nomeie o novo valor como **‘DisableDeviceEnumeration’** e pressione **‘Enter’**.
6. Clique duas vezes no valor recém-criado e defina o valor como **‘1’**.
7. Clique em **‘OK’** para salvar as alterações.

Espero que isso ajude!

Fonte: conversa com o Bing, 09/04/2023.
