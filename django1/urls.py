from django.contrib import admin
from django.urls import path, include


"""
Nota do aluno:
O ideal é que o arquivo urls.py da aplicação core seja o responsável por definir as rotas da aplicação.
Entretanto, o arquivo ficaria muito grande com o decorrer de um projeto com diversas aplicações. O ideial
nesse caso é que a aplicação tenha seu próprio arquivo de rotas, como é o caso do arquivo urls.py da aplicação core.

E como fazer referência ao arquivo de rotas que está na aplicação? Através da função include()."""
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
