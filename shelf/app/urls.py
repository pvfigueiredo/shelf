from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^livro/cadastrar/', cadastrar_livro, name='cadastrar_livro'),
    url(r'^autor/cadastrar/', cadastrar_autor, name='cadastrar_autor'),

    url(r'^livro/listar/', listar_livro, name='listar_livro'),
    url(r'^autor/listar/', listar_autor, name='listar_autor'),

    url(r'^livro/deletar/(?P<pk>[0-9]+)', remover_livro, name='remover_livro'),
    url(r'^autor/deletar/(?P<pk>[0-9]+)', remover_autor, name='remover_autor'),

]