from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *

# Create your views here.


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'isbn', 'num_paginas', 'data_lancamento', 'categoria', 'autor', 'idioma', 'editora',
                  'data_cadastro', 'link', 'audio_book']


class EditoraForm(ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'web_site', 'pais']


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'web_site', 'country']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields=['categoria']


def cadastrar_livro(request, template_name='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, template_name, {'form': form})


def listar_livro(request, template_name='livro_list.html'):
    query = request.GET.get("busca")
    if query:
        livro = Livro.objects.filter(nome_iexact=query)
    else:
        livro = Livro.objects.all()
    livros = {'lista': livro}
    return render(request, template_name, livros)


def cadastrar_autor(request, template_name='autor_form.html'):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_autor')
    return render(request, template_name, {'form': form})


def listar_autor(request, template_name='autor_list.html'):
    query = request.GET.get("busca")
    if query:
        autor = Autor.objects.filter(nome__iexact=query)
    else:
        autor = Autor.objects.all()
    autores = {'lista': autor}
    return render(request, template_name, autores)


def remover_livro(request, pk, template_name='livro_delete.html'):
    livro = Livro.objects.get(pk = pk)
    if request.method == "POST":
        livro.delete()
        return redirect('listar_livro')
    return render(request, template_name, {'livro': livro})


def remover_autor(request, pk, template_name='autor_delete.html'):
    autor = Autor.objects.get(pk = pk)
    if request.method == "POST":
        autor.delete()
        return redirect('listar_autor')
    return render(request, template_name, {'autor': autor})


def listar_livros_autor(request, pk, template_name="autor_livro_list.html"):
    livros = Livro.objects.filter(autor = pk)
    return render(request, template_name, {'livros': livros})


def editar_livro(request, pk, template_name="livro_form.html"):
    livro = get_object_or_404(pk = pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livro')
    else:
        form = LivroForm(instance=livro)
    return render(request, template_name, {'form': form})


def editar_autor(request, pk, template_name="autor_form.html"):
    autor = Autor.object_or_404(pk = pk)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autor')
    else:
        form = AutorForm(instance=autor)
    return render(request, template_name, {'form': form})
