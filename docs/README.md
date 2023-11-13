# Preparação do ambiente

1. Instalar o Ruby 
    ```bash
        sudo apt update
        sudo apt-get install ruby-full
        ruby -v
    ```
2. Instalar o Bundler
    ```bash
        sudo gem install bundler
    ```
3. Instalar as dependências do projeto
    ```bash
        sudo bundle install
    ```
4. Executar o projeto
    ```bash
        bundle exec jekyll serve --livereload --incremental
    ```
5. Instalar puml-for-markdown
    ```bash
        npm install -g puml-for-markdown
    ```
6. Executar o puml-for-markdown em `docs/`
    ```bash
        puml-for-markdown 
    ```
7. Instalar o servidor PlantUML local 
    1. Instalar o Java JDK
        ```bash
            sudo apt install default-jdk
        ```
    2. Instalar o Graphviz
        ```bash
            sudo apt install graphviz
        ```
    3. Instalar o PlantUML
        ```bash
            sudo apt install plantuml
        ```
    4. Usar a extensão PlantUML com id `jebbs.plantuml` no VSCode
    5. Usar a extensão PlantUML auto generator com id `goohan.plantumlautogenerator` no VSCode
 8. Atualizando a galeria de imagens:
    1. Gere arquivo `pics.txt` em `assets/images/gpt` com o comando 
       ```bash
        ls -1 > pics.txt
       ```
    2. No ChatGPT, gere saída utilizando o prompt.
    
        Leia a lista abaixo e gere código no formato:

        \```markdown<br>
        \- url: /assets/images/gpt/nome_arquivo.jpg <br> 
            image_path: /assets/images/gpt/nome_arquivo.jpg <br>
            alt: "nome arquivo" <br>
            title: "nome arquivo" <br>
        \```

        Lista:

        \```plain <br>
        Cole a lista aqui <br>
        \```

    3. Insira o código gerado em `2023-08-22-post-gallery.md`


# Dependências

- Tema: [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes)
- Documentação em: [Minimal Mistakes Docs](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)