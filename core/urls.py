from django.urls import path, include
from rest_framework import routers
from core import views


router = routers.DefaultRouter()
router.register(r'grupos', views.GrupoViewSet)
router.register(r'usuarios', views.UsuarioViewSet)



urlpatterns = [
    path('', include(router.urls)),

]