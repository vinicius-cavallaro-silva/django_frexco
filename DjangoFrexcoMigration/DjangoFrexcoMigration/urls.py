from django.contrib import admin
from django.urls import path
from CRM_APP import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register('organizacoes',views.OrganizacoesViewSet)
router.register('negocios',views.NegociosViewSet)
router.register('atividades',views.AtividadesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
