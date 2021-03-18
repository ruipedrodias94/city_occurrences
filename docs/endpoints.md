# Endpoints da aplicação

Nesta seção são apresentados os diversos endpoints da aplicação. Para a chamada de todos os endpoints, o utilizador deve estar autenticado.

## Utilizador de sistema

URL:

```url
http://localhost:8000/users/
```

MÉTODOS:

```HTTP
POST - Permite o registo de novos utilizadores
GET - Retorna uma lista de todos os utilizadores registados no sistema
```

URL:

```url
http://localhost:8000/users/{pk} - pk = chave primária
```

MÉTODOS:

```HTTP
GET - Retorna em detalhe o user com esse valor de chave primária
```

## ocorrências

URL:

```url
http://localhost:8000/occurrences/
```

MÉTODOS:

```HTTP
POST - Permite o registo de novas ocorrências
GET - Retorna uma lista de todos as ocorrências do sitema
```

URL:

```url
http://localhost:8000/occurrences/{pk} - pk = chave primária
```

MÉTODOS:

```HTTP
PUT - Permite fazer update a uma ocorrência com o valor de chave primária - Apenas administradores de sistema
GET - Retorna em detalhe a ocorrência com esse valor de chave primária
```

URL:

```url
http://localhost:8000/occurrences/?author=
```

MÉTODOS:

```HTTP
GET - Retorna uma lista de todos as ocorrências do sitema com o autor descrito (chave primária do autor)
```

URL:

```url
http://localhost:8000/occurrences/?category=
```

MÉTODOS:

```HTTP
GET - Retorna uma lista de todos as ocorrências do sitema com a categoria descrita. (CONSTRUCTION, SPECIAL_EVENT, INCIDENT, WEATHER_CONDITION, ROAD_CONDITION)
```

URL:

```url
http://localhost:8000/occurrences/?distance=
```

MÉTODOS:

```HTTP
GET - Retorna uma lista de todos as ocorrências do sitema com a distancia ao escritório da Ubiwhere menor que a descrita.
```
