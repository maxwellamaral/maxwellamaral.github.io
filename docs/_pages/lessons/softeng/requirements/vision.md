---
title: Obtendo a Visão do Produto
permalink: /lessons/softeng/requirements/vision/
sidebar:
    nav: "softeng-requirements"

layout: single
author_profile: true
toc: true
toc_label: "Conteúdo"
toc_icon: "cog"
toc_sticky: true
header:
    image: /assets/images/gpt/headers/cat_conducting_interview1.jpg
    caption: "Gato realizando uma entrevista junto a um cliente | Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: create a image of a software engineer cat conducting an interview with a client"
---

{% 
  include figure 
  image_path="/assets/images/gpt/cat_conducting_interview1.jpg" 
  alt="Gato realizando uma entrevista junto a um cliente." 
  caption="Crédito da imagem: gerado por IA com Bing por Maxwell Anderson (2023) | Prompt: create a image of a software engineer cat conducting an interview with a client" 
%}
{: .align-center} 

# Introdução

## O que é?

O Documento de Visão do Produto (DVP) é um documento que descreve o produto de software que será desenvolvido, só que de maneira abrangente, não é tão detalhado quanto a listagem de requisitos. Ele descreve o problema que será resolvido, as principais necessidades dos _stakeholders_, as principais funcionalidades do sistema, as restrições do projeto, etc.

## Por que é importante?

Ele é, de longe, a fonte de informação **mais importante** para novos projetos. Através dele você obtém uma visão geral do problema e da necessidade do cliente e dos demais _stakeholders_. 

É um artefato que deve ser atualizado ao longo do projeto, sempre que novas informações forem obtidas.

É difícil iniciar um trabalho de elicitação de requisitos sem que os engenheiros obtenham uma **visão** geral do problema e das necessidades dos _stakeholders_. É importante que você tenha uma visão geral do problema e das necessidades deles antes de iniciar o trabalho de elicitação detalhada dos requisitos. Acaba que se torna um norteador para que futuras questões possam ser elaboradas. Ficará mais fácil dividir suas necessidades em categorias que poderão se tornar módulos do sistema.

Você vai perceber que ele trará uma visão do negócio, bem como sobre as oportunidades e e melhorias no dia-a-dia dos _stakeholders_ no uso do novo produto de software que você irá desenvolver. Ele também trará uma visão sobre as restrições do projeto, como prazos, custos, tecnologias etc.

> 💰🤑💵
> 
> Lembre-se que o DVP poderá ser anexado a um contrato entre as partes!
{: .notice--info}

Tudo que é escrito nele será reutilizado nas próximas etapas e, portanto, tenha muito cuidado com o que escreve.

> **Lembre-se** 💡
>
> Se você é novato em uma empresa ou uma outra instituição, e se você irá fazer manutenção em produtos existentes, o DVP é um ótimo artefato norteador pois ele trará uma visão geral do produto e do negócio.
>
> Torça para que o DVP esteja atualizado e que ele seja um documento bem escrito. 
> 
> - Se ele não estiver atualizado, você terá que fazê-lo. 
> - Se ele não estiver bem escrito, você terá que reescrevê-lo. 
> - E caso ele não exista, você terá que criá-lo.
>
> Se o produto existente for grande e complexo, atue em conjunto com os engenheiros que já trabalham no produto. O site que contém informações sobre o software ajudará muito. Eles poderão te ajudar a entender o produto e a sua arquitetura. Construa dentro do escopo do módulo ou parte do conjunto de funcionalidades que você irá trabalhar.

## Quando deve ser criado?

Ele deve ser criado antes de iniciar o trabalho de elicitação detalhada dos requisitos. 

## Quem deve criá-lo?

Ele deve ser criado pelo engenheiro de software ou engenheiro de requisitos que assume o papel de Elicitador de Requisitos, em conjunto com o cliente e com os demais _stakeholders_.

## Como criá-lo?

Veja a seguir como criar um DVP.

# Documento de Visão do Produto (DVP)

A melhor forma de aprender é partindo de exemplos. Vamos ver um exemplo de um DVP que poderá ser utilizado como exemplo abaixo.

> Atente bem para as explicações em sala de aula!
{: .notice--info}

## Exemplo e template

**Imagens de exemplo**

{%
  include figure
  image_path="/assets/images/lessons/vision-capa.png"
  alt="Capa do Documento de Visão do Produto (DVP) do Sistema de Controle de Garantias de Produtos (SCGP)."
  caption="Crédito da imagem: Maxwell Anderson (2023) | Capa do Documento de Visão do Produto (DVP) do SCGP."
%}
{: .align-center}

{%
  include figure
  image_path="/assets/images/lessons/vision-arch.png"
  alt="Arquitetura do Sistema de Controle de Garantias de Produtos (SCGP)."
  caption="Crédito da imagem: Maxwell Anderson (2023) | Arquitetura ambiental do SCGP."
%}
{: .align-center}

