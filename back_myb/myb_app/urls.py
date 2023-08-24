# from django.urls import include, path, re_path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from myb_app import viewsets
# from rest_framework import permissions, routers

# from . import views

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1.0',
#         description="Snack bar application",
#         owner="Marques Igor",
#         contact_owner="contato@marquesigor.com.br",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# route = routers.SimpleRouter()
# route.register(r'paes', viewsets.AdicionarPaesViewSet, basename='paes')
# route.register(r'carnes', viewsets.AdicionarCarneViewSet, basename='carnes')
# route.register(r'opcionais', viewsets.AdicionarOpcionalViewSet,
#                basename='opcionais')
# route.register(r'status-burguer', viewsets.AdicionarStatusBurguerViewSet,
#                basename='status_burguer')
# route.register(r'burguers', viewsets.AdicionarBurguerViewSet,
#                basename='burguers')

# app_name = 'myb_app'


# urlpatterns = [
#     path('index/', views.index, name='index'),
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
#          name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger',
#          cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc',
#          cache_timeout=0), name='schema-redoc'),
# ]

from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from myb_app import viewsets
from rest_framework import permissions, routers

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1.0',
        description="Snack bar application",
        contact=openapi.Contact(name="Marques Igor",
                                email="contato@marquesigor.com.br"),
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('', include(route.urls)),
]
