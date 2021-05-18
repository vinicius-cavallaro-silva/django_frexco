from django.contrib import admin
from django.urls import path
from .CRM_APP import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("organizacoes/", views.OrganizacoesView.as_view()),
    path("negocios/", views.NegociosView.as_view()),
    path("atividades/", views.AtividadesView.as_view()),
]
