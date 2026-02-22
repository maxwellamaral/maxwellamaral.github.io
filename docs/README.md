# Preparação do ambiente

1.  Instalar o Ruby
2.  Instalar o Bundler
3.  Instalar as dependências do projeto
4.  Executar o projeto
5.  Instalar puml-for-markdown
6.  Executar o puml-for-markdown em `docs/`
7.  Instalar o servidor PlantUML local
    1.  Instalar o Java JDK
    2.  Instalar o Graphviz
    3.  Instalar o PlantUML
    4.  Usar a extensão PlantUML com id `jebbs.plantuml` no VSCode
    5.  Usar a extensão PlantUML auto generator com id `goohan.plantumlautogenerator` no VSCode
8.  Atualizando a galeria de imagens:

Gere arquivo `pics.txt` em `assets/images/gpt` com o comando

No ChatGPT, gere saída utilizando o prompt.

Leia a lista abaixo e gere código no formato:

\`\`\`markdown  
  
\- url: /assets/images/gpt/nome\_arquivo.jpg   
  
image\_path: /assets/images/gpt/nome\_arquivo.jpg   
  
alt: "nome arquivo"   
  
title: "nome arquivo"   
  
\`\`\`

Lista:

\`\`\`plain   
  
Cole a lista aqui   
  
\`\`\`

Insira o código gerado em `2023-08-22-post-gallery.md`

# Dependências

*   Tema: [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes)
*   Documentação em: [Minimal Mistakes Docs](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)

```
 ls -1 > pics.txt
```

```
    sudo apt install plantuml
```

```
    sudo apt install graphviz
```

```
    sudo apt install default-jdk
```

```
    puml-for-markdown 
```

```
    npm install -g puml-for-markdown
```

```
    bundle exec jekyll serve --livereload --incremental
```

```
    sudo bundle install
```

```
    sudo gem install bundler
```

```
    sudo apt update
    sudo apt-get install ruby-full
    ruby -v
```