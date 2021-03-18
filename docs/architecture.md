# Arquitetura e Modelos

A aplicação tem apenas um modelo, o de ocorrências. Um exemplo:

```python
class Occurrence(models.Model):
    description = models.TextField(max_length=200, null=True, blank=True)
    lat = models.FloatField(blank=True, default='')
    lon = models.FloatField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, null=True)
    status = models.TextField(max_length=20, null=True,
                              blank=True, default="POR_VALIDAR")
    category = models.TextField(max_length=20, null=True, blank=True)
    distance_from_hq = models.FloatField(blank=True, default='')
    author = models.ForeignKey(
        'auth.User', related_name='occurrences', on_delete=models.CASCADE)
```

Este modelo vai conter uma descrição, a latitude e longitude da mesma, o estado, categoria, distância até ao escritório da Ubiwhere e o autor associado.

Para ser feito o calculo da distância, foi usada o seguinte método:

```python
def get_distance_from_hq(self, lat, lon):
    coords_1 = (40.646860, -8.642999)
    coords_2 = (lat, lon)
    return distance.distance(coords_1, coords_2).km
```

Este recebe a latitude e longitude da ocorrência e calcula a respetiva distância.

Por fim, o modelo tem também um método de save personalisado, para calcular e guardar a distância automáticamente sempre que é criada uma nova ocorrência.

```python
def save(self, *args, **kwargs):
    self.distance_from_hq = self.get_distance_from_hq(self.lat, self.lon)
    super().save(*args, **kwargs)
```
