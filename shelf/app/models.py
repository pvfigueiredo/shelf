from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class Categoria(models.Model):
    categoria = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.categoria


class Country(models.Model):
    pais = models.CharField(max_length=50, null=False, unique=True)
    sigla_pais = models.CharField(max_length=3, null=False, unique=True)

    def __str__(self):
        return self.sigla_pais


class Autor(models.Model):
    nome = models.CharField(max_length=50, null=False, unique=True)
    web_site = models.URLField(null=False)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=50, null=False,unique=True)
    web_site = models.URLField()
    pais = models.ForeignKey(Country)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=50, null=False)
    isbn = models.PositiveIntegerField(unique=True)
    num_paginas = models.PositiveIntegerField()
    data_lancamento = models.DateField()
    categoria = models.ForeignKey(Categoria)
    autor = models.ForeignKey(Autor)
    idioma = models.CharField(max_length=20, null=False)
    editora = models.ForeignKey(Editora)
    data_cadastro = models.DateTimeField(default=datetime.now(), null=False)
    link = models.URLField()
    audio_book = models.URLField()

    def __str__(self):
        return self.nome