O exemplo acima de [Documento de Visão do Produto (DVP) pode ser visualizado aqui.](https://github.com/maxwellamaral/maxwellamaral.github.io/blob/8f925f5c8882263f475162a990b5da48b6779a3d/specs/requirements/vision.md)

O modelo em "branco" ou _template_ abaixo pode ser copiado e utilizado como base para a criação de um DVP. Ele contém os principais tópicos que devem ser abordados.

O modelo de [Documento de Visão do Produto (DVP) pode ser visualizado aqui.](/lessons/softeng/requirements/vision/model/)

> É crucial que ele seja elaborado a partir de uma entrevista com o cliente e com os demais _stakeholders_ conforme realizado na etapa anterior!
{: .notice--warning}

## Sobre as restrições mencionadas no DVP

Restrições são limitações impostas ao desenvolvimento do sistema ou à sua operação, que podem ter impacto no seu escopo, funcionalidade, desempenho, custo, prazo ou qualidade. Algumas possíveis restrições que podem ser consideradas são:

- **Restrições de hardware**: o sistema pode ter requisitos específicos em termos de capacidade de processamento, memória, armazenamento, rede ou outros componentes de hardware. Restrições de hardware podem afetar tanto a escolha da infraestrutura de TI como a capacidade do sistema em suportar um número maior de usuários ou transações.
- **Restrições de software**: o sistema pode ter dependências específicas em termos de sistemas operacionais, plataformas de desenvolvimento, bibliotecas de software, bancos de dados ou outras ferramentas de software. Restrições de software podem afetar tanto o desenvolvimento do sistema como a sua integração com outros sistemas.
- **Restrições de segurança**: o sistema pode ter requisitos específicos em termos de segurança, como autenticação, autorização, criptografia, auditoria, backup ou recuperação de desastres. Restrições de segurança podem afetar tanto o desenvolvimento do sistema como a sua operação e manutenção.
- **Restrições regulatórias**: o sistema pode estar sujeito a regulamentações ou padrões específicos, como normas de privacidade, segurança, interoperabilidade, acessibilidade ou outras. Restrições regulatórias podem afetar tanto o desenvolvimento do sistema como a sua operação e manutenção, e podem ter implicações legais ou financeiras.
- **Restrições de tempo e custo**: o sistema pode ter limitações em termos de prazo ou orçamento, que podem afetar tanto o escopo do sistema como a qualidade e desempenho do mesmo. Restrições de tempo e custo podem exigir que sejam tomadas decisões difíceis em termos de priorização de requisitos, recursos, riscos ou qualidade.
- **Restrições de usabilidade**: o sistema pode ter requisitos específicos em termos de usabilidade, acessibilidade, localização ou outras características que possam afetar a experiência do usuário. Restrições de usabilidade podem exigir que sejam realizados testes de usabilidade e feedback dos usuários para garantir que o sistema atenda às expectativas do usuário.

É importante que todas essas restrições sejam documentadas e consideradas ao longo do desenvolvimento do sistema, para que sejam tomadas as decisões adequadas e para que o sistema possa ser entregue com a qualidade e desempenho esperados.

Veja exemplos de restrições ao fim do Documento de Visão do Produto (DVP) acima.

# Dica de uso por IA generativa. 🧠

As IAs generativas podem ser utilizadas para gerar conteúdos e textos. Elas podem ser utilizadas para gerar exemplos de DVPs.

> **Atenção!** 🚨
>
> Devemos utilizar estas tecnologias como aliadas a fim de tornar o trabalho produtivo. Todavia, devemos ter cuidado para que não se tornem um obstáculo para a criatividade e para a inovação, pois elas podem acabar gerando conteúdos e textos que não sejam úteis ou mesmo que não sejam verdadeiros.
>
> Também tome cuidado para não infringir os direitos autorais de terceiros. Se você utilizar conteúdos e textos gerados por IA, certifique-se de que eles não infrinjam os direitos autorais de terceiros.
>
> E sempre, sempre, sempre revise o conteúdo gerado por IA. Não confie cegamente no que ela gera. Ela pode gerar conteúdos e textos que não façam sentido ou que não sejam verdadeiros.
{: .notice--danger}

Seguem alguns exemplos prompts e de textos gerados por IA.

## Prompt para descrição de oportunidades de negócios

Para gerar o exemplo de DVP acima, seguem alguns prompts que podem ser utilizados para gerar textos e conteúdos importantes:

> **Pergunta:**
>
> Haja como um especialista em negócios e em marketing. Tenho o seguinte escopo do produto descrito abaixo. Escreva oportunidades de negócios que o produto trará.
>
> "O **Sistema de Controle de Garantias de Produtos (SCGP).** é um sistema que tem como objetivo auxiliar o cliente a controlar as garantias de seus produtos. Será utilizado por clientes que compram produtos com garantia e necessitam que sejam informados quando o prazo de garantia estiver próximo de expirar."
>
>> **Resposta:**
>>
>> O Sistema de Controle de Garantias de Produtos (SCGP) apresenta várias oportunidades de negócios, tais como:
>>
>> 1. **Serviço de assinatura**: ofereça aos clientes um serviço de assinatura, onde eles possam pagar uma taxa mensal para ter acesso ao SCGP. Isso pode ser atraente para clientes que possuem muitos produtos com garantia e desejam um serviço de controle automatizado.
>> 2. **Venda de publicidade**: ao reunir informações sobre os produtos dos clientes, o SCGP pode ser um ótimo veículo para publicidade segmentada. Você pode vender espaço publicitário para empresas que vendem produtos relacionados aos que os clientes já possuem.
>> 3. **Venda de informações**: o SCGP coleta informações valiosas sobre os produtos que os clientes possuem, como a data de compra e o prazo de garantia. Essas informações podem ser vendidas a empresas que desejam conhecer melhor seus clientes e seus hábitos de compra.
>> 4. **Parcerias com varejistas**: o SCGP pode oferecer aos varejistas uma forma de se comunicar com os clientes após a venda. Os varejistas podem oferecer descontos ou promoções exclusivas para clientes que estejam usando o SCGP para controlar suas garantias.
>> 5. **Expansão para outros mercados**: o SCGP pode ser expandido para atender a outros mercados, como o de serviços automotivos ou de eletrônicos. Isso pode ser feito através de parcerias com fabricantes de automóveis ou empresas de eletrônicos, oferecendo um serviço semelhante ao SCGP para seus clientes.
>>
>> Essas são apenas algumas ideias de como o Sistema de Controle de Garantias de Produtos (SCGP) pode gerar oportunidades de negócios. Com criatividade e estratégia, você pode identificar muitas outras maneiras de monetizar este produto e torná-lo um sucesso comercial.

## Prompt para descrição sobre os benefícios que o produto trará

> **Pergunta:**
>
> Quais os benefícios para os clientes que este produto poderá trazer?
>
>> **Resposta:**
>>
>> O Sistema de Controle de Garantias de Produtos (SCGP) oferece diversos benefícios para os clientes, tais como:
>>
>> 1. Facilidade de gerenciamento: o SCGP permite que os clientes gerenciem todas as suas garantias de produtos em um só lugar. Eles não precisam mais se preocupar em lembrar quais produtos possuem garantia, quando a garantia expira ou onde encontrar os documentos de garantia.
>> 2. **Alertas personalizados:** o SCGP envia alertas personalizados aos clientes antes do prazo de garantia expirar, para que eles possam se planejar e tomar as providências necessárias. Isso ajuda a evitar surpresas desagradáveis, como ter que pagar por reparos que deveriam estar cobertos pela garantia.
>> 3. **Melhor experiência do cliente:** com o SCGP, os clientes se sentem mais seguros e confiantes ao comprar produtos com garantia. Eles sabem que terão uma ferramenta confiável para gerenciar suas garantias e que serão notificados quando a garantia estiver prestes a expirar.
>> 4. **Redução do tempo de espera:** se um produto com garantia precisar ser reparado ou substituído, o SCGP pode ajudar o cliente a encontrar as informações de contato corretas da empresa responsável pela garantia. Isso pode reduzir o tempo de espera e evitar a necessidade de entrar em contato com várias empresas diferentes.
>> 5. **Economia de dinheiro:** o SCGP ajuda os clientes a manterem suas garantias em dia e evita que eles precisem pagar por reparos ou substituições de produtos que ainda estão cobertos pela garantia.
>>
>> Esses são apenas alguns dos benefícios que o Sistema de Controle de Garantias de Produtos (SCGP) pode trazer para os clientes. No geral, o SCGP ajuda a simplificar a vida dos clientes, oferecendo uma solução eficaz e conveniente para o gerenciamento de garantias de produtos.

## Prompt para criação de tabela sobre benefícios, problemas resolvidos e afetados

> **Pergunta:**
>
> Descreva os benefícios acima levando em consideração, problemas resolvidos e afetados pelo problema. Construa uma tabela em markdown. Mostre o código-fonte.
>
>> **Resposta:**
>>
>> Com base nas informações que você forneceu anteriormente, aqui está uma tabela em markdown que descreve os benefícios do Sistema de Controle de Garantias de Produtos (SCGP), levando em consideração os problemas resolvidos e os afetados pelo problema:
>>
>> ```markdown
>> | Benefícios                     | Problemas Resolvidos                                                       | Afetados                                      |
>> |--------------------------------|----------------------------------------------------------------------------|-----------------------------------------------|
>> | Facilidade de gerenciamento    | Dificuldade em gerenciar múltiplas garantias de produtos                   | Clientes que compram produtos com garantia    |
>> | Alertas personalizados         | Falta de notificação antes do vencimento da garantia                       | Clientes que compram produtos com garantia    |
>> | Melhor experiência do cliente  | Insegurança em relação à garantia de produtos                              | Clientes que compram produtos com garantia    |
>> | Redução do tempo de espera     | Dificuldade em encontrar informações de contato para acionar a garantia    | Clientes que precisam acionar a garantia      |
>> | Economia de dinheiro           | Despesas desnecessárias com produtos ainda cobertos pela garantia          | Clientes que compram produtos com garantia    |
>> ```

---
Criado em Março de 2023 por *Maxwell Anderson*
