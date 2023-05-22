from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import PacientView, ImageView, DoctorView

router = routers.DefaultRouter()
router.register(r'pacients', PacientView, 'pacients')
router.register(r'images', ImageView, 'images')
router.register(r'doctors', DoctorView, 'doctors')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('predecir/', views.predecir, name='predecir'),
    path('docs/', include_docs_urls(title='Django CRUD API', description='RESTful API for managing tasks.')),
]