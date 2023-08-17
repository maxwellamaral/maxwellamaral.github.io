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