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