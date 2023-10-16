from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

LISTA_CATEGORIAS = (
    ("COMEDIA", "Comédia"),
    ("ACAO", "Ação"),
    ("AVENTURA", "Aventura"),
    ("SERIEs", "Series"),
    ("OUTROS", "Outros"),
)
#criar filmes
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


# criar episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo



# criar usuario

class Usuario(AbstractUser):
    filme_vistos = models.ManyToManyField("Filme")


