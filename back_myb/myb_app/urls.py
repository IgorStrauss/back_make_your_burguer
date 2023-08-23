from django.urls import include, path
from myb_app import viewsets
from rest_framework import routers

from . import views

route = routers.SimpleRouter()
route.register(r'paes', viewsets.AdicionarPaesViewSet, basename='paes')
route.register(r'carnes', viewsets.AdicionarCarneViewSet, basename='carnes')
route.register(r'opcionais', viewsets.AdicionarOpcionalViewSet,
               basename='opcionais')
route.register(r'status-burguer', viewsets.AdicionarStatusBurguerViewSet,
               basename='status_burguer')
route.register(r'burguers', viewsets.AdicionarBurguerViewSet,
               basename='burguers')

app_name = 'myb_app'


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', include(route.urls)),
]
