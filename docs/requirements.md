## Requisitos do Projeto

Os requistos do projeto _UnGastos_ foram descritos em forma de **histórias de usuário** e **histórias técnicas**. Uma história de usuário é uma descrição informal de uma necessidade ou funcionalidade na visão de um usuário final. Uma história técnica é a expressão de uma necessidade de infraestrutura ou suporte para a realização de uma história de usuário.

As histórias de usuários foram criadas tendo em mente o acrônimo INVEST.

* As histórias de usuário devem ser **I**ndependentes.
* As histórias de usuário devem ser **N**egociáveis.
* As histórias de usuário devem ser **V**aliosa.
* As histórias de usuário devem ser **E**stimáveis.
* As histórias de usuário devem ser **S**mall (Pequenas).
* As histórias de usuário devem ser **T**estáveis.

Abaixo segue a lista de histórias técnicas e histórias de usuário do projeto.

## Histórias 

### Histórias de Usuário

Eu, como usuário, desejo visualizar um gráfico de maiores gastos da FUB, para acompanhar o uso do dinheiro público pela organização.

Eu, como usuário, desejo filtrar o gráfico de gastos por mês, para visualizar quais meses são os que mais consomem o orçamento da FUB.

Eu, como usuário, desejo filtrar o gráfico de gastos por natureza detalhada, para visualizar qual a natureza das despesas que mais consomem o orçamento da FUB.

Eu, como usuário, desejo visualizar um gráfico de fontes de recurso, para acompanhar qual a fonte de recurso mais usada pela FUB para cobrir suas despesas.

---

As histórias de usuário abaixo são possíveis expansões do escopo, passíveis de realização caso exista tempo hábil.


Eu, como usuário, desejo visualizar um indicador do orçamento anual versus o que foi gasto até o momento, para acompanhar quanto a FUB dinheiro ainda pode ser utilizado pela FUB.

Eu, como usuário, desejo visualizar um indicador de despesas estranhas, para acompanhar possíveis usos indevidos do dinheiro público.

Eu, como usuário, desejo visualizar um ranking de credores, para me informar de quais são os indivíduos e organizações que mais recebem dinehiro da FUB.

## Restrições

O _UnGastos_ será um site desenvolvido em Python utilizando o framework web Django. Os dados utilizados para popular as possíveis tabelas e gráficos do site serão do ano de 2017, já que este ano contém dados de todos os meses. 

A tabela com os gastos de 2017 para cada mês pode ser encontrada neste [link][tabela-gastos].


[tabela-gastos]:http://www.unb.br/documentos/transparencia-unb/2-publicacoes/650-execucao-das-despesas-na-fub-2018
