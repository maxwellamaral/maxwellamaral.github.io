# Repositórios de códigos de exemplos

Para fins de exemplificação, esta pasta contem os códigos de exemplos que se baseiam nas especificações do curso de Engenharia de Software.

Assim sendo temos a seguinte arquitetura de pastas:

```
|
|--- backend: conterá tecnologias de backend.
|--- frontend: conterá tecnologias de frontend.
|--- monolithic: conterá tecnologias baseadas em arquiteturas monolíticas.
```

Em cada uma das pastas acima, teremos uma estrutura de pastas nomeadas conforme as tecnologias adotadas.

```
|
|--- dj: conterá tecnologias baseadas em Python e Django
|--- js: conterá tecnologias baseadas em frameworks com JavaScript
|--- fk: conterá tecnologias baseadas em Python e Flask
```

Cada tecnologia será armazenada em repositório próprio, sendo adicionado ao repositório principal utilizando **submódulos do Git**.

* Conteúdo sobre _[Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)_.
  * Para adicionar um submódulo ao repositório principal, utilize o comando `git submodule add <url> <path>`.
    * Exemplo: `git submodule add https://github.com/chaconinc/DbConnector`
    * Será adicionado um arquivo `.gitmodules` na raiz do repositório principal.
    * Será adicionada a pasta `DbConnector` na raiz do repositório principal.

## Monolithic

Exemplos:

* [x] Django - `./monolithic/dj` como submódulo de <https://github.com/maxwellamaral/garantias-mono-dj.git>
* [ ] dotNet - `./monolithic/dn`