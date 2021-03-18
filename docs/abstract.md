# Abstract

Pretende-se uma API REST que permita a gestão de ocorrências em ambiente urbano. As ocorrências devem ter descrição, uma localização geográfica, autor, data de criação, data de actualização, estado (por validar, validado, resolvido) e uma das seguintes categorias:

- CONSTRUCTION: planned road work
- SPECIAL_EVENT: special events (fair, sport event, etc.)
- INCIDENT: accidents and other unexpected events
- WEATHER_CONDITION: weather condition affecting the road
- ROAD_CONDITION: status of the road that might affect travellers (potholes, bad pavement, etc.)

## Requisitos

1. API REST

   - Tem de permitir a adição de ocorrências (com a localização geográfica, e autor associados). Nota: O estado default será sempre por validar quando estas são criadas.

   - Tem de permitir a actualização de ocorrências (para mudar o estado das mesmas para "validadas" por um administrador do sistema)

   - Tem de permitir a filtragem de ocorrências por autor, por categoria e por localização (raio de alcance)

## Notas sobre o exercício

1. A componente da API REST deve ser desenvolvida Flask ou Falcon. É obrigatória a partilha de uma collection Postman para conseguirmos testar rapidamente os endpoints que implementares.

2. A BD deixamos ao teu critério (SQLite, PostgresQL, MySQL,…) - mas recomendamos PostgreSQL com PostGIS para a parte geográfica.

3. Serás também valorizado caso coloques o código implementado no Github.
