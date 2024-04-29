
# Rodando o projeto

- git clone https://github.com/mouraribeiro/teste-painel-e-sus.git


## Via Docker
docker-compose -f docker-compose.yml  up --build


## Endpoints
Todos os dados:
-  http://localhost:8001/api/v1/atendimentos
#### Exemplos de filtros:
- http://localhost:8001/api/v1/atendimentos?data_atendimento=2023-07-26
- http://localhost:8001/api/v1/atendimentos?condicao_saude=hipertensao&data_atendimento=2023-07-26

## Observações

Uma segunda versão dessa api foi desenvolvida com abordagem de transformar o csv em um banco de dados e pode ser encontrada em:

- https://github.com/mouraribeiro/e-sus-segunda-versao
