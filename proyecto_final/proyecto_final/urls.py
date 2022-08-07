from django.contrib import admin
from django.urls import path   
from nutrisur.views import create_products, productos, categorias, envases, formulario_prod, search_products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', productos, name ='Healthdrink'),
    path('Category/', categorias, name = 'Category'),
    path('Container/', envases, name = 'Container'),
    path("formulario/", formulario_prod, name = "formulario"),
    path('Formulario_carga_productos/',create_products, name = 'Formulario_carga_productos'),
    path("search-product/", search_products, name = "search_products")
]
