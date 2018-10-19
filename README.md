## unGastos

[Logo do Projeto]

O projeto UnGastos é tem como objetivo auxiliar o cidadão comum a fiscalizar os gastos da Universidade de Brasília.

O site utiliza informações das [tabelas de execução de despesas] disponíveis no site da Universidade.

## Informações Úteis

[Documento de Requisitos do Projeto]


[tabelas de execução de despesas]: https://www.unb.br/documentos/2-publicacoes/658-execucao-das-despesas-na-fub-2018

---

## Configuração do Ambiente com Docker

Primeiramente é necessário a instalação do Docker, que pode ser encontrado [aqui], e do docker-compose, que pode ser encontrado [aqui][compose].

Após a instalação basta executar o comando:

```
docker-compose up
```

Na pasta do projeto, e o servidor _django_ será executado.


### Configuração Manual do Container

Na pasta onde se encontra o Dockerfile do projeto, execute o comando abaixo no terminal, onde deve-se substituir "NomeDaImagem" por um nome de sua escolha.

`sudo docker build -t NomeDaImagem ./`

Em seguida, para a criação do container que será usado como isolador de ambiente, rode o seguinte comando, novamente o "NomeDoConteiner" fica a escolha do usuário, já o "NomeDaImagem" deve ser o mesmo utilizado no passo anterior.

`sudo docker run -it --name NomeDoConteiner NomeDaImagem bash`

Depois desse comando você estará no shell interativo do container. Para sair/desligar o container, basta digitar, no terminal do container:

`exit`

ou usar o atalho

`Ctrl + d`

Caso deseje acessar novamente o container, utilize o seguinte comando:

`sudo docker exec -it NomeDoContainer bash`

#### Outros comandos Úteis

Iniciar um Container:

`sudo docker start NomeDoContainer`

Parar um Container:

`sudo docker stop NomeDoContainer`

Listar os Containers

`sudo docker ps -a`

Remover Containers

`sudo docker rm NomeDoContainer`

ou

`sudo docker rm IdDoContainer`

Listar as Imagens

`sudo docker images`

Remover Imagens

`sudo docker rmi NomeDaImagem`

[aqui]:
https://docs.docker.com/install/
[compose]:https://docs.docker.com/compose/install/
